import random
import pandas as pd

def gerar_dados_projeto(num_jogadores=50, giros_por_jogador=100):
    # Parâmetros do Caça-Níquel
    chance_vitoria = 0.16
    multiplicador = 5.0
    valor_aposta = 10
    saldo_inicial = 500

    dados_totais = []

    for id_jog in range(1, num_jogadores + 1):
        nome_jogador = f"Jogador_{id_jog:02d}"
        saldo_atual = saldo_inicial
        
        for num_giro in range(1, giros_por_jogador + 1):
            saldo_antes = saldo_atual
            saldo_atual -= valor_aposta
            
            # Algoritmo de Monte Carlo
            sorteio = random.random()
            if sorteio < chance_vitoria:
                ganho = valor_aposta * multiplicador
                resultado = "Vitoria"
            else:
                ganho = 0
                resultado = "Derrota"
                
            saldo_atual += ganho
            lucro_prejuizo_giro = ganho - valor_aposta
            
            if saldo_antes < valor_aposta:
                break
                
            # Guarda a linha de informação
            dados_totais.append({
                "ID_Jogador": nome_jogador,
                "Numero_Giro": num_giro,
                "Valor_Apostado": valor_aposta,
                "Resultado": resultado,
                "Valor_Ganho": ganho,
                "Resultado_Financeiro_Giro": lucro_prejuizo_giro,
                "Saldo_Acumulado": saldo_atual
            })

    # Transforma em DataFrame e exporta para CSV
    df = pd.DataFrame(dados_totais)
    df.to_csv("dados_16p.csv", index=False, sep=";")
    print(f"Sucesso! Base de dados gerada com {len(df)} linhas.")

# Executa para gerar o arquivo
gerar_dados_projeto()