from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Oculta a janela principal
Tk().withdraw()

caminho_arquivo = askopenfilename(
    title="Selecione um arquivo",
    filetypes=[
        ("Todos os arquivos", "*.*"),
        ("Arquivos de texto", "*.txt"),
        ("Python", "*.py"),
        ("PDF", "*.pdf"),
    ]
)

print(caminho_arquivo)