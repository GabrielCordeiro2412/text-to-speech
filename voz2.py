from gtts import gTTS
import os
from pygame import mixer

diretorio = input("Digite o local do arquivo, exemplo: C:/algo.txt: ")
teste = os.path.isfile(diretorio)

if teste:
    print("Carregando arquivo, aguarde...")
    with open(diretorio) as file_data:
        arquivo = file_data.read()
        print("Arquivo carregado")
        print("Efetuando a leitura, aguarde")
        voz = gTTS(arquivo, lang='pt')
        voz.save("C:/Users/logonrmlocal/Downloads/voz.mp3")
        print("Falando...")
        os.system("C:/Users/logonrmlocal/Downloads/voz.mp3")
else:
    print("Diretório não encontrado")