import os

def boas_vindas():
    print()
    print("================================")
    print("  Organizable Paste Version 1.0  ")
    print("  Organizador automatico de arquivos  ")
    print("             By GodZinn   ")
    print("================================")
    print()

def carregar_categorias():
    categorias = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv"],
        "Musicas": [".mp3", ".wav", ".aac", ".flac"],
        "Arquivos Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".html", ".css", ".sh"],
        "Outros": []
    }
    return categorias

def listar_arquivos(diretorio):
    arquivos = []
    for item in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, item)
        if os.path.isfile(caminho_completo):
            arquivos.append(item)
    return arquivos

def identificar_categoria(arquivo, categorias):
    _, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()
    for categoria, lista_extensoes in categorias.items():
        if extensao in lista_extensoes:
            return categoria  
    return "Outros"

def organizar_arquivos(pasta, arquivos, categorias):
    for arquivo in arquivos:
        categoria = identificar_categoria(arquivo, categorias)
        caminho_origem = os.path.join(pasta, arquivo)
        caminho_destino_pasta = os.path.join(pasta, categoria)
        caminho_destino_arquivo = os.path.join(caminho_destino_pasta, arquivo)


        if not os.path.exists(caminho_destino_pasta):
            os.makedirs(caminho_destino_pasta)


        os.rename(caminho_origem, caminho_destino_arquivo)


        print(f"'{arquivo}' foi movido para '{categoria}'")


pasta_alvo = "C:\\Users\\Seu Usuario\\Downloads" # COLOQUE O CAMINHO PARA A PASTA DOWNLOAD AQUI

categorias = carregar_categorias()
print("Categorias carregadas com sucesso.")
print(categorias)

arquivos = listar_arquivos(pasta_alvo)
print("\nArquivos na pasta de downloads:")
print(arquivos)

boas_vindas()

print("\nVerificando categorias de cada arquivo:")
for arquivo in arquivos:
    categoria = identificar_categoria(arquivo, categorias)
    print(f"{arquivo} → {categoria}")

print("\nOrganizando arquivos...")
organizar_arquivos(pasta_alvo, arquivos, categorias)

print("\nTodos os arquivos foram organizados com sucesso!")
