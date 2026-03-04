import sys
sys.dont_write_bytecode = True

from .Arquivo import Arquivo
import shutil
from pathlib import Path
import os


class Organizar:
    
    extensoes_imagem = ["jpg", "jpeg", "png", "gif", "webp", "bmp", "svg", "raw"]
    extensoes_texto = ["txt", "doc", "docx", "pdf", "rtf", "odt", "tex", "md", "pages"]
    extensoes_comprimidos = ["zip", "rar", "7z", "tar", "gz", "bz2", "xz", "iso", "z"]
    extensoes_video = ["mp4", "mkv", "avi", "mov", "wmv", "flv", "webm", "m4v", "mpg", "mpeg"]
    extensoes_audio = ["mp3", "wav", "flac", "aac", "ogg", "wma", "m4a", "aiff", "opus", "alac"]

    def __init__(self):
        env_destino = os.getenv("Destino")
        env_downloads = os.getenv("Downloads")

        self.destino = Path(env_destino) if env_destino else None
        self.downloads = Path(env_downloads) if env_downloads else None

    def Organizar_downloads(self):
        if (self.destino != None) and (self.downloads != None):

            os.chdir(self.downloads)
            conteudo = os.listdir()

            for i in conteudo:
                pasta = ""
                arquivo = Arquivo(i)
                # os.chdir(self.destino)
                Origin_path = self.downloads / arquivo.getNome()
                if(os.path.isdir(Path(self.downloads)/arquivo.getNome()) == False):
                    pastas = os.listdir()
                    if (arquivo.getExtensao() in self.extensoes_imagem):  
                        # os.makedirs("Imagens", exist_ok=True)
                        pasta = "Imagens"

                    elif (arquivo.getExtensao() in self.extensoes_texto):

                        os.makedirs("Textos", exist_ok=True)                 

                        pasta = "Textos"

                    elif (arquivo.getExtensao() in self.extensoes_comprimidos):

                        pasta = "Comprimidos"

                    elif (arquivo.getExtensao() in self.extensoes_video):

                        pasta =  "Videos"

                    elif (arquivo.getExtensao() in self.extensoes_audio):

                        pasta = "Audios"
                    else:

                        pasta = rf"{arquivo.getExtensao()}"
                    
                    caminho = Path(self.destino)/pasta/arquivo.getNome()
                    print(caminho)
                    if(arquivo.getNome not in os.listdir()):
                        shutil.move(str(Path(Origin_path),str(caminho)))
                        print(f"{arquivo.getNome()} movido com sucesso!")
                    else:
                        print(f"O arquivo: {arquivo.getNome()} já existe na pasta correspondente!")

        else:
            print("\033[1;31m Variáveis de ambiente não configuradas corretamente! Certifique-se que as variáveis 'Destino' e 'Downloads' existem! \033[0m")