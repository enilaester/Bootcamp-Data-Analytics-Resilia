#variável para o menu ficar em loop até que o número 0 seja digitado.
continuar = True  

#dicionários usados
dicio_vagas ={}

#listas usadas
lista_analista=[]
lista_cientista=[]
lista_classificados=[]
lista_classificados2=[]
lista_analistapadrao = ["python","power bi","sql","comunicação","comunicar"]
lista_cientistapadrao = ["python","banco de dados","machine learning","resolução de problemas", "estatística", "resolver problemas"]

#definição de funções       
        
def vagas():
    
    for i in dicio_vagas.values():

        if i == "analista de dados":
            lista_analista.append("analista de dados")
        elif i == "cientista de dados":
            lista_cientista.append("cientista de dados")  
        else:
            print('Não há candidatos cadastrados.')

def classificar_analista():
    for palavrachave in lista_analistapadrao:

        if palavrachave in resumo_analista:# resumo só de analistas
            
            lista_classificados.append(resumo_analista)

def classificar_cientista():
    for palavrachave in lista_cientistapadrao:
        if palavrachave in resumo_cientista: #resumos só de cientistas
            
            lista_classificados2.append(resumo_cientista)

def cadastro():
    global nome
    global resumo
    global resumo_analista
    global resumo_cientista
    nome = input(f'\nDigite o nome completo do candidato(a): ')
    vaga = input(f'Para qual vaga ele(a) está se aplicando? Digite "Analista de Dados" ou "Cientista de Dados": ')
    resumo = input('Insira o resumo do candidato(a): ')

    if dicio_vagas.get(nome):  #verificando se o candidato já está cadastrado pelo input do nome
        print("O candidato(a)",nome,"já está no sistema.")
    elif vaga.lower() == 'analista de dados': #condicional, se for para a vaga de analista, será usado uma variável e lista próprias.
        resumo_analista = resumo.lower()
        dicio_vagas[nome] = vaga.lower()
        classificar_analista() #chamando a função para conferir se o candidato será classificado ou não para a vaga de analista.

    elif vaga.lower() == 'cientista de dados': #condicional, se for para a vaga de cientista, será usado outra variável e lista.
        resumo_cientista = resumo.lower()
        dicio_vagas[nome] = vaga.lower()
        classificar_cientista() #chando a função para conferir se o candidato será classficado ou não para a vaga de cientista.

#___________________________________INÍCIO DO MENU__________________________________________________________________________________________

print(f'\nOlá, você está no sistema de cadastro do RH!\n1.Cadastrar candidato(a)\n0.Sair\n')

#menu está dentro da condicional while
while continuar:
    continuar = int(input(f'O que deseja fazer? Digite o número da opção escolhida: '))
    if continuar == 1:
        cadastro()  #Chamando a 1º função
    elif continuar == 0:
        continuar = False
        print("O sistema será encerrado, obrigado.")
    else:
        print("Opção inválida, tente novamente.")


vagas() #função para criar listas de candidaturas para as vagas

print('________________RELATÓRIO FINAL____________________')

# Quantidade de candidatos inscritos
print(f'Há {len(dicio_vagas)} candidato(s) registrado(s) no total.')
print(f'Há {len(lista_analista)} candidato(s) para a vaga de "Analista de dados."')
print(f'Há {len(lista_cientista)} candidato(s) para a vaga de "Cientista de dados."')

# Quantidade de candidatos classificados
print(f'Há {len(lista_classificados)} candidato(s) classificado(s) para a vaga de "Analista de Dados".')
print(f'Há {len(lista_classificados2)} candidato(s) classificado(s) para a vaga de "Cientista de Dados".')


#______________________DADOS PARA TESTAR O CÓDIGO__________________________________________________________________

#Resumo 1 - José Menezes: Me formei no Ensino Médio em 2021 e desde 2022 faço parte da Resilia Educação como aluno do curso de "Análise de Dados". Em apenas dois meses, já co-criei diferentes projetos na linguagem Python para resolver demandas reais de empresas e da sociedade no geral.

#Resumo 2 - Maria das Graças: Matemática de formação, estou migrando para a área de dados porque sou uma entusiasta da área de tecnologia. Ao longo da graduação, fiz Iniciação Científica e pude aprender sobre modelagem em Excel e linguagens de programação como Python e R.

#Resumo 3 - Marcelo Ferreira: Atualmente trabalho em uma multinacional e sou responsável pelo setor de  marketing. Por estar em contato com os escritórios de toda a América Latina, lido diarimente com muitos bancos de dados e adquiri vasta experiência com o SQL. Tenho facilidade em produzir relatórios e me comunicar para diferentes tipos de público.

#Resumo 4 - Juliana da Silva: Ao longo dos últimos 3 anos como designer, desenvolvi diversos projetos em DataViz utilizando para isso principalmente Power BI. Tenho excelente comunicação verbal e escrita e sei aplicar storytelling aos dados.

#Resumo 5 - Carlos de Almeida: Estou cursando uma segunda graduação em Ciência da Computação e sou motivado quando estou em um contexto de desafio. Gosto de aplicar pensamento lógico para resolver problemas.

#Resumo 6 - João Lima: Estou cursando pós graduação em Data Science e atualmente sou responsável pela área de business analytics de uma locadora de veículos. Sou focado em resolução de problemas e tenho experiência em tomar decisões em contextos de incerteza e pressão. 

#Resumo 7 - Patricia de Almeida: Recentemente resolvi fazer minha transição de carreira do mundo acadêmico para o corporativo. Em meu doutorado desenvolvi pesquisas envolvendo I.A e machine learning. Tenho experiência com Python e C++.

#Resumo 8 - Cristina Souza: Como responsável pela área de análise de dados, trabalho principalmente com a linguagem R e SQL. Coordeno cinco equipes ao redor do Brasil. Sou proativa e atenciosa aos detalhes.

#Resumo 9 - Verônica Freitas - Trabalho como atuária em um banco de prestígio nacional e tenho ampla experiência com análise de risco, probabilidade e testes estatísticos. Estou habituada a lidar com grandes volumes de dados diariamente.

#Resumo 10 - Túlio Pires - Trabalho há 10 anos como professor de Web Designer e almejo me inserir na área de dados. Tenho vasta experiência com Java, C e C++ e atualmente estou fazendo especialização em Data Science e Analytics.


     
