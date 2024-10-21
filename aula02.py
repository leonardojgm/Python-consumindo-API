from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, marca = '', modelo = ''):
        self._marca  = marca 
        self._modelo = modelo

    def __str__(self):
        return f'{self._marca} {self._modelo}'

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @abstractmethod
    def ligar(self):
        pass
    
class Carro(Veiculo):
    def __init__(self, marca = '', modelo = '', cor = ''):
        super().__init__(marca, modelo)
        self._cor  = cor 

    @property
    def cor(self):
        return self._cor

    def ligar(self):
        print(f"O carro {self._modelo} está ligado.")

carro1 = Carro(marca="Ford", modelo="Focus", cor="Preto")
carro2 = Carro(marca="Chevrolet", modelo="Cruze", cor="Prata")
carro3 = Carro(marca="Honda", modelo="Civic", cor="Vermelho")

print(f"Carro 1: {carro1.marca} {carro1.modelo}, Cor: {carro1.cor}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}, Cor: {carro2.cor}")
print(f"Carro 3: {carro3.marca} {carro3.modelo}, Cor: {carro3.cor}")

carro1.ligar()
carro2.ligar()
carro3.ligar()