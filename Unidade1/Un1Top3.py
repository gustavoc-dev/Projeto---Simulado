import os

gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "A arquitetura em camadas pode ser considerada uma versão mais aprimorada da estratégia presente na arquitetura monolítica, uma vez que no modelo em camadas cada uma oferece funcionalidades utilizadas apenas pelas camadas superiores. "
    B = "Uma máquina virtual é idêntica ao hardware verdadeiro; cada uma pode executar qualquer SO que seja executado diretamente no hardware básico. Diferentes VM podem executar diferentes SO. "
    C = "A arquitetura monolítica é a organização mais direta para a concepção de um SO, e a mais organizada e eficiente. Alguns autores a chamam de “estrutura simples”, porque o SO é construído com um conjunto de rotinas que podem ser chamadas umas pelas outras. "
    D = "Em uma arquitetura de microkemel o SO é reestruturado, retirando-se componentes não essenciais do kernel e adicionando-os como programas de nível de sistema e de usuário diminuindo assim o tamanho do kernel. "

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("1  Você aprendeu que o SO é um software de sistema responsável por realizar uma série de funções importantes para o funcionamento de um sistema computacional. As funções executadas pelo SO somente são possíveis porque são implementadas sobre um dado modelo de arquitetura, podendo ser: arquitetura monolítica, arquitetura em camadas, máquinas virtuais e arquiteturas microkernel. Sobre as diversas arquiteturas de um SO, assinale a alternativa INCORRETA:")
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
questao1()
def questao2():
    global pontos
    A = "A arquitetura possibilita a troca de informações entre os elementos computacionais, precisa estar relacionada ao objetivo e finalidade do SO, porém não tem relação com o quesito uso do computador mais amigável no tocante às necessidades do usuário final. "
    B = "A arquitetura prioriza a troca de informações entre os elementos computacionais, especialmente em nível da camada de interação com o hardware, deixando os aspectos relacionados à camada de interação com os sistemas aplicativos em um plano secundário."
    C = "A arquitetura possibilita a troca de informações entre os elementos computacionais, precisa estar relacionada ao objetivo e finalidade do SO, e torna o uso do computador mais amigável produzindo o efeito esperado para o usuário."
    D = "A arquitetura prioriza a troca de informações entre os elementos computacionais, especialmente em nível da camada de interação com os softwares aplicativos, deixando os aspectos relacionados à camada de interação com o hardware em um plano secundário."

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("2  O conceito de arquitetura perpassa pelo “[...] projeto geral de um sistema computacional e os inter-relacionamentos lógico e físico entre seus componentes”. Logo, o projeto eficiente de um SO está associado à escolha de uma arquitetura adequada às execuções de seus processos e serviços. Sobre a importância das arquiteturas para o projeto de um SO, assinale a alternativa CORRETA:")
    
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
            pontos +=2.5
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
    A = "Uma operação de E/S é realizada apenas em momentos específicos definidos pelo SO sem que um dado programa em execução requeira algum tipo de serviço ou acesso ao SO. Por essa razão, pela necessidade de um acesso a estas operações, o SO não pode deixar esse controle em nível de usuário."
    B = "Pode-se considerar quase uma regra geral que os processos criados pelos programas em execução sobre um SO necessitam trocar informações entre si. Esses processos, rodando em um ambiente de memória compartilhada ou em um ambiente interconectado por sistemas computacionais diferentes, podem necessitar trocar mensagens nesses ambientes."
    C = "Um SO carrega e executa um programa em memória apenas se houver garantias de que ele encerra de maneira normal, sem a necessidade de indicar se algum erro ocorreu."
    D = "Um SO trata alguns tipos de erros como falhas de hardware (CPU ou memória), erros gerados por operações de dispositivos de E/S, porém aqueles gerados pelos programas dos usuários são tratados exclusivamente por esses programas para que não haja sobrecarrega nas atividades do SO."

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("4  Um SO apresenta uma série de funções (serviços) que devem atender tanto às necessidades do usuário quanto permitir aos desenvolvedores programar suas tarefas de maneira mais fácil. Dessa forma, no contexto dessas funções, existem serviços com características bem específicas (operações de usuário e programas) executados pelos SO. Tendo isso em mente, assinale a alternativa CORRETA sobre esses serviços.")
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
            pontos +=2.5
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
    A = "Os SO sempre oferecem algum tipo interface de usuário, baseada em gráficos ou em apenas texto, com a função de executar comandos submetidos pelos usuários através de linha de comando, interface batch, interface gráfica de usuário, ou mesmo uma combinação dessas formas."
    B = "Um SO, normalmente, possui seu conceito de sistemas de arquivos baseados em arquivos e diretórios (pastas) físicos, aos quais são submetidas operações de criação, consulta, modificação e exclusão, incluindo a utilização de filtros de pesquisa sobre algumas dessas operações."
    C = "Uma outra função exercida pelo SO, porém não relacionada ao funcionamento eficiente do sistema, permite a contagem (quantidade e tipo) de recursos iniciados pelos usuários e seus processos. Essa função permite o gerenciamento dos recursos no tocante a sua liberação quando necessária, ou apenas para fins estatísticos, buscando uma melhor configuração e reconfiguração dos recursos do sistema." 
    D = "A alocação de recursos é, sem dúvida, um dos serviços mais essenciais presentes em um SO. O gerenciamento desse serviço permite a distribuição correta de recursos (processador, uso de memória principal e manipulação de arquivos, dispositivos de E/S, entre outros) aos processos dos usuários e do próprio sistema. E se idealizarmos ambientes mais complexos com múltiplos usuários e múltiplos recursos compartilhados, esse gerenciamento toma uma proporção ainda mais complexa e bem mais delicada."

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("5  Um SO apresenta uma série de funções (serviços) que devem atender tanto às necessidades do usuário quanto permitir aos desenvolvedores programar suas tarefas de maneira mais fácil. Dessa forma, além dessas funções, existem serviços com características bem mais específicas, associados à garantia de bom funcionamento do próprio sistema. Tendo isso em mente, assinale a alternativa CORRETA sobre esses serviços.")
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
    os.system("cls")
questao4()


print("============GABARITO============")
for i in range(0,5):
    print(gabarito[i])
print("============SUA PROVA============")
for i in range(0,5):
    print(resp[i])
print("Sua pontuação foi de: {}".format(pontos))