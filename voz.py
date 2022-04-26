import os
from gtts import gTTS
from pygame import mixer

voz = gTTS("Olá mundo!", lang='pt')
voz.save("C:/Users/logonrmlocal/Downloads/voz.mp3");
os.system("C:/Users/logonrmlocal/Downloads/voz.mp3")
fim = input("Digite algo para finalizar: ")