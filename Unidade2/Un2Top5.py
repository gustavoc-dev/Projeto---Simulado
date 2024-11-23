import os

gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "V – V – V – V. "
    B = "V – F – V – F."
    C = "V – F – F – V. "
    D = "F – V – F – V. "

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("1  Após o nascimento e o amadurecimento da computação, com o advento das redes de computadores, o surgimento dos sistemas distribuídos e o nascimento da internet, culmina-se na miniaturização dos equipamentos, sua integração, e o surgimento de um novo conceito de computação, a computação móvel e a computação ubíqua, e orbitando nesse ambiente a computação pervasiva. Sobre esses novos paradigmas avalie as sentenças:")
    print("\n(   ) Quando um usuário, levando consigo o seu celular, tablet, notebook, entre outros, está conectado a uma rede A e muda para uma rede B, e com isso leva com ele os serviços computacionais que usava na rede A, e consequentemente caracterizando que esses serviços tornam-se um elemento que pode ser movimentado entre redes a qualquer momento caracteriza o conceito fundamental da computação ubíqua.")
    print("\n(   ) Quando um usuário, levando consigo o seu celular, tablet, notebook, entre outros, está conectado a uma rede A e muda para uma rede B, e com isso leva com ele os serviços computacionais que usava na rede A, e consequentemente caracterizando que esses serviços tornam-se um elemento que pode ser movimentado entre redes a qualquer momento, caracteriza o conceito fundamental da computação móvel.")
    print("\n(   ) Quando um usuário, levando consigo o seu celular, tablet, notebook, entre outros, está conectado a uma rede A e muda para uma rede B, e com isso leva com ele os serviços computacionais que usava na rede A, e consequentemente caracterizando que esses serviços tornam-se um elemento que pode ser movimentado entre redes a qualquer momento caracteriza o conceito fundamental da computação pervasiva.")
    print("\n(   ) Imagine um ambiente de serviços computacionais (acesso a impressoras, serviços Wi-Fi, compartilhamento de mídias, entre outros) e que o mesmo seja totalmente transparente para quem o utiliza. Nesse ambiente, os dispositivos têm a capacidade de extrair informações desse ambiente e as utilizar na criação de novos modelos computacionais, isso caracteriza o conceito fundamental da computação pervasiva.")
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
    elif r == "D":
        resp.append(r)
        r=D
        if r == rCorreta:
            pontos +=2.5
    os.system("cls")
