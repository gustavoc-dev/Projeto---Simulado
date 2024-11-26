import os

gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "V – F – F – V."
    B = "F – V – V – F."
    C = "F – V – F – V."
    D = "V – F – V – F."

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("1  Está claro que os sistemas distribuídos precisam das redes de computadores, ou até mesmo redes de dispositivos, para o seu funcionamento. Além de elas oferecerem uma infraestrutura de conectividade, também oferecem uma infraestrutura de comunicação para as entidades envolvidas nas trocas de mensagens no ambiente distribuído. Com isso em mente, avalie as sentenças relacionadas aos protocolos de comunicação classificando com V as sentenças verdadeiras e F as falsas:")
    print("\n(   )  Nas trocas de mensagens em um ambiente distribuído, as entidades (nodos) envolvidas nessa troca, ora podem se comportar como emissores, e ora podem se comportar como receptores.")
    print("\n(   )  O caminho que as mensagens percorrem nas camadas de protocolos é diferente nos sistemas distribuídos quando comparadas aos sistemas tradicionais cliente/servidor devido a sua natureza mais complexa.")
    print("\n(   )  O caminho que as mensagens percorrem nas camadas de protocolos é a mesma nos sistemas distribuídos quando comparadas aos sistemas tradicionais cliente/servidor independentemente de sua natureza mais complexa.")
    print("\n(   )  Nas trocas de mensagens em um ambiente distribuído, as entidades (nodos) envolvidas nessa troca, quem atua como emissor sempre será um emissor, e da mesma forma quem se comporta como receptor sempre será um receptor.")
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
            pontos +=2
    os.system("cls")
questao1()
def questao2():
    global pontos
    A = "V – V – V – F."
    B = "V – F – F – V."
    C = "F – V – V – V."
    D = "V – F – V – F."

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("2  Nos ambientes de sistemas distribuídos não há como processos serem executados, ou recursos serem acessados sem o envio/recebimento de pacotes, e, para isso, as entidades lançam mão de duas operações básicas envio e recebimento. Com isso em mente, avalie as sentenças relacionadas ao conceito de sincronização classificando com V as sentenças verdadeiras e F as falsas:")
    print("\n(   )  Na comunicação síncrona uma ação de impedimento, nas operações básicas (send/recieve), impede as ações da entidade origem da mensagem até que sua requisição seja aceita.")
    print("\n(   )  As comunicações síncrona e assíncrona possuem características semelhantes independentes da natureza de comunicação exigida por um recurso distribuído (serviço, aplicação etc.) quando da solicitação desse recurso por uma entidade emissora e a resposta dada por uma entidade receptora. Dessa forma, toda comunicação síncrona pode ser assíncrona e vice-versa.")
    print("\n(   )  Na comunicação assíncrona uma ação de impedimento nas operações básicas (send/recieve), impede as ações da entidade origem da mensagem até que sua requisição seja aceita.")
    print("\n(   )  As comunicações síncrona e assíncrona dependem da natureza de comunicação exigida por um recurso distribuído (serviço, aplicação etc.) quando da solicitação desse recurso por uma entidade emissora e a resposta dada por uma entidade receptora.")
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
    A = "As sentenças I e III estão corretas."
    B = "As sentenças II e IV estão corretas."
    C = "As sentenças I e II estão corretas."
    D = "As sentenças III e IV estão corretas."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("3  Está claro que os sistemas distribuídos precisam das redes de computadores, ou até mesmo redes de dispositivos, para o seu funcionamento. Além de elas oferecerem uma infraestrutura de conectividade, também oferecem uma infraestrutura de comunicação para as entidades envolvidas nas trocas de mensagens no ambiente distribuído. Com isso em mente, avalie as sentenças relacionadas aos protocolos de comunicação:")
    print("\nI-     Os protocolos de comunicação são responsáveis por garantir que uma mensagem enviada por uma entidade emissora seja recebida pela entidade receptora.")
    print("\nII-   Nas camadas do modelo OSI, em número de 7, as camadas mais baixas são mais próximas das aplicações dos usuários e as camadas mais altas mais próximas dos meios físicos da rede.")
    print("\nIII-  Os protocolos de comunicação são organizados logicamente em camadas sobrepostas uma a outra, na qual cada uma delas possui um conjunto de regras específicas para a recepção, tratamento e repasse de uma mensagem para outra camada.")
    print("\nIV-  Nas camadas do modelo OSI, em número de 5, as camadas mais baixas representam camadas mais próximas dos meios físicos das redes e as mais altas mais próximas das aplicações dos usuários.")
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
questao3()
def questao4():
    global pontos
    A = "As sentenças I e III estão corretas."
    B = "As sentenças II e IV estão corretas."
    C = "As sentenças II e III estão corretas."
    D = "As sentenças III e IV estão corretas."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("4  Nos ambientes de sistemas distribuídos não há como processos serem executados, ou recursos serem acessados sem o envio/recebimento de pacotes, e, para isso, as entidades lançam mão de duas operações básicas, envio e recebimento. Com isso em mente, avalie as sentenças relacionadas ao conceito de sincronização:")
    print('\nI-    Na comunicação síncrona as entidades emissora e receptora trocam mensagens sem a necessidade de um evento de impedimento, logo, uma operação de envio não impede a entidade emissora de continuar enviando transmissões à entidade receptora.')
    print("\nII-   Na comunicação assíncrona as entidades emissora e receptora trocam mensagens sem a necessidade de um evento de impedimento, devido à utilização de um repositório intermediário (buffer) no qual as mensagens são armazenadas.")
    print("III- Na comunicação assíncrona as entidades emissora e receptora trocam mensagens sem a necessidade de um evento de impedimento, logo, uma operação de envio não impede a entidade emissora de continuar enviando transmissões à entidade receptora.")
    print("\nIV- Na comunicação síncrona, ou mesmo na assíncrona, as mensagens das entidades emissoras são produzidas sem a interferência de eventos de impedimento, logo, as operações de envio e de recebimento não são influenciadas por esse tipo de evento.")
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
    A = "As sentenças I e II representam proposições verdadeiras, mas a II não é uma justificativa correta da I."
    B = "As sentenças I e II não representam proposições verdadeiras."
    C = "A sentenças I é uma proposição verdadeira, porém a II é uma proposição falsa." 
    D = "As sentenças I e II representam proposições verdadeiras, e a II é uma justificativa correta da I."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("5  Nos ambientes de sistemas distribuídos não há como processos serem executados, ou recursos serem acessados sem o envio/recebimento de pacotes, e, para isso, as entidades lançam mão de duas operações básicas, envio e recebimento, sendo que esse envio/recebimento deve ser transparente, isto é, como se ele estivesse acontecendo localmente. Dessa forma, avalie a sentença de afirmação e a sentença de explicação relacionadas ao modelo de comunicação RPC envolvido na construção de sistemas distribuídos.")
    print("\nI-    O modelo RPC tem como objetivo tornar o mais transparente possível as chamadas remotas como se fossem chamadas a serviços, ou recursos, locais. Isso deve ocorrer sem que haja qualquer distinção na sintaxe de parâmetros entre uma chamada de procedimento local e um remoto.")
    print("\nPORQUE\n")
    print("II-  Em um ambiente distribuído um defeito, erro ou falha, podem ocorrer e comprometer a eficiência, e eficácia, isto é, o próprio comportamento do sistema. Logo, o sistema deve ser o que se chama de tolerante a esses eventos como forma de manter a qualidade de execução de seus serviços.")
    print("\nAgora, assinale a alternativa que apresenta a resposta CORRETA:\n")
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