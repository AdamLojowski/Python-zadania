"""szuka plików o zadanych rozszerzeniach w pewnych katalogach i tworzy kopie zapasowe tych zmodyfikowanych w ostatnich trzech dniach do
katalogu Backup/copy-X (lub Backup\copy-X pod Windows), gdzie X to
aktualna data."""

import sys
import os
from shutil import copy
import time
from datetime import date
path = "\\Users\\lojow\\Desktop\\"


            
def copy_types(dir_list:list, type_list:list):
      
      DAY_TIME = 24*60*60
      dir_name = "Backup-copy-{}".format(date.today())
      os.mkdir(path+dir_name)
      dir_paths = []
      for d in range(len(dir_list)):
            print("pierwsza część")
            dir_paths.append(os.path.abspath(dir_list[d]))
                             
      for i in range(len(dir_list)):
            print("druga")
            for root, dirs, files in os.walk(dir_list[i]):
                  print("trzecia")
                  for file_name in files:
                        print("czwarta")
                        if is_type(type_list, file_name):
                              print("piąta")
                              file_time = os.path.getmtime(str(os.path.join(root,file_name)))
                              time_date = time.ctime(file_time)
                              if file_time > DAY_TIME:
                                    #tutaj coś wyjebuje podczas przenoszenia 
                                    copy(file_name, path+dir_name)
                                    print("File {} has been moved to {}".format(file_name, dir_name))

def is_type(type_list:list, file_name):
      expansion = file_name.split(sep = ".")
      for j in range(len(type_list)):
            if expansion[1] == type_list[j]:
                  return True
            
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


      """
      Program tworzy kopie zapasowe plików o wybranym rozszerzeniu z jednego, bądź więcej folderów.
      @param[1:-2]:str folderów, w których szukamy plików
      @param[:-1]:str typ rozszerzenia, którego wyszukujemy
      """
                                    
DAY_TIME = 24*60*60
dir_name = "Backup-copy-{}".format(date.today())
os.mkdir(path + dir_name)
dir_paths = []
type_list = [sys.argv[-1]]
file_number = 0

for i in range(1,len(sys.argv)):
      try:
            dir_paths.append(os.path.abspath(sys.argv[i]))
      except:
            print("ale takiego folderu nie ma :C")
            raise ValueError

for j in range(len(dir_paths)):
      for root, dirs, files in os.walk(dir_paths[j]):
            for file_name in files:
                  if is_type(type_list, file_name):
                        file_time = os.path.getmtime(str(os.path.join(root,file_name)))
                        time_date = time.ctime(file_time)
                        file_number += 1

                        if file_time > DAY_TIME:
                              copy(find_file(file_name), dir_name)
                              print("File {} has been moved to {}".format(file_name, dir_name))
if file_number == 0:
      print("No files found!")

#python "zad 3.py" Folderowiec2 txt
                       
      
                        
            
