from Torre import Torre
from Apartamento import Apartamento
from Fila import Fila

t1 = Torre("Torre A", "Rua A, 100")
t2 = Torre("Torre B", "Rua B, 200")


ap1 = Apartamento("101" , t1)
ap2 = Apartamento("102" , t1)
ap3 = Apartamento("201" , t2)
ap4 = Apartamento("202" , t2)
ap5 = Apartamento("303" , t2)

ap1.vaga = 11
ap3.vaga = 12

fila = Fila()

fila.add(ap2)
fila.add(ap4)
fila.add(ap5)


print(" ---------------------------- ")

vaga = ap1.vaga
ap1.vaga = None
fila.add(ap1)

x = fila.remover()
if x is not None:
    x.vaga = vaga
