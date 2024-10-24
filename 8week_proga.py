
import math

class Radioactive():
    def __init__(self, Z, A):
        self.Z = Z
        self.A = A
        self.N = A - Z

    def set(self, Z, A):
        self.Z = Z
        self.A = A

    def get(self):
        return self.Z, self.A

    def energy_VZ(self):
        if self.A%2 == 0 and self.Z%2 == 0:
            self.energy = 15.7*self.A - 17.8*(self.A**(2/3)) - 0.71*(self.Z**2)/(self.A**(1/3)) - 23.7*(self.A - 2*(self.Z**2))/self.A + 34*(self.A**(-3/4))
        elif self.A%2 != 0 and self.Z%2 != 0:
            self.energy = 15.7*self.A - 17.8*(self.A**(2/3)) - 0.71*(self.Z**2)/(self.A**(1/3)) - 23.7*(self.A - 2*(self.Z**2))/self.A - 34*(self.A**(-3/4))
        elif self.A%2 != 0:
            self.energy = 15.7*self.A - 17.8*(self.A**(2/3)) - 0.71*(self.Z**2)/(self.A**(1/3)) - 23.7*(self.A - 2*(self.Z**2))/self.A
        self.relative_energy = self.energy/self.A
        print('Удельная энергия связи: ', self.relative_energy, 'Мэв/нуклон')

    def mass(self):
        self.mass = self.Z*7.289 + self.N*8.071 - self.energy + self.A*931.5
        print('Масса атома: ', self.mass, 'Мэв', 'или', self.mass/931.5, 'а.е.м.')
        
    def radius(self):
        self.radius = 1.3*(self.A**(1/3))
        print('Радиус атома: ', self.radius, 'Фм')
        
    def ystoichivost(self):
        self.Z_ravn = int(self.A/(0.015*self.A**(2/3)+2))+1
        if self.Z != self.Z_ravn:
            print('Изотоп неустойчив к b-распаду')
        else:
            print('Изотоп устойчив к b-распаду')

    def delenie_na_oskolki(self):
        if self.A%4 == 0 and self.Z%4 == 0:
            print('Изотоп может поделиться на 2 одинаковых четно-четных осколка')
        else:
            print('Изотоп не может поделиться на 2 одинаковых четно-четных осколка')

    def atom_info(self):
        self.energy_VZ()
        self.mass()
        self.radius()
        self.ystoichivost()
        self.delenie_na_oskolki()


"""if __name__ == "__main__":
    nuclei = [Nucleus(92,238), 
    Nucleus(94,239), 
    Nucleus(98,252), 
    Nucleus(94,238), 
    Nucleus(52,135),
    Nucleus(28,60),
    Nucleus(8,16),
    Nucleus(7,15),
    Nucleus(15,29),
    Nucleus(24,52)]"""

Atom = Radioactive(98, 252)
Atom.atom_info()

    
