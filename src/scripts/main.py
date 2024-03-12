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

            # Cria coluna location consoante ao nome do arquivo

            file_name = os.path.basename(excel_file)

            df_temp['filename'] = file_name

            if 'brasil' in file_name:
                df_temp['location'] = 'br'
            elif 'france' in file_name:
                df_temp['location'] = 'fr'
            elif 'italian' in file_name:
                df_temp['location'] = 'it'

            # Cria coluna 'campaign' 
                
            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')
            dfs.append(df_temp)

        except Exception as e:
            print(f'Erro ao ler o arquivo. {excel_file} : {e}')

if dfs:

    # Concatena as tabelas para formar uma tabela só
    result = pd.concat(dfs, ignore_index=True)

    # Caminho de saída
    output_file = os.path.join('src', 'data', 'data_ready', 'clean.xlsx')

    # Configura motor de escrita
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    # Leva os dados do result para serem escritos no motor do excel configurado
    result.to_excel(writer, index=False)
    # Salva o arquivo de excel
    writer._save()
else:
    print('Nenhum dado para salvar.')



