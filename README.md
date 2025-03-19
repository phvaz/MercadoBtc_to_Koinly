# Conversão de Extrato de Mercado Bitcoin para Koinly

Este repositório contém um script Python para converter extratos de transações de criptomoedas do Mercado Bitcoin para o formato compatível com o Koinly. O Koinly é uma plataforma de rastreamento de portfólio de criptomoedas e gerenciamento de impostos, e esse script facilita a importação de transações do Mercado Bitcoin para o Koinly.

## Funcionalidade

O script realiza as seguintes ações:

- Lê um arquivo CSV contendo as transações do Mercado Bitcoin.
- Converte as transações para o formato esperado pelo Koinly.
- Mapeia categorias e moedas de acordo com o padrão do Koinly.
- Gera um novo arquivo CSV com os dados convertidos para serem importados diretamente no Koinly.

## Como Usar

1. **Prepare o arquivo de entrada**: Exporte seu extrato de transações do Mercado Bitcoin para um arquivo CSV com o nome `extrato_mercado_bitcoin.csv`. O arquivo precisa ter as seguintes colunas:
   - `Data`: Data da transação.
   - `Categoria`: Categoria da transação (ex: compra, venda, etc.).
   - `Moeda`: Tipo de moeda da transação (ex: BTC, ETH).
   - `Quantidade`: Quantidade de moedas (números negativos indicam transações de saída).

2. **Execute o script**:
   - Certifique-se de ter o Python 3.x instalado.
   - Instale a dependência `pandas`:
     ```bash
     pip install pandas
     ```
   - Execute o script `converter.py`:
     ```bash
     python converter.py
     ```

3. **Arquivo de saída**: O script criará um arquivo CSV chamado `extrato_koinly.csv`, que estará no formato compatível com o Koinly.

## Exemplo de Estrutura de Arquivo CSV de Entrada

O arquivo `extrato_mercado_bitcoin.csv` deve seguir este formato:

```csv
Data,Categoria,Moeda,Quantidade
2023-01-01,Compra,BTC,0.5
2023-01-02,Venda,BTC,-0.2
