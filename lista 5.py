import requests
import os.path
import sys
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def download_data():
      """Ta funkcja pobiera dane walutowe z API NBP, po czym obrabia je w taki sposób, by móc odczytać z nich 
         kody oraz wartości poszczególnych walut. W przypadku braku połączenia internetowego korzysta z danych
         zapisanych w kopii zapasowej w pliku txt. 
         @return cur_list / cleared_copy:dict, są to słowniki zawierające dane walutowe
         cur_list - aktualne dane
         cleared_copy - dane pobrane z kopii zapasowej"""

      try:
            path = "C://Users//lojow//Desktop//programowanie//kalkulator//currency_copy.txt"
            url = "http://api.nbp.pl/api/exchangerates/tables/C/"
            r = requests.get(url)
            json_data = r.json()
            cleared = json_data[0]
            cur_list = cleared['rates']
            
            sec_copy(cleared['rates'])
            return cur_list

      except:
            copy_path = "C://Users//lojow//Desktop//programowanie//kalkulator//currency_copy.txt"
            open_text = open(path, "r")
            cur_copy = open_text.read()
            cleared_copy = eval(cur_copy)
            open_text.close()
            
            return cleared_copy

"""W tej części pobieram oczyszczone dane z funkcji download_data i tworzę listy:
    value_list oraz code_list. Przechowują one kolejno - wartości walut oraz ich kody"""
cur_list = download_data()
code_list = ['PLN']
value_list = [1.0]

n = len(cur_list)
for i in range(n):
      code_list.append(cur_list[i]['code'])
      value_list.append(cur_list[i]['ask'])


def przelicznik(ofered, wanted):
      """Ta funkcja dzieli nam pierwszą zmienną przez drugą oraz zaokrągla ją do trzeciego miejsca po przecinku
         @param1 ofered:float/int
         @param2 wanted:float/int
         @return float, zwraca nam zaokrąglony wynik dzielenia"""

      answer = round(ofered/wanted, 2)
      return  answer

def sec_copy(copy):
      """ Ta funkcja tworzy w pliku txt kopię zapasową danych pobieranych z API NBP, jeśli po wywołaniu GUI plik, w którym zapisano dane
         nie był modyfikowany od ostatniego dnia.
         @param1 copy:any, parametr, który chcemy zapisać w pliku tekstowym  """
      
      path = "C://Users//lojow//Desktop//programowanie//kalkulator//currency_copy.txt"
      DAY_TIME = 60*60*24
      if os.path.getmtime(path) > DAY_TIME:
            write_text = open(path, "w")
            write_text.write(str(copy))
            write_text.close()


def calculate():
      """Jest to funkcja przypisana do przycisku "Calculate". Po jej wciśnięciu sprawdza, czy w oknie "Entry_value" została
         wpisana odpowiednia wartość, w przeciwnym wypadku generuje błąd. Naprawia błąd polegający, na wpisaniu 
         w okno liczbę oddzieloną ','. Jeśli wszystko się zgadza, wpisuje w pole tekstowe Value_text odpowiednią wartość
         wyliczoną za pomocą pomocniczej funkcji "przelicznik", po czym dopisuje dodatkowo kod pożądanej waluty"""
      global first_currency
      global second_currency
      entry_value = Entry_field.get()
      check_if_choosen()
      try:
            if "," in entry_value:
                  splited = entry_value.split(",")
                  corected = splited[0]+"."+splited[1]
                  value = float(corected)
            else:
                  value = float(entry_value)
            result = round(value * przelicznik(first_currency,second_currency),7)

            Value_text.config(state = NORMAL)
            Value_text.delete('1.0',END)
            Value_text.insert(END,str(result)+" "+second_cur_code)
            Value_text.config(state = DISABLED)

      except ValueError:
            if len(Entry_field.get()) == 0:
                  Entry_field.insert(0, str(0.0))
                  Value_text.config(state = NORMAL)
                  Value_text.delete('1.0',END)
                  Value_text.insert(END,str(0.0))
                  Value_text.config(state = DISABLED)
            else:
                  Entry_field.delete(0, END)
                  messagebox.showwarning(title="Wpisana zła wartość", 
                  message = "Proszę wpisać liczbę!")
            
