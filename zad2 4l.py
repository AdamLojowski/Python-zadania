"""Skrypt symuluje błądzenie pojedynczego agenta na macierzy 10 na 10
i zapisuje go w postaci gifa"""

from matplotlib import pyplot as plt
import numpy as np
import random
from PIL import Image
import os
import imageio
import argparse

parser = argparse.ArgumentParser(description = "Skrypt symuluje błądzenie pojedynczego agenta na macierzy 10 na 10")
parser.add_argument('-f', '--frames', help = "Ilość klatek",
                    type = int, default = 1, required = False)
parser.add_argument('-n', '--length', help = "Długość gifu",
                    type = int, default = 20, required = False)

args = parser.parse_args()
print("Wybrana ilość klatek to: ", args.frames)
print("Ilość kroków agenta: ", args.length)
                         

path = 'C:\\Users\\lojow\\Desktop\\programowanie\\matrix_plots\\'
file_names = []
Matrix = np.zeros((10,10))
x = random.randint(0,9)
y = random.randint(0,9)
print("Agent rozpoczyna bieg")

for i in range(args.length):
      Matrix[x,y] += 10
      fig, ax = plt.subplots()
      ax.axes.xaxis.set_visible(False)
      ax.axes.yaxis.set_visible(False)
      im = ax.imshow(Matrix)
      for frame in range(args.frames):
            fig.savefig(path+"{}{}".format(i,frame))
            file_names.append(path+"{}{}.png".format(i,frame))
            
      Matrix[x,y] -= 9
      plt.close()
      
      x += random.randint(-1,1)
      y += random.randint(-1,1)
      if x > 9:
            x = 0
      elif x < 1:
            x = 9
      if y > 9:
            y = 0
      elif y < 1:
            y = 9

print("Tworzenie Gif'a")
with imageio.get_writer('matrix_agent.gif', mode = 'I') as writer:
      for file in file_names:
            image = imageio.imread(file)
            writer.append_data(image)
            
print("Usówanie zbędnych pngków")
for image in set(file_names):
      os.remove(image)


      

