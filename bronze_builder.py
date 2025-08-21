# bronze_builder.py
import os, glob, pandas as pd
from datetime import datetime
from utils_adls import upload_bytes

RAW_DIR   = "data/raw/indices"
BRONZE_ADLS_PREFIX = "bronze/indices"   # dentro del contenedor "market"

SOURCE = "yfinance"
INGEST_TS = datetime.utcnow().isoformat(timespec="seconds")+"Z"

# --- procesa cada archivo raw ---
for parquet_file in glob.glob(f"{RAW_DIR}/*.parquet"):
    ticker = pathlib.Path(parquet_file).stem              # p.ej. "SP500"
    df = pd.read_parquet(parquet_file)

    # añade metadatos
    df = (
        df.reset_index()                      # 'date' pasa a columna
          .assign(
              ingest_ts = INGEST_TS,
              source    = SOURCE,
              year      = lambda x: pd.to_datetime(x["date"]).dt.year
          )
    )

    # escribe Parquet repartido por año
    for yr, group in df.groupby("year"):
        local_tmp = f"tmp_{ticker}_{yr}.parquet"
        group.to_parquet(local_tmp, index=False, engine="pyarrow")

        remote_path = f"{BRONZE_ADLS_PREFIX}/{ticker}/year={yr}/{ticker}_{yr}.parquet"
        with open(local_tmp, "rb") as f:
            upload_bytes(remote_path, f.read(), content_type="application/octet-stream")
        os.remove(local_tmp)
        print(f"▲ subido {remote_path}  ({len(group)} filas)")
