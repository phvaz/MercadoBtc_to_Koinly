import pandas as pd

# Nome do arquivo de entrada e saída
input_file = 'extrato_mercado_bitcoin.csv'
output_file = 'extrato_koinly.csv'

# Lendo o arquivo CSV do Mercado Bitcoin
df = pd.read_csv(input_file)

# Lista para armazenar os dados convertidos
data_koinly = []

# Mapeamento de categorias para o Koinly
for _, row in df.iterrows():
    data = {
        'Date': pd.to_datetime(row['Data']).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'Sent Amount': '',
        'Sent Currency': '',
        'Received Amount': '',
        'Received Currency': '',
        'Fee Amount': '',
        'Fee Currency': '',
        'Net Worth Amount': '',
        'Net Worth Currency': '',
        'Label': row['Categoria'],
        'Description': f"{row['Categoria']} - {row['Moeda']}",
        'TxHash': ''
    }

    if row['Quantidade'] < 0:
        # Transação de saída (venda, saque)
        data['Sent Amount'] = abs(row['Quantidade'])
        data['Sent Currency'] = row['Moeda']
    else:
        # Transação de entrada (compra, depósito)
        data['Received Amount'] = row['Quantidade']
        data['Received Currency'] = row['Moeda']

    data_koinly.append(data)

# Convertendo para DataFrame
df_koinly = pd.DataFrame(data_koinly)

# Salvando para CSV no formato do Koinly
df_koinly.to_csv(output_file, index=False)

print(f'Arquivo convertido para o formato Koinly salvo em: {output_file}')
