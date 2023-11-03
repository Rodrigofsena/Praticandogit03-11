print("Olá, meu nome é Luna, eu sou uma IA")
bemmau = input("Tudo bem? (yes/no) ")
nome = input("Qual é o seu nome? ")
bem = "yes"
mau = "no"

if bemmau == bem:
    print("Que ótima notícia {}, é sempre bom saber que as coisas estão indo bem para alguem!".format(nome))
else:
    print("As coisas vão melhorar, pode acreditar, {}, nem tudo oque eu falo se escreve mas, eu entendo oque é problema.!".format(nome))

print ("{} Você tem quantos anos?".format(nome))
anonascimento = int (input("Não melhor ainda eu vou advinhar, em que ano você nasceu?"))
anoatual = int(2023) 
idade = anoatual - anonascimento
if idade <= 0:
    print("Você não pode ter idade negativa, certo?")
elif idade <= 12:
    print("Sério, {}? que coisa boa com {} anos, você ainda tem muita coisa pra aprender".format(nome, idade))
elif idade <= 30:
    print("Sério, {}? Com {} anos, eu jurava que você era mais novo.".format(nome, idade))
else:
    print("Nossa, Parabéns, {}! Com {} anos, você está bem conservado, esta com cara de ter 20.".format(nome, idade))


## praticando o comando direto do repositorio online.
#4 tentativa de entender.

