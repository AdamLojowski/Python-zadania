"Skrypt rozwiązuje równanie ruchu wahadła matematycznego z tłumieniem oraz okresową siłą wymuszającą"


import argparse
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
#Q w A v th

parser = argparse.ArgumentParser(description = "Skrypt rozwiązuje równanie ruchu wahadła matematycznego z tłumieniem oraz okresową siłą wymuszającą")

parser.add_argument('-Q', required = True, type = float)
parser.add_argument('-w', required = True, type = float)
parser.add_argument('-A', required = True, type = float)
parser.add_argument('-v', required = True, type = float)
parser.add_argument('-th', required = True, type = float)

args = parser.parse_args()

def f(u,x):
      return(u[1], args.A*np.cos(args.w*x)-(1/(args.Q)*u[1]+np.sin(u[0])))

y0 = [0, args.th]
xs = np.linspace(1,50,400)
us = odeint(f,y0, xs)
ys = us[:,0]
ys2 = us[:, 1]
plt.plot(xs,ys,'r-', color = 'r', label = 'theta')
plt.plot(xs, ys2, color = 'y', label = 'omega')
plt.xlabel('time')
plt.legend()
plt.title('(D^2 + (1/Q)*D + sin(th))th = A*cos(w*r)')
plt.show()
