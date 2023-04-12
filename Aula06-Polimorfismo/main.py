from Cidade import Cidade
from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

c1 = Cidade(1, "Porto Alegre")
c2 = Cidade(2, "Capão da Canoa")

p1 = Pessoa("Maria", "1122-3344", c1)
pf1 = Fisica("João", "123456", c2, "000.222")

#pf1.imprimir()

print(p1)
print("----------------")
print(pf1)
