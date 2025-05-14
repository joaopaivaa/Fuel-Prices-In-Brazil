import pandas as pd
from download_functions import download_LPG, download_Gasoline_Ethanol, download_Diesel_CNG
from datetime import datetime

today = datetime.now()

if today.day == 10:

    # LPG Prices

    df_lpg = pd.read_parquet('LPG Prices.parquet', engine='pyarrow')

    df_lpg_past_4_weeks = download_LPG()

    if df_lpg.equals(df_lpg_past_4_weeks):
        print('LPG: No new data to append\n')
    else:
        print('LPG: New data to append\n')
        df_lpg = pd.concat([df_lpg, df_lpg_past_4_weeks])
        df_lpg.to_parquet('LPG Prices.parquet', index=False, engine='pyarrow')

    # Gasoline Ethanol Prices

    df_gasoline_ethanol = pd.read_parquet('Gasoline and Ethanol Prices.parquet', engine='pyarrow')

    df_gasoline_ethanol_past_4_weeks = download_Gasoline_Ethanol()

    if df_gasoline_ethanol.equals(df_gasoline_ethanol_past_4_weeks):
        print('Gasoline and Ethanol: No new data to append\n')
    else:
        print('Gasoline and Ethanol: New data to append\n')
        df_gasoline_ethanol = pd.concat([df_gasoline_ethanol, df_gasoline_ethanol_past_4_weeks])
        df_gasoline_ethanol.to_parquet('Gasoline and Ethanol Prices.parquet', index=False, engine='pyarrow')

    # Diesel and CNG Prices

    df_diesel_cng = pd.read_parquet('Diesel and CNG Prices.parquet', engine='pyarrow')

    df_diesel_cng_past_4_weeks = download_Diesel_CNG()

    if df_diesel_cng.equals(df_diesel_cng_past_4_weeks):
        print('Diesel and CNG: No new data to append\n')
    else:
        print('Diesel and CNG: New data to append\n')
        df_diesel_cng = pd.concat([df_diesel_cng, df_diesel_cng_past_4_weeks])
        df_diesel_cng.to_parquet('Diesel and CNG Prices.parquet', index=False, engine='pyarrow')