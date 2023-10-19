import random

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0 ]
        self.portaHalteres = {}
        self.reiniciar_o_dia

    def reiniciar_o_dia(self):
        self.portaHalteres = { i: i for i in self.halteres }

    def listar_halteres(self):
        return [i for i in self.portaHalteres.values() if i !=0]

    def listar_espacos(self):
        return [i for i, j in self.portaHalteres.values() if j == 0]

    def pegar_haltere(self, peso):
        halt_pos = list(self.portaHalteres.values()).index(peso)
        key_halt = list(self.portaHalteres.keys())[halt_pos]
        self.portaHalteres[key_halt] = 0
        return peso
    
    def devolverHaltere(self, pos, peso):
        self.portaHalteres[peso] = peso

    def calcularCaos(self):
        caos = [i for i, j in self.portaHalteres.items() if i != j]
        return len(caos) / len(self.portaHalteres)

class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_haltere(self.peso)

    def finalizar_treino(self):
        espacos = self.academia.listar.espacos()
        
        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolverHaltere(self.peso, self.peso)
            else:
                pos = random.choice(espacos)
                self.academia.devolverHaltere(pos, self.peso)
        
        elif self.tipo == 2:
            pos = random.choice(espacos)
            self.academia.devolverHaltere(pos, self.peso)
        self.peso = 0



academia = Academia()

usuarios = [Usuario(1, academia) for i in range(10)]
usuarios += [Usuario(2, academia) for i in range(1)]
random.shuffle(usuarios)

list_chaos = []

for k in range(50):
    for i range(10):
        random.shaffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
    list_chaos += [academia.calcularCaos()]

academia.portaHalteres
academia.calcularCaos()
        

    