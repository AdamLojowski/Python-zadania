"""To jest moduł w który tworzy aplikację GUI, w której możemy rozrysować wykresy podstawowych funkcji. Użytkownik sam wpisuje zakres funkcji oraz jej wzór. Należy zapoznać się z instrukcją zawartą w prawym dolnym rogu okna aplikacji."""

from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, pi, log, sqrt, power
from numpy import testing


def get_function():
    """ Stwórz wykres funkcji korzystając z danych z wszystkich pól tekstowych

    Funkcja przypisana do przycisku Draw_button.
    Funckja nie przyjmuje żadnych argumentów.
    Funkcja pobiera dane z pól tekstowych [Entry_field, X_min, X_max, Title_graph, Y_name, X_name].
    Wykres jest generowany za pomocą pakietu matplotlib.pyplot oraz numpy
    Wartość globalnej zmiennej n definiuje, czy ma zostać wyświetlona legenda wykresu.
    """
    global n
    x_range_min()
    x_range_max()

    if X_min.get() == "Zły zakres" or X_max.get() == "Zły zakres":
        return
    
    
    try:
        
        func = Entry_field.get()
        list_func = func.split(';')
        x = np.arange(x_min, x_max, 0.2)
        ax1 = fig.add_subplot()
        ax1.cla()
        ax1.set_title(Title_graph.get())
        ax1.set_ylabel(Y_name.get())
        ax1.set_xlabel(X_name.get())

        
        for i in range(len(list_func)):
            ax1.plot(x, eval(list_func[i]), label = list_func[i])
            if n%2== 0:
                ax1.legend()
        
                    
        canva.draw()
        #ax.grid()
        #plt.show()
        return
    except NameError or ValueError:
        Entry_field.delete(0,END)
        Entry_field.insert(0, "Nieprawidłowa funkcja")

def kill():
    """Zamknij okno aplikacji

    Funkcja przypisana do przycisku Kill_button
    """
    root.destroy()

def x_range_min():
    """Sprawdź poprawność zakresu minimalnego x, w przypadku błędu wpisz 'Zły zakres'

    Wartość zakresu jest pobierana z pola tekstowego X_min.
    """

    global x_min
    try:
        x_min = float(X_min.get())
    except ValueError:
        X_min.delete(0, END)
        X_min.insert(0, "Zły zakres")

def x_range_max():
    """Sprawdź poprawność zakresu maksymalnego x, w przypadku błędu wpisz 'Zły zakres'

    Wartość zakresu jest pobierana z pola tekstowego X_max.
    """
    
    global x_max 
    try:
        x_max = float(X_max.get())
    except ValueError:
        X_max.delete(0, END)
        X_max.insert(0, "Zły zakres")

def check():
    """Zwiększ wartość globalnej zmiennej n oraz zmień kolor przycisku.
    Funkcja przypisana do przycisku Check_button.
    """
    global n
    n += 1
    if n % 2 == 0:
        Check_button.configure(bg = "#ffb3fe")
    else:
        Check_button.configure(bg = "white")
    

###############  TWORZENIE OKNA APLIKACJI   ####################

n = 1   
root = Tk()

#pole do wpisywanie funkcji
Entry_field = Entry(root, bg = "light yellow", width=40)

#pole do ustalania zakresów X
X_min = Entry(root)
X_max = Entry(root)

#Tytuł oraz etykiety osi
Title_graph = Entry(root, bg = "tomato", width=25)
X_name = Entry(root, bg = "lemon chiffon")
Y_name = Entry(root, bg = "cyan")

#Buttons
Check_button = Button(root, text = "Check Button", command = check)
Draw_button = Button(root, text = "Draw", command = get_function)
Kill_button = Button(root, text = " X ", command= kill, bg = "red", fg = "white", width = 3)

#Sin_button = Button(root, text="sin", command= sin_b)
#Cos_button = Button(root, text="cos", command= cos_b)

#Sqrt_button = Button(root, text="sqrt", command= sqrt_b)
#Power_button = Button(root, text="power", command=power_b)

#Canva
fig = Figure(figsize=(1.5,2.5), dpi = 100)
canva = FigureCanvasTkAgg(fig, master = root)
canva.get_tk_widget().place(height = 365, width = 410, x = 5, y = 150)

#LabelFrame
How_to = LabelFrame(root, text = "Instrukcja")
Special = LabelFrame(root, text = "Funcje elementarne")

#Labele root
Entry_label = Label(root, text="f(x) = ")
X_axis_label = Label(root, text = "x axis label")
Y_axis_label = Label(root, text = "y axis label")
X_min_label = Label(root, text= "x min")
X_max_label = Label(root, text= "x max")
Title_label = Label(root, text= "graph title")

#Labele How_to oraz Special
How_to_label = Label(How_to, text = "Kalkulator przyjmuje \n zmienną x \n powinno zachować się \n prawidłową składnię \n dla języka Python \n \n funcje należy \n oddzielać znakiem ;")
Special_label = Label(Special, text = "Możliwe jest używanie \n funkcji elementarnych \n wystarczy wpisać: \n sin(x) \n cos(x) \n sqrt(x, y) dla x^(1/y) \n power(x, y) dla x^y \n log(x, y) dla log_y(x) \n oraz stała pi")

###    ROZMIESZCZENIE     ###

#gridowanie Buttonów
Draw_button.grid(row = 9 , column=1, columnspan=1)
Kill_button.place(x = 545, y = 0, height = 30, width = 30)
Check_button.grid(row= 9, column = 2, columnspan= 2)



#gridowanie miejsca na funkcję oraz ich Labeli
Entry_label.grid(row = 3, column = 1)
Entry_field.grid(row=4, column=1)

#gridowanie zakresów funcji oraz ich Labeli
X_min_label.grid(row = 5, column = 1, columnspan = 1)
X_min.grid(row=6,column=1, columnspan=1)

X_max_label.grid(row = 5, column = 2, columnspan = 2)
X_max.grid(row=6,column= 2, columnspan=2)

#gridowanie tytułów osi, samego wykresu oraz ich Labele
X_axis_label.grid(row = 7, column = 1, columnspan =1)
X_name.grid(row = 8, column = 1, columnspan=1)

Y_axis_label.grid(row = 7, column = 2, columnspan =2)
Y_name.grid(row = 8, column = 2, columnspan=2)

Title_label.grid(row = 3, column = 2, columnspan =2)
Title_graph.grid(row = 4, column = 2, columnspan=2)

#Umieszczanie wskazówek dotyczących obsługi aplikacji

How_to.place(x = 420, y = 170, height= 150, width= 150)
How_to_label.pack()

Special.place(x = 420, y =  330, height = 170, width = 150)
Special_label.pack()

root.minsize(570,520)
root.maxsize(570,520)
root.title("Wolfram 2.0")
root.mainloop()
