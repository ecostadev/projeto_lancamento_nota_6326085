import time
import webbrowser
import pyautogui

pyautogui.PAUSE = 1.0

LINK_FORMULARIO = "https://docs.google.com/forms/d/e/1FAIpQLSfkt0hNT9aGEmle8wGxc8kWakMCh2JCQ6lLKhRPGo6YgPCtaA/viewform?usp=preview"

def calcular_notas_ponderadas(tf1, tf2):
    # Aplicação dos pesos solicitados: Nota final com peso 8 e TF com peso 2
    # Exemplo de cálculo ponderado: (Nota_base * 0.8) + (TF * 0.2)
    # Ajustando para calcular a Nota 1 e Nota 2 baseadas nos TFs informados:
    
    nota1 = (tf1 * 0.8) + (tf1 * 0.2)  # Equivalente à nota ponderada
    nota2 = (tf2 * 0.8) + (tf2 * 0.2)
    
    # Média para verificar a aprovação (considerando média >= 6.0)
    media = (nota1 + nota2) / 2
    status = "Aprovado" if media >= 6.0 else "Reprovado"
    
    return round(nota1, 2), round(nota2, 2), status

def automatizar_preenchimento(dados_alunos):
    print("Abrindo o formulário no navegador...")
    webbrowser.open(LINK_FORMULARIO)
    
    print("Aguardando 9 segundos para a página carregar e você focar no primeiro campo...")
    time.sleep(9)  

    for aluno in dados_alunos:
        n1, n2, status = calcular_notas_ponderadas(aluno['tf1'], aluno['tf2'])

        pyautogui.write(str(aluno['ra']), interval=0.05)
        pyautogui.press('tab')
        
        pyautogui.write(aluno['nome'], interval=0.05)
        pyautogui.press('tab')
        
        pyautogui.write(str(n1), interval=0.05)
        pyautogui.press('tab')
        
        pyautogui.write(str(n2), interval=0.05)
        pyautogui.press('tab')
        
        pyautogui.write(str(aluno['tf1']), interval=0.05)
        pyautogui.press('tab')
        
        pyautogui.write(str(aluno['tf2']), interval=0.05)
        pyautogui.press('tab')
        
        pyautogui.press('enter')
        
        time.sleep(4)
        
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(3)

        print(f"Aluno: {aluno['nome']} | Nota 1: {n1} | Nota 2: {n2} | Status: {status}")

    print("Automação concluída!")

alunos_para_lancar = [
    {"ra": "6326085", "nome": "Emanuela Oliveira da Costa", "tf1": 10.0, "tf2": 9.0},
    {"ra": "123456", "nome": "João Silva", "tf1": 8.5, "tf2": 9.5},
]

if __name__ == "__main__":
    automatizar_preenchimento(alunos_para_lancar)