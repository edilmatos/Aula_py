#8) Escreva um programa que receba o nome do usuário. Se o nome for “Optimus Prime”, imprima
#“Bem-vindo, você é um guerreiro de Cybertron”. Caso contrário, imprima “Bom dia, NOME”
#(Sendo NOME o nome dado pelo usuário)

nome = str(input('Quam o nome do usuário? '))

if nome == 'Optimus Prime':
    print('Bem-vindo, você é um guerreiro de Cybertron')
else:
    print('Bom dia {}'.format(nome))
    