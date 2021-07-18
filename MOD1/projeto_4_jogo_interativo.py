# Proposta de projeto de ficção interativa para avaliação de OO
# Sugestão: completar com classes filhas colocando pessoas saudáveis, trabalhos menos remunerados, casas melhor equipadas et cetera

# É obrigatório o uso de orientação a objetos (classes, encapsulamento e # polimorfismo), funções, laços (while) e condicionais (if, elif, else). 
# Para o desenvolvimento do jogo os grupos devem utilizar o arquivo disponibilizado no # moodle como exemplo.


print('GRIPÃO A DOENÇA FATAL')
print()
print('Chegou no país uma terrível doença chamada Gripão que esta matando as pessoas e o')
print('governo decidiu colocar a população em um extremo confinamento em suas casas até que a')
print('cura chegue ou que não tenha mais a doença no país.')
print('Sua família, Mãe Dona Ada, Pai Sr Oto, irmã Ana e você Natan, precisam se proteger desta terrível doença.')
print()
print('Você decide o que fazer!')
print()
print('Que comece o jogo!!!')

class Calendário():
    def __init__(self):
        self.dia = 1

    def __str__(self):
        return f"{self.dia}"

    def pulaDia(self):
        self.dia += 1

calendario = Calendário()


class GRIPÃO:
  def __init__(self, Ada, Oto, Ana, Natan):
    self.Ada = Ada
    self.Oto = Oto
    self.Ana = Ana
    self.Natan = Natan

#class Sobrevivencia:
  def __init__(self, garrafa_de_agua, lata_de_sopa, pao):
    self.garrafa_de_agua = garrafa_de_agua
    self.lata_de_sopa = lata_de_sopa
    self.pao = pao

#class Segurança:
  def __init__(self, mascara_de_protecao, espingarda, cadeado):
    self.mascara_de_protecao = mascara_de_protecao
    self.espingarda = espingarda
    self.cadeado = cadeado

#class Medicamento:
  def __init__(self, remedio):
    self.remedio = remedio

#class Entretenimento:
  def __init__(self, radio, baralho, gaita, violao):
    self.radio = radio
    self.baralho = baralho
    self.gaita = gaita
    self.violao = violao    




#from random import randint


dia = Calendário()

print('\n----------------- Dia', dia, '--------------------')
#print('\nO rádio AMADOR esta tocando, deseja atender? \n')
escolha = input('O rádio AMADOR esta tocando, deseja atender? (S/N): ').upper().replace('SIM','S')

if escolha == 'S':
  print('Noticia sobre o Gripão que esta assolando a cidade, todos da cidade estão em isolamento e não podem sair no período de 30 dias. Aguarde por mais informações.')
  #Aqui entra a parte do suprimentos
elif escolha == 'N':
  print('A família ficou sem saber da Notícia referente a QUARENTENNA. A mãe resolveu sair do abrigo sem mascara para ver a situação lá fora, porém como estava muito frio, voltou logo. Mas parece que se resfriou e terá que tomar remédio para não piorar!')
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
    print('Está sendo noticiado que para sair brevemente do abrigo deve-se usar a mascara de proteção, pois do contrários você poderá ser contaminado com o GRIPÃO e contaminar toda a sua família!')
    dia.pulaDia()
else:
    aleatorio = randint(0,1)
    if aleatorio == 0:
        print('A mãe resolveu sair do abrigo sem mascara para ver a situação lá fora, porém como estava muito frio parece que se resfriou e terá que tomar remédio para não piorar!')
        tomar = itens()
        tomar.tomar_remedios()
        print(f'ainda tem {tomar} remedios no estoque')
        dia.pulaDia()
    else:
        print('O rádio dizia que ninguem deve sair dos seus abrigos, pois corre grande risco de se contaminar com GRIPÃO')
        print('A mãe volta para o abrigo sã e salva')
        dia.pulaDia()

print('\n----------------- Dia', dia, '--------------------')
