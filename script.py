# Importação o módulo 'os' para interagir com o sistema operacional.
import os

# Define uma variável de ambiente para ocultar a mensagem de boas-vindas do Pygame.
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# Importa a biblioteca Pygame.
import pygame

# --- Função principal para reprodução e controle da música ---
def play_music(folder, song_name):

    file_path = os.path.join(folder, song_name)

    # Verifica se o arquivo realmente existe no caminho especificado.
    if not os.path.exists(file_path):
        print("Arquivo não encontrado")
        return
    
    # Carrega o arquivo de áudio no mixer do Pygame.
    pygame.mixer.music.load(file_path)

    # Inicia a reprodução da música.
    pygame.mixer.music.play()

    print(f"\nTocando: {song_name}")
    print("Comandos: [P]ausar, [R]esumir, [F]inalizar")

    while True:

        command = input("> ").upper()
        if command == "P":
            pygame.mixer.music.pause()
            print("Pausado")
        elif command == "R":
            pygame.mixer.music.unpause()
            print("Resumido")
        elif command == "f":
            pygame.mixer.music.stop()
            print("Finalizado")
            return
        else:
            print("Comando Inválido!")

# --- Função principal do programa ---
def main():
    try:
        # Inicializa o módulo de áudio (mixer) do Pygame.
        pygame.mixer.init()
    except pygame.error as e:
        # Imprime um erro se a inicialização do áudio falhar
        print("Inicialização de Áudio falhada! ", e)

    # Define o nome da pasta que contém os arquivos de música.
    folder = "music"

    # Verifica se a pasta 'music' existe no diretório atual.
    if not os.path.isdir(folder):
        print(f"Pasta '{folder}' não encontrada")
        return
    
    # Lista todos os arquivos na pasta 'music' e filtra apenas aqueles que terminam com ".mp3".
    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]

    # Linha de debug/informação: imprime a lista de arquivos encontrados.
    print(mp3_files)

    # Verifica se a lista de MP3s está vazia.
    if not mp3_files:
        print("Arquivos mp3 não encontrados!")

    # Loop principal para exibir o menu e gerenciar a seleção de músicas.
    while True:
        print("********* MP3 PLAYER *********")
        print("Minha lista de música:")

        # Itera sobre a lista de músicas, exibindo um índice numerado (começando em 1).
        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")
        
        # Solicitar ao usuário a escolha da música ou a opção de sair.
        choice_input = input("\nColoque o número do som para tocar (ou aperte 'Q' para sair): ")

        # Verifica se o usuário deseja sair do programa.
        if choice_input.upper() == "Q":
            print("Tchau!")
            break

        # Verifica se a entrada do usuário é um número.
        if not choice_input.isdigit():
            print("Coloque um número válido")
            # Volta ao início do loop.
            continue

        # Converte a entrada (baseada em 1) para um índice de lista (baseado em 0).
        choice = int(choice_input) -1

        if 0 <= choice < len(mp3_files):
            # Chama a função para reproduzir a música selecionada.
            play_music(folder, mp3_files[choice])
        else:
            # Trata a escolha de um número fora do intervalo válido.
            print("Escolha inválida")

# Bloco de execução principal.
if __name__ == "__main__":
    main()