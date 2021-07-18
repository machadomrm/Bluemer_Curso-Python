from random import randint

class Calendário():
    def __init__(self):
        self.dia = 1

    def __str__(self):
        return f"{self.dia}"

    def pulaDia(self):
        self.dia += 1

class Familia():
    def __init__(self):
        self.sujo = False
        self.fome = 0
        self.doente = False
        self.vida = True
        self.descansado = True
        self.sanidade = 0
        if self.fome == 3:    
            self.vida == False

    def __str__(self):
        return f" está " + ("vivo(a), " + (("sujo(a), " if self.sujo else "limpo(a), ") + ("com fome, " if self.fome >= 1.5 else "sem fome, ") + ("está mentalmente bem, " if self.sanidade <= 1.5 else "está com sinais de loucura, ") + ("descansado(a) e " if self.descansado else "cansado(a) e ") + ("doente." if self.doente else "saudável.")) if self.vida else "morto(a)." )

    def morrer(self):
        if self.fome == 3:    
            self.vida == 0

    def endoidar(self):
        if self.descansado == 3:
            self.sanidade += 0.5

    def descansar(self):
        self.descansado = True
        self.fome += 0.5
        self.sujo = True

class itens():
    def __init__(self):
        self.comida = 10
        self.agua = 10
        self.arma = 1
        self.mascara = 1
        self.cadeado = 1
        self.radio = 1
        self.baralho = 1
        self.gaita = 1
        self.violao = 1
        self.remedios = 5
    
    def __str__(self):
        return f"{self.remedios}"
        
    def tomar_remedios(self):
       self.remedios = self.remedios - 1
               
if __name__ == "__main__":
    calendario = Calendário()
    dolores = Familia()
    jose = Familia()
    ana = Familia()
    carlos = Familia()
    bau = itens()
    print("---"*14)
    print('GRIPÃO A DOENÇA FATAL')
    print()
    print('Chegou no país uma terrível doença chamada Gripão que esta matando as pessoas e o')
    print('governo decidiu colocar a população em um extremo confinamento em suas casas até que a')
    print('cura chegue ou que não tenha mais a doença no país.')
    print('Sua família, Mãe Dolores, Pai José, irmã Ana e você Carlos, precisam se proteger desta terrível doença.')
    print()
    print('Você decide o que fazer!')
    print()
    print('Que comece o jogo!!!')
    print()
    print("---"*14)
    print(f"Dolores{dolores}")
    print(f"José{jose}")
    print(f"Ana{ana}")
    print(f"Carlos{carlos}")
    print()
    print(f"Você(s) tem {bau.comida} de comida e {bau.agua} de água.")
    print("1 valor de comida ou água alimenta ou hidrata bem uma pessoa.")

dia = Calendário()

print('\n----------------- Dia', dia, '--------------------')
print('\nPai e filho mal chegaram ao abrigo e já estão com fome!\n')
escolha = input('Deseja alimentá-los agora ? (S/N): ').upper().replace('SIM','S')

if escolha == 'S':
  print('Muito cedo para alimentá-los, pode ser que falte comida para o resto da família!')
  #Aqui entra a parte do suprimentos
elif escolha == 'N':
  print('Não esqueça de alimentá-los ainda hoje, senão eles poderão morrer!')
else:
    while escolha != 'S' and escolha != 'N':
      escolha = input('Opção errada, digite apenas S ou N: ').upper().replace('SIM','S')
      if escolha == 'S':
        pass
      elif escolha == 'N':
        print('Não esqueça de alimentá-los o quanto antes, senão eles poderão morrer!')
           
dia.pulaDia()
print('\n----------------- Dia', dia, '--------------------')

escolha = input('O rádio amador está tocando, deseja ouvir a notícia ? (S/N): ').upper().replace('SIM','S')
if escolha == 'S':
    print('Está sendo noticiado que para sair brevemente do abrigo deve-se usar a mascara de proteção, pois do contrários você poderá ser contaminado com o GRIPÃO!! e contaminar toda a sua família')
else:
    aleatorio = randint(0,1)
    if aleatorio == 0:
        print('A mãe resolveu sair do abrigo sem mascara para ver a situação lá fora, porém como estava muito frio parece que se resfriou e terá que tomar remédio para não piorar!')
        tomar = itens()
        tomar.tomar_remedios()
        
dia.pulaDia()        
print('\n----------------- Dia', dia, '--------------------\n')
print('\nBarulhos do lado de fora.')
escolha = input('Você quer ir lá fora com a mascara para ver o que é o barulho? (S/N): ').upper().replace('SIM','S')

if escolha == 'S':
  print('você vê um grupo de vândalos invadindo outras casas em busca de alimentos, proteja-se.')
  dia.pulaDia()
else:
    while escolha != 'S' and escolha != 'N':
      escolha = input('Opção errada, digite apenas S ou N: ').upper().replace('SIM','S')
      if escolha == 'S':
        pass
      elif escolha == 'N':
        print('Ficamos apreensivos com o barulho vindo do lado de fora e não tivemos coragem, de abrir a porta!')        
    dia.pulaDia()
        
print('\n----------------- Dia', dia, '--------------------') #Dia 04

dia.pulaDia()        
#print('\n----------------- Dia', dia, '--------------------')
print('\nA menina esta entediada e quer fazer algo para se divertir.')
escolha = input('Você quer jogar baralho com ela? (S/N): ').upper().replace('SIM','S')

if escolha == 'S':
  print('Familia fica animada e feliz.')
  dia.pulaDia()
else:
    while escolha != 'S' and escolha != 'N':
      escolha = input('Opção errada, digite apenas S ou N: ').upper().replace('SIM','S')
      if escolha == 'S':
        pass
      elif escolha == 'N':
        print('Ana parou de falar com a família e começa a ter problemas de loucura.')        
    dia.pulaDia()