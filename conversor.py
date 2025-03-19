import pandas as pd

# Nome do arquivo de entrada e saída
input_file = 'extrato_mercado_bitcoin2.csv'
output_file = 'extrato_koinly.csv'

# Lendo o arquivo CSV do Mercado Bitcoin
df = pd.read_csv(input_file)

# Convertendo todas as colunas para minúsculas
df.columns = df.columns.str.lower()

# Garantindo que a coluna 'quantidade' seja numérica
df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce')

# Lista para armazenar os dados convertidos
data_koinly = []

# Função para identificar e converter a data para o formato correto
def convert_date(date_str):
    try:
        # Tenta o formato mais recente: dd/mm/yyyy HH:MM:SS
        return pd.to_datetime(date_str, format='%d/%m/%Y %H:%M:%S', dayfirst=True).strftime('%Y-%m-%d %H:%M:%S UTC')
    except ValueError:
        # Se falhar, tenta o formato anterior: yyyy-mm-dd HH:MM:SS
        return pd.to_datetime(date_str).strftime('%Y-%m-%d %H:%M:%S UTC')

# Mapeamento de categorias para o Koinly
for _, row in df.iterrows():
    data = {
        # Usa a função para converter a data
        'Date': convert_date(row['data']),
        'Sent Amount': '',
        'Sent Currency': '',
        'Received Amount': '',
        'Received Currency': '',
        'Fee Amount': '',
        'Fee Currency': '',
        'Net Worth Amount': '',
        'Net Worth Currency': '',
        'Label': row['categoria'],
        'Description': f"{row['categoria']} - {row['moeda']}",
        'TxHash': ''
    }

    if row['quantidade'] < 0:
        # Transação de saída (venda, saque)
        data['Sent Amount'] = abs(row['quantidade'])
        data['Sent Currency'] = row['moeda']
    else:
        # Transação de entrada (compra, depósito)
        data['Received Amount'] = row['quantidade']
        data['Received Currency'] = row['moeda']

    data_koinly.append(data)

# Convertendo para DataFrame
df_koinly = pd.DataFrame(data_koinly)

# Salvando para CSV no formato do Koinly
df_koinly.to_csv(output_file, index=False)

print(f'Arquivo convertido para o formato Koinly salvo em: {output_file}')
