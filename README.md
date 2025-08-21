# TFM – Simulador corporativo de inversión con ML/DL y Big Data (EE. UU.)

Este repositorio contiene el código fuente, notebooks y artefactos de mi **Trabajo Fin de Máster (TFM)**. El proyecto construye un **simulador de inversión** que predice retornos a **5, 20 y 180 días** para **S&P 500, DJIA, NASDAQ, Russell 2000 y Wilshire 5000**, integrando **indicadores técnicos** y **variables macroeconómicas** sobre una arquitectura **Lakehouse–Medallion** en Azure. Se entrenan modelos **HistGradientBoosting**, **LSTM** y **Híbrido HGB+LSTM** para **regresión y clasificación**.

---

## Estructura del repositorio

Incluye los cuadernos y utilidades clave del pipeline. La organización sigue las capas Medallion y los modelos por índice.

  market/\
    ├─ 01_Ingesta_Bronze_Indices.ipynb\
    ├─ 01_Ingesta_Bronze_Macros.ipynb\
    ├─ 02_Capa_Silver_Indices.ipynb\
    ├─ 02_Capa_Silver_Macros.ipynb\
    ├─ 03_build_gold_features.ipynb\
    ├─ 04_eda_and_modeling SP500.ipynb\
    ├─ 04_eda_and_modeling DJIA.ipynb\
    ├─ 04_eda_and_modeling NASDAQ.ipynb\
    ├─ 04_eda_and_modeling RUSSELL2000.ipynb\
    ├─ 04_eda_and_modeling WILSHIRE5000.ipynb\
    ├─ 05_TFM_Simulador_5d20d180d_IndicesUSA.pbix\
    ├─ bronze_builder.py\
    └─ utils_adls.py
  
## Datos
- **Fuente**
  - Yahoo Finance (`yfinance`): ^GSPC, ^DJI, ^IXIC, ^RUT, ^W5000 (1992–2025).
  - FRED (`fredapi`): 30 series (FEDFUNDS, CPI, UNRATE, DGS10, M2SL, VIXCLS, etc.).
- **Frecuencia y alineación**: calendario **diario** con *forward-fill*.

## Tecnologías principales

**Python 3.11**, Jupyter • `pandas`, `numpy`, `scikit-learn`, **PyTorch** • `pyarrow` • `yfinance`, `fredapi` • Azure Data Lake (**adlfs**, `fsspec`) • **Power BI**.

## Credenciales (crear .env)
AZ_STORAGE_ACCOUNT=xxxx\
AZ_ACCOUNT_KEY=xxxx\
FRED_API_KEY=xxxx

## Autor
Miguel Alejandro Cortez Surio\
Máster en Big Data y Analytics - UAX

