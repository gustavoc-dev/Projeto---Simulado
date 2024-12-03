import os

gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "V – V – F – F."
    B = "F – V – V – F."
    C = "F – F – V – V."
    D = "V – V – F – F."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("1  Um dos principais serviços que um sistema distribuído deve implementar, de maneira eficiente e eficaz, é, sem dúvida, os seus atributos de segurança. Isso deve ser alcançado através de técnicas, mecanismos e políticas que garantam uma visão segura para todos os recursos compartilhados no ambiente distribuído. Com isso em mente, avalie as sentenças relacionadas às visões de segurança classificando com V as sentenças verdadeiras e F as falsas:")
    print("\n(   )  No tocante à visão de comunicação, a segurança é alcançada utilizando uma autenticação entre as entidades que estão trocando as mensagens e tentando acessar os recursos do sistema.")
    print("\n(   )  A integridade e a confidencialidade de mensagens estão associadas à visão de autorização que uma entidade precisa possuir para usufruir de um determinado recurso.")
    print("\n(   )  A integridade e a confidencialidade de mensagens estão associadas à visão de autenticação que uma entidade precisa possuir para usufruir de um determinado recurso.")
    print("\n(   )  O estabelecimento de um canal de comunicação seguro com uma posterior validação de autorização para uma entidade pertencente a um ambiente distribuído caracterizam as duas visões apresentadas para a segurança para sistemas distribuídos.")
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
    rCorreta = D
    gabarito.append("D")

    print("2  A segurança de um sistema distribuído pode ser alcançada através de técnicas como a assinatura digital. Ela utiliza os atributos de integridade e de confidencialidade das mensagens, e de um canal de comunicação, para garantir os atributos de segurança. Sabendo disso, avalie a sentença de afirmação e a sentença de explicação relacionadas a essas duas características de segurança envolvidas na construção de sistemas distribuídos.")
    print("\nI-    “É importante que a segurança de recursos de informação possua, sem dispensar, características como a de confidencialidade (proteção contra exposição para pessoas não autorizadas) e integridade (proteção contra alteração ou dano)”")
    print("\nPORQUE")
    print("\nII-  “Em ambientes distribuídos, clientes e servidores enviam e recebem informações em mensagens por uma rede. Essa rede, que pode ser a internet, permite que um programa em um computador se comunique com um programa em outro computador, independentemente de sua localização, com inerentes riscos de segurança associados ao livre acesso a todos os recursos disponíveis”")
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
    elif r == "C":
        resp.append(r)
        r=C
    elif r == "D":
        resp.append(r)
        r=D
        if r == rCorreta:
            pontos +=2
    os.system("cls")
questao2()
def questao3():
    global pontos
    A = "As sentenças I e III estão corretas."
    B = "As sentenças II e IV estão corretas."
    C = "As sentenças I e II estão corretas."
    D = "As sentenças III e IV estão corretas."

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("3  Um dos principais serviços que um sistema distribuído deve implementar, de maneira eficiente e eficaz, é sem dúvida os seus atributos de segurança. Isso deve ser alcançado através de técnicas, mecanismos e políticas que garantam uma visão segura para todos os recursos compartilhados no ambiente distribuído. Dessa forma, avalie as sentenças relacionadas às visões de segurança:")
    print("\nI-    A integridade e a confidencialidade de mensagens não estão associadas a nenhuma das visões relacionadas à segurança em sistemas distribuídos, já que tratam de aspectos complementares relacionadas às mensagens trocadas entre as entidades presentes no sistema.")
    print("\nII-   Garantir a integridade e a confidencialidade de mensagens, juntamente com uma posterior validação de autorização das entidades comunicantes, fazem parte das visões de segurança presentes na implementação de ambientes distribuídos.")
    print("\nIII-  O estabelecimento de um canal de comunicação seguro com uma posterior validação da integridade e da confidencialidade de mensagens, caracterizam as duas visões apresentadas para a segurança para sistemas distribuídos.")
    print("\nIV-  O controle que os processos possuem sobre os seus recursos associados a um sistema distribuído está relacionado à visão de autorização presente na segurança desse sistema.")
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
        if r == rCorreta:
            pontos +=2
    elif r == "C":
        resp.append(r)
        r=C
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao3()
def questao4():
    global pontos
    A = "V – V – F – V."
    B = "F – V – F – V."
    C = "F – F – V – V."
    D = "F – F – V – F."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("4  A segurança de um sistema distribuído pode ser alcançada através de técnicas como a assinatura digital. Ela utiliza os atributos de integridade e de confidencialidade das mensagens, e de um canal de comunicação, para garantir os atributos de segurança. Com isso em mente, avalie as sentenças relacionadas a esses atributos de segurança classificando com V as sentenças verdadeiras e com F aquelas que são falsas:")
    print('\n(   )  Um atributo de uma mensagem deve ser um encapsulamento de proteção que evite sua apresentação às entidades sem esse direito de visualização.')
    print("\n(   )  Um atributo de uma mensagem deve ser um encapsulamento de proteção que evite sua modificação, ou estrago, por entidades sem esse direito de modificação.")
    print("\n(   )  Confidencialidade e integridade de mensagens são atributos de segurança opcionais aos sistemas distribuídos, uma vez que na internet, por exemplo, um servidor pode possuir uma senha de acesso criada por algoritmos de criptografia confiáveis que, por si só, diminuiriam os riscos de acessos não autorizados aos recursos distribuídos desse servidor.")
    print("\n(   )  Confidencialidade e integridade de mensagens são atributos de segurança indispensáveis aos sistemas distribuídos, uma vez que na internet, por exemplo, mesmo que um servidor possua uma senha de acesso criada por algoritmos de criptografia confiáveis, isso por si só, não diminuiria os riscos de acessos não autorizados aos recursos distribuídos desse servidor.")
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
questao4()
def questao5():
    global pontos
    A = "F – V – F – F."
    B = "V – V – F – V."
    C = "F – V – V – F." 
    D = "V – F – V – F."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("5  Políticas e mecanismos de segurança são elementos fundamentais para se implementar serviços de segurança em ambientes distribuídos. E, que apesar de relacionados, possuem conceitos e utilização distintos. Com isso em mente, avalie as sentenças relacionadas aos conceitos de política e mecanismos de segurança classificando com V as sentenças verdadeiras e F as falsas:")
    print("\n(   )  Uma das garantias para os requisitos de segurança de um sistema distribuídos é a criação de mecanismos de segurança viabilizados com a utilização das políticas de segurança.")
    print("\n(   )  Uma das garantias para os requisitos de segurança de um sistema distribuídos é a criação de políticas de segurança viabilizados com a utilização dos mecanismos de segurança.")
    print("\n(   )  Recursos lógicos (serviços e dados, por exemplo), usuários e recursos físicos (máquinas equipamentos em geral) são descritos por operações precisas que podem realizar e quais dessas operações podem ser opcionais. A definição dessas operações caracteriza uma política (ou políticas) de segurança.")
    print("\n(   )  Recursos lógicos (serviços e dados, por exemplo), usuários e recursos físicos (máquinas equipamentos em geral) são descritos por operações precisas que podem realizar e quais dessas operações podem ser opcionais. A definição dessas operações caracteriza um mecanismo (ou mecanismos) de segurança.")
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