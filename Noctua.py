import keyboard
import sys 

def bloquear_teclas(teclas):
    for tecla in teclas:
        keyboard.block_key(tecla)

# Lista de teclas a serem bloqueadas
teclas_a_bloquear = ['a', 'alt', 'del']  # Adicione aqui as teclas que deseja bloquear

# Bloqueando as teclas
bloquear_teclas(teclas_a_bloquear)

# Manter o programa executando
print("Teclas bloqueadas. Pressione ESC para sair.")
keyboard.wait('esc')  # Espera até que a tecla ESC seja pressionada

import psutil
import time

# Lista de nomes de aplicativos a serem bloqueados
bloqueados = ["Steam.exe", "steamwebhelper.exe", "steamwebhelper"]

while True:
    # Itera sobre os processos em execução
    for proc in psutil.process_iter(['pid', 'name']):
        # Verifica se o processo está na lista de bloqueados
        if proc.info['name'] in bloqueados:
            print(f"Encerrando {proc.info['name']} (PID: {proc.info['pid']})")
            proc.terminate()  # Tenta encerrar o processo
    
    # Espera um pouco antes de verificar novamente
    time.sleep(5)