import time
import webbrowser
import pyautogui

pyautogui.PAUSE = 1.0

LINK_FORMULARIO = "https://docs.google.com/forms/d/e/1FAIpQLSfkt0hNT9aGEmle8wGxc8kWakMCh2JCQ6lLKhRPGo6YgPCtaA/viewform?usp=preview"

def calcular_notas(tf1, tf2):
    nota1 = tf1 * 0.8
    nota2 = tf2 * 0.8
    return round(nota1, 2), round(nota2, 2)

def automatizar_preenchimento(dados_alunos):
    print("Abrindo o formulário no navegador...")
    webbrowser.open(LINK_FORMULARIO)
    
    print("Aguardando 9 segundos para a página carregar e você focar no primeiro campo...")
    time.sleep(6)  

    for aluno in dados_alunos:
        n1, n2 = calcular_notas(aluno['tf1'], aluno['tf2'])

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

    print("Automação concluída!")

alunos_para_lancar = [
    {"ra": "123456", "nome": "João Silva", "tf1": 10.0, "tf2": 9.0},
    {"ra": "654321", "nome": "Maria Souza", "tf1": 8.5, "tf2": 9.5},
]

if __name__ == "__main__":
    automatizar_preenchimento(alunos_para_lancar)