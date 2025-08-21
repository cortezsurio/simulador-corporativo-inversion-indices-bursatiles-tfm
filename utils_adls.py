# utils_adls.py
import os
from dotenv import load_dotenv
from azure.storage.filedatalake import DataLakeServiceClient, ContentSettings

load_dotenv()
ACCOUNT     = os.getenv("AZ_STORAGE_ACCOUNT")
ACCOUNT_KEY = os.getenv("AZ_ACCOUNT_KEY")
CONTAINER   = "market"

def _client():
    """Devuelve un DataLakeServiceClient para usar en otros scripts."""
    return DataLakeServiceClient(
        account_url=f"https://{ACCOUNT}.dfs.core.windows.net",
        credential=ACCOUNT_KEY,
    )

svc = _client()   # se usa internamente en upload_bytes


def upload_bytes(path_in_container: str, data: bytes,
                 content_type: str = "application/octet-stream") -> None:
    """
    Sube el archivo a ADLS Gen2; si ya existe lo sobrescribe.
    """
    file_client = svc.get_file_client(CONTAINER, path_in_container)

    # ►-- una única operación: crea o reemplaza
    file_client.upload_data(
        data,
        overwrite=True,
        content_settings=ContentSettings(content_type=content_type),
    )
