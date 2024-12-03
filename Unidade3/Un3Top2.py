import os

gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "V – V – V – F."
    B = "V – F – F – V."
    C = "F – V – V – V."
    D = "V – F – V – F."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("1  Um sistema distribuído deve incorporar muitas características que permitam o acesso seguro e contínuo, pelas entidades presentes no ambiente, aos seus recursos. Esses recursos manipulam dados que devem ser preservados, confiáveis e acessíveis dentro de parâmetros aceitáveis de desempenho e atributos como replicação e consistência conferem ao sistema essas características. Dessa forma, avalie as sentenças relacionadas aos conceitos de replicação e consistência classificando com V as sentenças verdadeiras e F as falsas:")
    print("\n(   )  Utilizar visões de dados em dispositivos pertencentes a um sistema distribuído, característica de consistência, aumentam a capacidade do sistema a responder a possíveis falhas, contribuindo também para o seu desempenho e confiabilidade.")
    print("\n(   )  Utilizar visões de dados em dispositivos pertencentes a um sistema distribuído, característica de replicação, aumentam a capacidade do sistema a responder a possíveis falhas, contribuindo também para o seu desempenho e confiabilidade.")
    print("\n(   )  Ao se utilizar os serviços de armazenamento, que permitem o compartilhamento de arquivos de máquinas locais em servidores centrais disponibilizados por uma empresa, está-se usando uma característica de replicação de dados.")
    print("\n(   )  Ao se utilizar os serviços de armazenamento, que permitem o compartilhamento de arquivos de máquinas locais em servidores centrais disponibilizados por uma empresa, está-se usando uma característica de replicação de dados. Essa característica favorece o conceito de confiabilidade que deve existir nos ambientes distribuídos.")
    print("\nAgora, assinale a alternativa CORRETA:")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    
    if r == "A":
        resp.append(r)
        r=A
    elif r == "B":
        resp.append(r)
        r=B
    elif r == "C":
        resp.append(r)
        r=C
        if r == rCorreta:
            pontos +=2
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao1()
def questao2():
    global pontos
    A = "As sentenças I e II representam proposições verdadeiras, mas a II não é uma justificativa correta da I."
    B = "As sentenças I e II não representam proposições verdadeiras."
    C = "A sentenças I é uma proposição verdadeira, porém a II é uma proposição falsa."
    D = "As sentenças I e II representam proposições verdadeiras, e a II é uma justificativa correta da I."

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("2  Talvez uma das características mais básicas de qualquer tipo de sistema é a de que ele é suscetível a uma falha, ocasionada por um erro de programação, por uma queda de conectividade, a indisponibilidade de um recurso etc. Todos esses exemplos ganham uma magnitude maior quando adicionada a eles a característica distribuída. Sendo assim, outro elemento de significativa relevância para estudo é como construir sistemas distribuídos tolerantes a falhas. Sabendo disso, avalie a sentença de afirmação e a sentença de explicação relacionadas ao conceito de tolerância a falhas envolvidas na construção de sistemas distribuídos.")
    print("\nI-   Um reprodutor de áudio contém uma lista de rádios que podem ser ouvidas através da internet, porém ao clicar na rádio “Classical FM” a mensagem “a lista Classical FM não pode ser usada porque não foi encontrada no repositório do servidor” é apresentada na tela do dispositivo em questão. Isso representa uma falha que precisa ser tratada por um sistema distribuído.")
    print("\nPORQUE")
    print("\nII-  O erro que ocasionou a falha precisa ser tratado pela característica de tolerância a falhas de um sistema distribuído, isto é, possibilitar que o sistema possa identificar e assumir um comportamento tolerante ao erro, mantendo a continuidade de seus serviços.")
    print("\nAgora, assinale a alternativa que apresenta a resposta CORRETA:\n")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    if r == "A":
        resp.append(r)
        r=A
    elif r == "B":
        resp.append(r)
        r=B
        if r == rCorreta:
            pontos +=2
    elif r == "C":
        resp.append(r)
        r=C
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao2()
def questao3():
    global pontos
    A = "As sentenças II e III estão corretas."
    B = " As sentenças II e IV estão corretas."
    C = "As sentenças I e II estão corretas."
    D = "As sentenças I e IV estão corretas."

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("3  Um sistema distribuído deve incorporar muitas características que permitam o acesso seguro e contínuo, pelas entidades presentes no ambiente, aos seus recursos. Esses recursos manipulam dados que devem ser preservados, confiáveis e acessíveis dentro de parâmetros aceitáveis de desempenho e atributos como replicação e consistência conferem ao sistema essas características. Com isso, avalie as sentenças relacionadas aos conceitos de replicação e consistência:")
    print("\nI-    A consistência impõe uma condição a uma replicação, ou replicações, de que para ela ser (ou serem) bem sucedidas implica que as visões de dados (cópias) geradas, não necessariamente, devam possuir os mesmos estados. Se elas possuírem um estado bem próximo do original já é suficiente para garantir a característica de consistência.")
    print("\nII-   A consistência impõe uma condição a uma replicação, ou replicações, de que para ela ser (ou serem) bem sucedidas implica que suas visões de dados (cópias) geradas devem possuir os mesmos estados e assim garantir a característica de consistência.")
    print("\nIII- Os modelos de consistência lidam com as regras que as réplicas podem, ou não, obedecer para a geração de seus estados. As regras, de maneira geral, são inflexíveis em relação a diferença entre os estados dos dados originais e daqueles replicados, para garantir assim o nível de consistência desejado.")
    print("\nIV- Os modelos de consistência atuam nos tipos de regras (restrições) que as réplicas devem obedecer para a geração de seus estados. Essas regras podem ser mais, ou menos, rígidas em relação a diferença entre os estados dos dados originais e daqueles replicados, garantindo assim o nível de consistência desejado.")
    print("\nAgora, indique a alternativa CORRETA:\n")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    if r == "A":
        resp.append(r)
        r=A
    elif r == "B":
        resp.append(r)
        r=B
    elif r == "C":
        resp.append(r)
        r=C
    elif r == "D":
        resp.append(r)
        r=D
        if r == rCorreta:
            pontos +=2
    os.system("cls")