def kill():
      """Ta funkcja jest częścią przycisku "Kill". Po jego wciśnięciu zamyka okno GUI """
      root.destroy()

def check_if_choosen():
      """Ta funkcja sprawdza, czy użytkownik zaznaczył waluty w comboboxach currency oraz wanted_currency.
         W przeciwnym wypadku wyrzuca na ekran błąd. 
      """
      if wanted_currency.current() == -1:
            messagebox.showinfo(title = "Nie wybrano waluty",
            message = "Proszę wybrać pożądaną walutę")
      elif currency.current() == -1:
            messagebox.showinfo(title = "Nie wybrano waluty",
            message = "Proszę wybrać posiadaną walutę")
      
def get_cur(event):
      """Ta funkcja tworzy globalną zmienną, która jest uzależniona od wybranej wartości w comboboxie currency:
         first_currency: float, jest to wartość liczbowa aktualnie zaznaczonego comboboxa currency"""

      global currency
      global first_currency 

      first_index  = currency.current()
      first_currency = float(value_list[first_index])
def wan_cur(event):

      """Ta funkcja tworzy dwie globalne zmienne, które są uzależnione od wybranej wartości w comboboxie wanted_currency:
         second_cur_code: str, jest to kod waluty aktualnie zaznaczonego comboboxa wanted_currency
         second_currency: float, jest to wartość liczbowa aktualnie zaznaczonego comboboxa wanted_currency"""
      global wanted_currency
      global second_currency
      global second_cur_code
            
      second_index = wanted_currency.current()
      second_cur_code = code_list[second_index]
      second_currency = float(value_list[second_index])

#Początek GUI
root = Tk()

#Tworzenie pól do wyświetlania wartości
Entry_field = Entry(root, bg = "light yellow")
Value_text = Text(root, height = 1, width = 10, bg = "light yellow", state = DISABLED)

#Przyciski
Calculate = Button(root, text = " = ", command = calculate, width = 3 )
Kill = Button(root, text = " X ", command= kill, bg = "red", fg = "white", width = 3)

#Labele
your_currency = Label(root, text = "Mam", bd = 3)
you_want = Label(root, text = "Chcę", bd = 3)
your_currenty_amount = Label(root, text = "Moja Kwota", bd = 2)
you_will_get = Label(root, text = "Dostanę", bd = 2)

#Comboboxy
selected_cur = StringVar()
wanted_cur = StringVar()

currency = ttk.Combobox(root, textvariable =  selected_cur)
currency['values'] = code_list
currency['state'] = 'readonly'

currency.bind('<<ComboboxSelected>>', get_cur)

wanted_currency = ttk.Combobox(root, textvariable =  wanted_cur)
wanted_currency['values'] = code_list
wanted_currency['state'] = 'readonly'
wanted_currency.bind('<<ComboboxSelected>>', wan_cur)

#Gridowanie 

#Grid Button
Calculate.grid(row = 2, column = 3, columnspan = 3)
Kill.grid(row = 0, column = 3, columnspan = 2, sticky = E )

#Grid Label
your_currency.grid(row = 3, column = 1, columnspan = 2)
you_want.grid(row = 3, column = 3, columnspan = 3)

your_currenty_amount.grid(row = 1, column = 0, columnspan = 3)
you_will_get.grid(row = 1, column = 1, columnspan = 3)

#Grid Entry and Text
Entry_field.grid(row = 2, column= 0, columnspan=3, padx = 15, pady = 5)
Value_text.grid(row = 2, column =1, columnspan =3, padx = 10, pady = 5)

#Grid Combobox
currency.grid(row = 4, column = 2)
wanted_currency.grid(row = 4, column = 3)

#Tytuł, kolor tła i geometria GUI 
root.title("Kalkulator walutowy")
root.configure(background = "light grey")
root.minsize(300,300)
root.maxsize(300,300)
root.mainloop()