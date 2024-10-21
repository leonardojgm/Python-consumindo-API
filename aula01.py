class Banco:
    def __init__(self, nome = '', endereco = ''):
        self._nome = nome
        self._endereco = endereco
        
class Agencia(Banco):
    def __init__(self, nome = '', endereco = '', numero = 0):
        super().__init__(nome, endereco)
        self._numero = numero

class Veiculo:
    def __init__(self, marca = '', modelo = '', ligado = False):
        self._marca  = marca 
        self._modelo = modelo
        self._ligado = ligado

    def __str__(self):
        return f'{self._marca} {self._modelo}, - Status: {'Ligado' if self._ligado else 'Desligado'}'
    
class Carro(Veiculo):
    def __init__(self, marca = '', modelo = '', ligado = False, portas = 0):
        super().__init__(marca, modelo, ligado)
        self._portas  = portas 

    def __str__(self):
        return f'{super().__str__()}, {self._portas} portas'
    
class Moto(Veiculo):
    def __init__(self, marca = '', modelo = '', ligado = False, tipo = ''):
        super().__init__(marca, modelo, ligado)
        self._tipo   = tipo  

    def __str__(self):
        return f'{super().__str__()}, tipo {self._tipo}'
    
carro1 = Carro('Fiat', 'Uno', True, 4)
carro2 = Carro('Volkswagen', 'Gol', True, 4)
carro3 = Carro('Ford', 'Fusion', True, 4)
moto1 = Moto('Honda', 'CB 250', True, 'casual')
moto2 = Moto('Harley', 'Ducati', True, 'esportiva')
moto3 = Moto('Yamaha', 'YBR', True, 'esportiva')

print(carro1)
print(carro2)
print(carro3)
print(moto1)
print(moto2)
print(moto3)