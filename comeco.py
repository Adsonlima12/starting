print (f"Hello")
c0 = input(f'Qual o teu nome: ')
print(c0,"?")
c1= input(f'nome lindo quem escolheu ? ' )

print(f'escolheu um nome lindo ')
print(c0)
c2=int(input(f"qual é a sua idade?"))
idade = c2

if idade < 18:
    print(f'Legal ',c0, ' tu tem ',c2,' anos, ainda é Jovem')
else:
        
#if idade > 18:
    print(f'Legal ',c0, ' tu tem ',c2,' anos, Exeperiente')

if idade < 18:
    c4= input(f'como está os seus estudos?')
    print(f'Mesmo que seus estudos',c4,'precisa buscar mais')
else:#if idade > 18:
     c4= input('como está a sua vida?')
     print(f'Mesmo que sua vida esteja',c4,'precisa buscar mais')
     
while True:
    resposta = input("Você deseja continuar? (s/n): ")
    if resposta.lower() == 'n':
        break
    else:
        c5=input('Como tu está agora?')
        if c5.lower()== 'mal':
            print('tu precisa se cuidar mais')
        else:
            print('Tem que cuidar da saúde sempre')
            break

