
import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Button('Carregar imagem',size=(22,0)),sg.Input(size=(15,0))],
            [sg.Button('Calcular números CT médios',size=(22,0)),sg.Input(size=(15,0))],
            [sg.Button('Exibir dados')]
        ]
        # janela
        janela = sg.Window("Resolução de baixo contraste").layout(layout)
        # Extrair os dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)
        

tela = TelaPython()
tela.Iniciar()

from skimage import io, filters, data
import matplotlib.pyplot as plt
import pydicom
import numpy as np
import numpy
from PIL import Image

img1  =  pydicom . read_file ("C:/IC Rômulo José/IC 2018 2019/Principais arquivos ic 2018 - 2019/Material sobre filtros/Filtros Aptos/60598011")
l_bytes = img1.PixelData
img1.pixel_array
p = img1.pixel_array
import matplotlib
matplotlib.rcParams['font.size'] = 18
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()


ax[0].imshow(p)
ax[1].imshow(edges)
for i in range(len(edges)):print(edges[i])
fig.tight_layout()
plt.show()
print(p)