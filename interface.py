
import PySimpleGUI as sg
from skimage import io, filters, data
import matplotlib.pyplot as plt
import pydicom
import numpy as np
from PIL import Image


class TelaPython:
    """ Class responsible for creating the main window """

    def __init__(self):
        self.layout = [
            [
                sg.Button('Carregar Imagem', size=(22, 0), key="-IMGL-"),
                sg.Input(size=(22, 0)), sg.FileBrowse()
            ],
            [
                sg.Button('Calcular números CT médios', size=(22, 0)),
                sg.Input(size=(15, 0))
            ],
            [
                sg.Button('Exibir Dados'),
            ]
        ]

    # def __str__(self):
    #     return f"Value: \n{self.values} \n Buttons:\n{self.button}"

    def WindowRoutine(self):

        janela = sg.Window("Resolução de baixo contraste").layout(self.layout)
        self.button, self.values = janela.Read()

        if(self.button == "-IMGL-"):
            return {
                'message': "filePath",
                'content': str(self.values[0])
            }

        elif(self.button == "Calcular números CT médios"):
            return {
                'message': "",
                'content': ""
            }

        elif(self.button == "Exibir dados"):
            return {
                'message': "Dados",
                'content': self.__str__()
            }

        else:
            return {
                'message': "",
                'content': ""
            }


tela = TelaPython()
dicionario = tela.WindowRoutine()
print(str(dicionario))

# img1 = pydicom . read_file(filePath)

# l_bytes = img1.PixelData
# img1.pixel_array
# p = img1.pixel_array
# matplotlib.rcParams['font.size'] = 18
# fig, axes = plt.subplots(1, 2, figsize=(8, 4))
# ax = axes.ravel()


# ax[0].imshow(p)
# ax[1].imshow(edges)
# for i in range(len(edges)):
#     print(edges[i])
# fig.tight_layout()
# plt.show()
# print(p)
