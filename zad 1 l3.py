import sys
import os
from shutil import copy
path = "\\Users\\lojow\\Desktop\\"

def find_file(name,path = "C:"):
      """
      Ta funkcja wyszukuje ścieżki danego pliku zadanego nazwą z rozszerzeniem
      @param1 name:str nazwa pliku
      @param2 path:str nazwa dysku, w którym szukamy
      @return:str wypluwa ścieżkę do danego pliku
      """
      
      for root, dir, files in os.walk(path):
            if name in files:
                  return os.path.join(root,name)
            
def pack_files(list_of_files, dir_name: str):
      """
      Ta funkcja tworzy folder o nazwe dir_name i kopiuje do niego pliki z listy list_of_files
      @param1 list_of_files:list of strings
      @param2 dir_name:str name of new folder
      """
      list_of_files = sys.argv[1]
      dir_name = sys.argv[2]
      os.mkdir(path+dir_name)
      destination = path + dir_name
      
      for i in range(len(list_of_files)):
            file_name = "\\copy_{}".format(list_of_files[i])
            if os.path.isfile(path+list_of_files[i]) == False:
                  print('WARNING\nFile {} is no more :C'.format(list_of_files[i]))
            else:    
                  copy(find_file(list_of_files[i]), destination + file_name)
                  print('File {} was copied successfully'.format(list_of_files[i]))
      

#pack_files(['tekst1.txt','tekst2.txt','tekst3.txt'],'Folderowiec')

def find_file(name,path = "C:"):
      """
      Ta funkcja wyszukuje ścieżki danego pliku zadanego nazwą z rozszerzeniem
      @param1 name:str nazwa pliku
      @param2 path:str nazwa dysku, w którym szukamy
      @return:str wypluwa ścieżkę do danego pliku
      """
      
      for root, dir, files in os.walk(path):
            if name in files:
                  return os.path.join(root,name)


#python "zad 1 l3.py" tekst1.txt tekst2.txt tekst3.txt Folderowiec300
"""
Ten program kopiuje wybrane pliki do specjalnego folderu na kopie
w cmd przyjmuje minimum 2 argumenty
@param[1:-2]: str Nazwy plików z rozszerzeniami
@param[:-1]: str nazwa folderu, który utworzymy
""" 
if os.path.isdir(path+sys.argv[-1]):
      print("Dir named like that already exist :C")
      raise ValueError
if len(sys.argv)< 2:
      print("This program must get minumum 2 args!")
      raise ValueError

dir_name = str(sys.argv[-1])
os.mkdir(path+dir_name)
destination = path + dir_name

for i in range(1, len(sys.argv)-1):
      file_name = "\\copy_{}".format(sys.argv[i])
      if os.path.isfile(path+sys.argv[i]) == False:
            print('WARNING\nFile {} is no more :C'.format(sys.argv[i]))
      else:
            copy(find_file(sys.argv[i]), destination + file_name)
            print('File {} was copied successfully'.format(sys.argv[i]))