questao3()
def questao4():
    global pontos
    A = "V – V – V – F."
    B = "V – F – F – V."
    C = "F – F – V – V."
    D = "V – F – V – F."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("4  Talvez uma das características mais básicas de qualquer tipo de sistema é a de que ele é suscetível a uma falha, ocasionada por um erro de programação, por uma queda de conectividade, a indisponibilidade de um recurso etc. Todos esses exemplos ganham uma magnitude maior quando adicionada a eles a característica distribuída. Sabendo disso, avalie as sentenças relacionadas aos conceitos de tolerância a falhas classificando com V as sentenças verdadeiras e F as falsas.")
    print('\n(   )  Um defeito ocorre quando um sistema cumpre parcialmente aquilo que se propõem.')
    print("\n(   )  Um erro é a causa de uma falha, e, em se tratando de sistemas distribuídos, identificar o evento, ou agente, que o causou é muito importante.")
    print("\n(   )  Uma falha representa os valores dos dados de um sistema em um dado instante de sua execução.")
    print("\n(   )  Um erro representa os valores dos dados de um sistema em um dado instante de sua execução.")
    print("\nAgora, indique a alternativa CORRETA:\n")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    if r == "A":
        resp.append(r)
        r=A
    elif r == "B":
        resp.append(r)
        r=B
    elif r == "C":
        resp.append(r)
        r=C
        if r == rCorreta:
            pontos +=2
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao4()
def questao5():
    global pontos
    A = "A sentença I está correta."
    B = "As sentenças II, III e IV estão corretas."
    C = "As sentenças I e II estão corretas." 
    D = "As sentenças III e IV estão corretas."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("5  Um sistema distribuído confiável é potencialmente um sistema tolerante a falhas, dessa forma, a confiabilidade deve ser um dos atributos mais desejável de um sistema distribuído. Com isso, avalie as sentenças relacionadas ao conceito de sistema confiável:")
    print("\nI- Disponibilidade é a característica que um sistema apresenta de estar pronto para uso quando acessado.")
    print("\nII-   Confiabilidade remete a uma característica presente nos sistemas quando são usados por períodos consideráveis de tempo sem apresentar defeitos.")
    print("\nIII- Um sistema é manutenível se, mesmo diante de uma falha, um estado de criticidade não é alcançado.")
    print("\nIV- Quando um sistema possui a facilidade em se consertar uma falha, isto é, falhas potenciais são previamente detectadas e imediatamente recuperadas, diz-se que tal sistema é seguro.")
    print("\nAgora, indique a alternativa CORRETA:\n")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    if r == "A":
        resp.append(r)
        r=A
        if r == rCorreta:
            pontos +=2
    elif r == "B":
        resp.append(r)
        r=B
    elif r == "C":
        resp.append(r)
        r=C
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao5()

print("============GABARITO============")
for i in range(0,5):
    print(gabarito[i])
print("============SUA PROVA============")
for i in range(0,5):
    print(resp[i])
print("Sua pontuação foi de: {}".format(pontos))