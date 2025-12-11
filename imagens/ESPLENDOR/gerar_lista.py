import os

def gerar_lista_nomes(caminho_da_pasta='.', nome_arquivo_saida='nomes_atuais.txt'):
    """
    Lê todos os nomes de arquivos de imagem em uma pasta e salva em um arquivo de texto.
    """
    try:
        # Lista todos os itens na pasta
        nomes_atuais = os.listdir(caminho_da_pasta)

        # Filtra apenas arquivos (ignora subpastas) e apenas arquivos de imagem comuns
        nomes_de_arquivos = [
            f for f in nomes_atuais 
            if os.path.isfile(os.path.join(caminho_da_pasta, f)) and 
               f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))
        ]

        # Salva a lista em um arquivo de texto
        with open(nome_arquivo_saida, 'w', encoding='utf-8') as f:
            for nome in nomes_de_arquivos:
                f.write(f"{nome}\n")

        print(f"Arquivo '{nome_arquivo_saida}' gerado com sucesso!")
        print(f"Total de arquivos encontrados: {len(nomes_de_arquivos)}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Para rodar, salve este código como 'gerar_lista.py' e execute no terminal:
# python gerar_lista.py
if __name__ == "__main__":
    # O '.' significa a pasta atual onde o script está sendo executado
    gerar_lista_nomes()