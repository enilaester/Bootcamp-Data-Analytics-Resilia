# _____________________________LISTA DE CANDIDATOS _________________________________________________________________________________

e=[]  #listas vazias
t=[]
p=[]
s= []
nota = []
notas =[]

print(f'\n' "Olá, você está no setor de cadastramento do RH ! \nVamos começar o cadastro, informe notas entre 0 e 9.") #saudação inicial

def cadastro(): #definição da função de cadastro
    e = input('Qual a nota da entrevista? ')   
    t = input('Qual a nota do teste teórico? ')
    p = input('Qual a nota do teste prático? ')
    s = input('Qual a nota em soft skills? ')

    nota = [e,t,p,s]           #junção das avaliações em uma única nota
    notas.append(nota)         # cada nota é então adicionada na lista 'notas'
        

cadastro()     #para chamar a função de cadastro
    
def escolha(): #definição da função para o usuário decidir se quer continuar o cadastro ou não
    
    escolha = input("Quer continuar cadastrando? Digite 'Sim' ou 'Não': ")
    escolha = escolha.capitalize()
   
    while escolha:
        if escolha == "Sim":
              
                e = input('Qual a nota da entrevista? ')  
                t = input('Qual a nota do teste teórico? ')
                p = input('Qual a nota do teste prático? ')
                s = input('Qual a nota em soft skills? ')

                nota = [e,t,p,s]
                notas.append(nota)
                
                escolha = input("Quer continuar cadastrando? Digite 'Sim' ou 'Não': ")
                escolha = escolha.capitalize()

           
        else:
            print('Cadastramento finalizado.')
            print('Foram cadastrados', len(notas), 'candidatos até o momento.')  #quando o cadastro termina, retorna a quantidade de candidatos que foi cadastrada.
            break


escolha() #para chamar a função escolha


#_______________________________________FUNÇÃO PARA CLASSIFICAR CANDIDATOS_____________________________________________________________


def busca(notas,e_minimo,t_minimo,p_minimo,s_minimo):  #definição da função de busca que irá comparar as avaliações de cada candidato com os critérios informados pelo usuário
    for numero in notas:
        if numero[:][0] >= e_minimo and numero[:][1] >= t_minimo and numero[:][2] >= p_minimo and numero[:][3] >= s_minimo: #condição para satisfazer os critérios
             
         print(f"O candidato avaliado com e{numero[:][0]}_t{numero[:][1]}_p{numero[:][2]}_s{numero[:][3]} atende os critérios desejados.") #retorno positivo, coloca a nota formatada no modelo ex_tx_px_sx
        
        else:
            print(f'O candidato não atingiu os requisitos mínimos.') #retorno negativo
            

print('Obrigado! Agora você deve informar as notas mínimas desejadas para cada item:')
e_minimo = input('Qual a nota mínima para a entrevista? ')
t_minimo = input('Qual a nota mínima para o teste teórico? ')
p_minimo = input('Qual a nota mínima para a teste prático? ')
s_minimo = input('Qual a nota mínima em soft skills? ')

busca(notas,e_minimo,t_minimo,p_minimo,s_minimo) #para chamar a função de busca

