import sys


"""
      Ten program zmienia znak końca znaku z Unixowego na Windowsowy i odwrotnie
      @param1:str pełna nazwa pliku tekstowego
"""
file_name = sys.argv[1]
line_list = []

if file_name.split(".")[1] == "txt":
      text = open(file_name, "rb")
      text_lines = text.readlines()
      text.close()
      print(text_lines)
else:
      print("Wrong file extanction")
      raise ValueError

if len(sys.argv) > 2:
      print("Too many args!")
      raise ValueError

for line in text_lines:
      
      if line[-2:] == b'\r\n':
            line = line[:-2] + b'\n'
            
      elif line[-1:] == b'\n':
            line = line[:-1]
            line += b'\r\n' 
                  
      else:
            pass
      line_list.append(line)

text.close()

write_text = open(file_name, "wb")
for i in range(len(line_list)):
      write_text.write(line_list[i])
write_text.close()

#python "zad4 l3.py" tekst2.txt



