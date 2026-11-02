
Este projeto é uma ferramenta em Python desenvolvida para simular rodadas de jogos de caça-níquel utilizando o **Método de Monte Carlo**. A simulação modela o comportamento financeiro e estatístico de múltiplos jogadores ao longo de diversas rodadas, exportando os resultados detalhados em um arquivo CSV.

## 📌 Funcionalidades

- **Simulação Estocástica**: Utiliza a geração de números pseudoaleatórios para simular o resultado de cada giro (`Vitoria` ou `Derrota`).
- **Controle de Saldo**: Acompanha o saldo acumulado de cada jogador rodada a rodada, respeitando a trava de saldo mínimo para apostas.
- **Exportação dos Dados**: Gera um arquivo `.csv` estruturado contendo o histórico completo dos giros efetuados.

---

## ⚙️ Regras da Simulação

Por padrão, a função utiliza as seguintes premissas financeiras e probabilísticas:

- **Probabilidade de Vitória (P)**: 16% (0,16)
- **Multiplicador de Ganho**: 5X o valor apostado
- **Valor por Aposta**: R$10,00
- **Saldo Inicial por Jogador**: R$ 500,00
- **Retorno Esperado por Giro (E)**:
  E = (10 x 5,0 x 0,16) - 10 = 8 - 10 = -R$ 2,00
  *(Ou seja, a casa possui uma vantagem estatística esperada de 20% por giro)*.

---

## 📁 Estrutura do Arquivo Exportado (`dados_16p.csv`)

O arquivo gerado é separado por ponto e vírgula (`;`) e contém as seguintes colunas:

| Coluna | Descrição |
| :--- | :--- |
| `ID_Jogador` | Identificador único do jogador (ex: `Jogador_01`) |
| `Numero_Giro` | Número sequencial do giro do jogador |
| `Valor_Apostado` | Valor em dinheiro apostado na rodada |
| `Resultado` | Status do giro (`Vitoria` ou `Derrota`) |
| `Valor_Ganho` | Valor bruto recebido na rodada |
| `Resultado_Financeiro_Giro` | Lucro ou prejuízo líquido da rodada |
| `Saldo_Acumulado` | Saldo restante do jogador após o processamento da rodada |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas**: Para manipulação de dados e geração do arquivo CSV.
- **Random**: Módulo nativo do Python para geração de probabilidades aleatórias.

---

## 🚀 Como Executar

### 1. Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Instale a biblioteca `pandas` executando:

```bash
pip install pandas
```

### 2. Execução

Execute o script Python contendo a função:

```bash
python main.py
```

Após a execução, a mensagem de confirmação indicará o total de registros gerados e o arquivo `dados_16p.csv` estará disponível no mesmo diretório.

---

## 🎛️ Customização

Você pode ajustar a quantidade de jogadores e giros alterando os parâmetros da função `gerar_dados_projeto`:

```python
# Exemplo: Simular 100 jogadores fazendo 200 giros cada
gerar_dados_projeto(num_jogadores=100, giros_por_jogador=200)
```
