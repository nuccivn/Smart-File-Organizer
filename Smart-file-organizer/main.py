import os
import shutil

# Tipos de arquivos
EXTENSOES = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "pdf": [".pdf"],
    "excel": [".xlsx", ".xls", ".csv"],
    "documentos": [".docx", ".txt"],
    "outros": []
}

def organizar_arquivos(pasta, simular=False):
    log = []

    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)

        if os.path.isfile(caminho_arquivo):
            nome, extensao = os.path.splitext(arquivo)

            destino = "outros"
            for pasta_tipo, extensoes in EXTENSOES.items():
                if extensao.lower() in extensoes:
                    destino = pasta_tipo
                    break

            pasta_destino = os.path.join(pasta, destino)

            if not os.path.exists(pasta_destino):
                if not simular:
                    os.makedirs(pasta_destino)

            novo_caminho = os.path.join(pasta_destino, arquivo)

            if simular:
                print(f"[SIMULAÇÃO] {arquivo} → {destino}/")
            else:
                shutil.move(caminho_arquivo, novo_caminho)
                log.append(f"Movido: {arquivo} → {destino}/")

    if not simular:
        with open("log.txt", "w") as f:
            for linha in log:
                f.write(linha + "\n")

        print("\n✔ Organização concluída! Log salvo em log.txt")


def menu():
    print("=== SMART FILE ORGANIZER ===")
    print("1 - Organizar arquivos")
    print("2 - Simular organização")

    opcao = input("Escolha uma opção: ")
    pasta = input("Digite o caminho da pasta: ")

    if not os.path.exists(pasta):
        print("❌ Pasta não encontrada!")
        return

    if opcao == "1":
        organizar_arquivos(pasta, simular=False)
    elif opcao == "2":
        organizar_arquivos(pasta, simular=True)
    else:
        print("❌ Opção inválida!")


if __name__ == "__main__":
    menu()