questao1()
def questao2():
    global pontos
    A = "As sentenças I e II estão corretas."
    B = "As sentenças III e IV estão corretas. "
    C = "A sentença III está incorreta e a sentença IV está correta."
    D = "A sentença I está correta e a sentença III está incorreta. "

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("1  O novo ambiente criado pela computação móvel, ubíqua e pervasiva lida, muitas vezes, com dispositivos que possuem recursos limitados (principalmente processamento e memória). Um outro aspecto relativo a essas limitações lida com o consumo de energia desses dispositivos. Com isso em mente, avalie as sentenças sobre as características desses dispositivos:")
    print("\nI-    O recurso para o consumo de energia dos dispositivos móveis é inversamente proporcional às suas velocidades de processamento e às suas capacidades de armazenamento. Dessa forma, uma melhoria no tocante ao consumo de energia não implicaria diretamente em um maior poder computacional desses dispositivos.")
    print("\nII-   O recurso para o consumo de energia dos dispositivos móveis é diretamente proporcional às suas velocidades de processamento e às suas capacidades de armazenamento. Dessa forma, uma melhoria no tocante ao consumo de energia implicaria diretamente em um maior poder computacional desses dispositivos.")
    print("\nIII- O ambiente da computação móvel trouxe à tona dispositivos como controladores e sensores. Os controladores respondem pela medição de valores físicos para fornecê-los a algum software (Sistema de Posicionamento Global, por exemplo), já os sensores obedecem aos softwares, afetando dessa forma o ambiente físico no qual se encontram.")
    print("\nIV- O ambiente da computação móvel trouxe à tona dispositivos como controladores e sensores. Os sensores respondem pela medição de valores físicos para fornecê-los a algum software (Sistema de Posicionamento Global, por exemplo), já os controladores obedecem aos softwares, afetando dessa forma o ambiente físico no qual se encontram.")
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
            pontos +=2.5
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao2()
def questao3():
    global pontos
    A = "A característica de um dispositivo pervasivo perceber que uma conexão não está mais disponível devido a um movimento desse dispositivo entre redes é conhecida como composição ad hoc."
    B = "A característica de um dispositivo pervasivo perceber que uma conexão não está mais disponível devido a um movimento desse dispositivo entre redes é conhecida como reconhecimento de compartilhamento como padrão."
    C = "A característica de um dispositivo pervasivo perceber que uma conexão não está mais disponível devido a um movimento desse dispositivo entre redes é conhecida como adoção de mudanças contextuais. Sendo que, a natureza desses sistemas não permite acesso e compartilhamento de informações entre os dispositivos conectados."
    D = "A característica de um dispositivo pervasivo perceber que uma conexão não está mais disponível devido a um movimento desse dispositivo entre redes é conhecida como adoção de mudanças contextuais."

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("3  Na computação pervasiva deve existir uma propriedade inerente aos dispositivos (sensores, controladores e outros) de ter consciência do ambiente ao qual pertencem, e por outro lado, esse ambiente precisa perceber tais dispositivos integrantes dele, isso garante que eles se integrem através de interações inteligentes entre si. Dessa forma, assinale a afirmação CORRETA sobre as características desse tipo de sistema:")
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
            pontos +=2.5
    os.system("cls")
questao3()
def questao4():
    global pontos
    A = "F – F – V – F. "
    B = "V – V – F – V. "
    C = "V – F – V – F. " 
    D = "F – V – F – V."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("4  Sabe-se que o novo ambiente criado pela computação móvel, ubíqua e pervasiva lida, muitas vezes, com dispositivos que possuem recursos limitados (principalmente processamento e memória). Sendo assim, nesse tipo de ambiente deve-se levar em consideração questões ligadas a segurança, principalmente a privacidade. Lembre-se que o tripé que fundamenta a segurança nos sistemas distribuídos é baseado na confidencialidade, integridade e disponibilidade. Sabendo disso, avalie as sentenças sobre os problemas de segurança em sistemas distribuídos, classificando V para as sentenças verdadeiras e F para as falsas:")
    print("\n\n(   ) A característica portátil dos dispositivos distribuídos (smartphones, sensores, controladores, tablets, entre outros) não representa um problema, pois não são facilmente roubados ou falsificados.")
    print("(   ) O item recurso computacional dos dispositivos distribuídos não é um fator relevante para ser considerado na construção de sistemas distribuídos, já que esses dispositivos podem ter embarcados em sua estrutura interna desde recursos para processamento de dados até aqueles que envolvem criptografia.")
    print("(   ) Consumir energia é um fator inerente a todo dispositivo eletrônico, seja ele distribuído ou não. Porém quando ele está associado ao processamento e armazenamento de dispositivos executando funções em ambientes distribuídos, converte-se em um item extremamente relevante e complexo.")
    print("(   ) Consumir energia é um fator inerente a todo dispositivo eletrônico, seja ele distribuído ou não. Porém quando ele está associado ao processamento e armazenamento de dispositivos executando funções em ambientes distribuídos, converte-se em um item extremamente relevante, porém simples de solucionar.")
    print("\n\nAgora, assinale a alternativa CORRETA:\n\n")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    if r == "A":
        resp.append(r)
        r=A
        if r == rCorreta:
            pontos +=2.5
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
questao4()

print("============GABARITO============")
for i in range(0,5):
    print(gabarito[i])
print("============SUA PROVA============")
for i in range(0,5):
    print(resp[i])
print("Sua pontuação foi de: {}".format(pontos))