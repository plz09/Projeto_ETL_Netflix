# Projeto de Limpeza de Dados

## Descrição do Projeto

Este projeto tem como objetivo praticar processos ETL com dados fictícios de camapanha da Netflix. Foi desenvolvido na mentoria da DIO para realizar a limpeza e transformação de dados provenientes de arquivos Excel localizados no diretório `src/data/raw`. Os dados são combinados em um único conjunto de dados limpo, que é então salvo no arquivo `src/data/data_ready/clean.xlsx`.

## Pré-requisitos

- Python 3.x
- Biblioteca pandas
- Biblioteca glob
- Arquivos Excel no diretório `src/data/raw`

## Instalação

1. Certifique-se de ter o Python 3.x instalado. Caso contrário, você pode baixá-lo [aqui](https://www.python.org/downloads/).

2. Instale as bibliotecas necessárias usando o seguinte comando no terminal:

    ```bash
    pip install pandas
    ```

3. Execute o script Python para iniciar o processo de limpeza de dados:

    ```bash
    python script.py
    ```

## Funcionalidades

- Leitura de arquivos Excel no diretório `src/data/raw`.
- Criação de uma tabela consolidada a partir dos dados extraídos dos arquivos.
- Adição das colunas 'filename', 'location' e 'campaign' ao conjunto de dados, com base no nome do arquivo e na análise da coluna 'utm_link'.
- Exportação do conjunto de dados limpo para o arquivo `src/data/data_ready/clean.xlsx`.

## Observações

- Caso ocorram erros durante a leitura dos arquivos, detalhes serão exibidos no console.
