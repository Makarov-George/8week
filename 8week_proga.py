
import math
import matplotlib.pyplot as plt
import numpy as np

class Radioactive():
    def __init__(self, Z, A):
        self.Z = Z
        self.A = A
        self.N = A - Z

    def set(self, Z, A):
        self.Z = Z
        self.A = A

    def get_Z(self):
        return self.Z
    
    def get_A(self):
        return self.A

    def energy_VZ(self):
        print("Для ядра с барионным зарядом:", self.A)
        if self.A%2 == 0 and self.Z%2 == 0:
            self.energy = 15.7*self.A - 17.8*(self.A**(2/3)) - 0.71*(self.Z**2)/(self.A**(1/3)) - 23.7*(self.A - 2*(self.Z))**2/self.A + 34*(self.A**(-3/4))
        elif self.A%2 != 0 and self.Z%2 != 0:
            self.energy = 15.7*self.A - 17.8*(self.A**(2/3)) - 0.71*(self.Z**2)/(self.A**(1/3)) - 23.7*(self.A - 2*(self.Z))**2/self.A - 34*(self.A**(-3/4))
        elif self.A%2 != 0:
            self.energy = 15.7*self.A - 17.8*(self.A**(2/3)) - 0.71*(self.Z**2)/(self.A**(1/3)) - 23.7*(self.A - 2*(self.Z))**2/self.A
        self.relative_energy = round(self.energy/self.A, 2)
        print('Удельная энергия связи: ', self.relative_energy, 'Мэв/нуклон')

    def mass(self):
        self.mass = self.Z*7.289 + self.N*8.071 - self.energy + self.A*931.5
        print('Масса атома: ', round(self.mass, 2), 'Мэв', 'или', round(self.mass/931.5, 2), 'а.е.м.')
        
    def radius(self):
        self.radius = round(1.3*(self.A**(1/3)), 2)
        print('Радиус атома: ', self.radius, 'Фм')
        
    def ystoichivost(self):
        self.Z_ravn = int(self.A/(0.015*self.A**(2/3)+2))+1
        if self.Z != self.Z_ravn:
            print('Изотоп неустойчив к b-распаду')
        else:
            print('Изотоп устойчив к b-распаду')

    def delenie_na_oskolki(self):
        if self.A%4 == 0 and self.Z%4 == 0:
            print('Изотоп может поделиться на 2 одинаковых четно-четных осколка\n')
        else:
            print('Изотоп не может поделиться на 2 одинаковых четно-четных осколка\n')

    def plot_R_ot_Z(self):

        arZ = list()
        arR = list()
        for i in nucleis:
            arZ.append(i.get_Z())
            arR.append(i.radius)
        indices = sorted(range(len(arZ)), key=lambda i: arZ[i])
        arZ = np.array(arZ)
        arR = np.array(arR)
        indices = arZ.argsort()  
        print(arZ[indices], arR[indices] )
        plt.figure(figsize=[9,6])
        plt.plot(arZ[indices], arR[indices], linewidth=2)
        plt.grid(True, color='#DDDDDD', linestyle='--', which='both')
        plt.ylabel('Радиус ядра, Мэв')
        plt.xlabel('Заряд ядра')
        plt.title('Зависимость радиуса ядер от числа протонов')
        plt.legend(['1'])
        plt.show()
        
    def plot_E_ot_A(self):
        arA = list()
        arE = list()
        for i in nucleis:
            arA.append(i.get_A())
            arE.append(i.relative_energy)
        indices = sorted(range(len(arA)), key=lambda i: arA[i])
        arA = np.array(arA)
        arE = np.array(arE)
        indices = arA.argsort()  
        print(arA[indices], arE[indices] )
        plt.figure(figsize=[9,6])
        plt.plot(arA[indices], arE[indices], linewidth=2)
        plt.grid(True, color='#DDDDDD', linestyle='--', which='both')
        plt.ylabel('Удельная энергия связи, Мэв/нкулон')
        plt.xlabel('Количество нуклонов')
        plt.title('Зависимость удельной энергии связи ядра от барионного заряда')
        plt.legend(['2'])
        plt.show()


    def atom_info(self):
        self.energy_VZ()
        self.mass()
        self.radius()
        self.ystoichivost()
        self.delenie_na_oskolki()


if __name__ == "__main__":
    nucleis = [Radioactive(92,238), 
    Radioactive(94,239), 
    Radioactive(98,252), 
    Radioactive(94,238), 
    Radioactive(52,135),
    Radioactive(28,60),
    Radioactive(8,16),
    Radioactive(7,15),
    Radioactive(15,29),
    Radioactive(24,52)]

Atom = Radioactive(92,238)

for i in nucleis:
    Atom = i
    Atom.atom_info()

Atom.plot_R_ot_Z()
Atom.plot_E_ot_A()
