#TODO2: MAPEAMENTO DE PÚBLICO PARA PESQUISA AMBIENTAL
#ATIVIDADE: CRIAR UM CÓDIGO QUE CALCULE O TAMANHO AMOSTRAL
#variáveis
# z escore = 1,96
# p proporção = O.05
# e = margem de erro no formato decimal
# N = tamanho da população


from math import ceil
print( 'Olá! Vamos calcular o tamanho da sua amostra!')

N = int(input( "Informe o tamanho da sua população (apenas números): "))
e = float(input("Informe a margem de erro desejada (em formato decimal). Quanto menor a margem de erro, maior será a amostra: "))

calculo1 = (1.96**2*0.5*(1 - 0.5))
calculo2 = (calculo1/(e**2))
calculo3 = 1 + (calculo1/((e**2)*N))
calculofinal = (calculo2/calculo3)
arredondamento = str(ceil(calculofinal))
print("O tamanho da amostra deverá ser composto de", arredondamento, "respostas.")


#TESTES
# Brasília, DF = 3094325
# Recife, PE = 1661017
# Rio Branco, AC = 419452
# Campo Grande, MS = 916001
# São Paulo, SP = 12396372


