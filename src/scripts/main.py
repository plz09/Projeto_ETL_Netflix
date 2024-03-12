import pandas as pd
import os
import glob

folder_path = 'src\\data\\raw'

excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print('Nenhum arquivo compatível encontrado.')
else:

    dfs = []

    for excel_file in excel_files:

        try:
            df_temp = pd.read_excel(excel_file)
            print(df_temp)
        except Exception as e:
            print(f'Erro ao ler o arquivo. {excel_file} : {e}')