#2.1 - REPRESENTAÇÃO DO TABULEIRO

#função 2.1.1 que analiza se o argumento corresponde a um tabuleiro
def eh_tabuleiro(arg):
    """
    Analiza se o argumento corresponde a um tablueiro válido

    Um tablueiro válido é um tuplo formado formado por tuplos onde:
    - Cada elemento do tuplo principal é um tuplo
    - O tabuleiro deve ter entre 2 a 100 linhas
    - Todas as linhas devem ter o mesmo número de colunas
    - Cada linha deve ter entre 2 a 100 colunas
    - Cada elemento dentro dos tuplos dentro do tuplo principal devem ser -1, 1 ou 0

    Parâmetro:
    - arg: qualquer tipo de dado que será verificado se corresponde a um tabuleiro válido

    Retorna:
    - True, se o argumento for um tabulerio válido
    - False, caso contrário
    """
    #analiza se o argumento é um tuplo
    if type(arg) != tuple:
        return False
    
    #analiza quantos tuplos tem o tuplo principal
    def contem_tuplos(tuplo):
        contador_tuplos = 0
        for elemento in tuplo:
            if type(elemento) == tuple:
                contador_tuplos += 1
        return contador_tuplos

    #define os limites que o tabuleiro pode ter
    if  contem_tuplos(arg) >= 2 and contem_tuplos(arg) <= 100:
        n_colunas = len(arg[0])                       #armazena o tamanho do 1º tuplo 
        for tuplo_interno in arg:
            if type(tuplo_interno) != tuple:          #analiza se é um tuplo o que está dentro do tuplo principal
                return False
            if len(tuplo_interno) < 2 or len(tuplo_interno) > 100: #analiza o comprimento dos tuplos
                return False
            if len(tuplo_interno) != n_colunas:       #analiza se todos os tuplos têm o mesmo tamanho
                return False
            if tuplo_interno == ():                   #analiza se algum tuplo está vazio
                return False
            for el in tuplo_interno:
                if type(el) != int:                   #analiza se todos os tuplos são formadas por números inteiros
                    return False
                if el not in (1, 0, -1):              #analiza se todos os valores representam uma posição válida no tabuleiro
                    return False
        return True
    
    return False                                      #returna falso caso o tuplo tenha menos de 2 ou mais de 100 tuplos dentro do mesmo

#funçao 2.1.2 que analiza se o argumento corresponde a uma posição de um tabuleiro
def eh_posicao(arg):
    """
    Analiza se o argumento corresponde a uma posição de um tabuleiro

    Uma posição válida é representada por um número inteiro positivo, maior que 0 e menor a igual a 10000

    Parâmetro:
    - arg: qualquer tipo de dado que será verificado se corresponde a uma posição válida

    Retorna:
    - True, se o argumento for uma posição válida
    - False, caso contrário
    """
    #analiza se o argumento é um inteiro
    if type(arg) != int:
        return False

    if 0 < arg <= 10000:
        return True
    else:
        return False

#função que calcula o comprimento de uma linha ou o número de colunas
def n_colunas(tuplo):
    """
    Calcula o número de colunas de um tabuleiro, ou seja, o seu comprimento

    Parâmetro:
    - tuplo (tup): O tabuleiro válido que é um tuplo de tuplos

    Retorna:
    - O número de colunas
    """
    return len(tuplo[0])

#função que calcula a altura de uma coluna ou o número de linhas
def n_linhas(tuplo):
    """
    Calcula o número de linhas de um tabuleiro, ou seja, a sua altura

    Parâmetro:
    - tuplo (tup): O tabuleiro válido que é um tuplo de tuplos

    Retorna:
    - O número de linhas 
    """
    return len(tuplo)

#função 2.1.3 que devolve um tuplo com o número de linhas(m) e colunas(n) de um tabuleiro
def obtem_dimensao(tab):
    """
    Obtém as dimensões do tabuleiro

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos

    Retorna:
    - Um tuplo que contem duas informações: o número de linhas (m) e o número de colunas (n) do tabuleiro 
    """
    m = n_linhas(tab)
    n = n_colunas(tab)
    return (m, n)

#função 2.1.4 que devolve o valor contido numa posição
def obtem_valor(tab, pos):
    """
    Calcula o valor de uma posição específica do tabuleiro

    Parâmetros:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - pos (int): A posição do tabuleiro (um número entre 1 e o número total de casas)

    Retorna:
    - O valor contido na posição inserida
    """
    pos = pos - 1                                     #retiramos 1 porque em python o indice começa em 0 e não em 1 como no nosso jogo
    n = n_colunas(tab)
    linha = pos // n                                  #determina a linha em que está situada
    coluna = pos % n                                  #determina a coluna em que está situado
    return tab[linha][coluna]

#função 2.1.5 que devolve por ordem crescente todas as posições pertencentes à mesma coluna
def obtem_coluna(tab, pos):
    """
    Devolve por ordem crescente todas as posições pertencentes à mesma coluna da posição inserida

    Parâmetros:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - pos (int): A posição do tabuleiro (um número entre 1 e o número total de casas)

    Retorna:
    - Um tuplo com todas as posições pertencentes à mesma coluna da posição inserida, por ordem crescente
    """
    comp = n_colunas(tab)
    alt = n_linhas(tab)
    res = []
    if 0 < pos <= comp:                               #guarda a posiçao inicial do tabuleiro caso esta pertença a 1º linha
        n_inicial = pos
    while not 0 < pos <= comp:                        #acha a posição correspondente na 1º linha caso a posição inserida não pertença a esta
        pos -= comp
        n_inicial = pos
    while pos < ((comp * alt - (comp - n_inicial)) + 1):
        res += [pos]
        pos += comp

    return tuple(res)

#função 2.1.6 que devolve por ordem crescente todas as posições pertencestes à mesma linha
def obtem_linha(tab, pos):
    """
    Devolve por ordem crescente todas as posições pertencentes à mesma linha da posição inserida

    Parâmetros:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - pos (int): A posição do tabuleiro (um número entre 1 e o número total de casas)

    Retorna:
    - Um tuplo com todas as posições pertencentes à mesma linha da posição inserida, por ordem crescente
    """
    res = ()
    pos -= 1
    n = n_colunas(tab)
    linha = pos // n                                  #determina a linha em que está situada
    for i in range(1, (n + 1)):
        comprimento = n * linha
        num = i + comprimento
        res += (num,)
    
    return res

#função 2.1.7 que devolve um tuplo formado por dois tuplos correspondentes à diagonal e antidiagonal
def obtem_diagonais(tab, pos):
    """
    Devolve por ordem crescente todas as posições pertencentes à diagonal e à antidiagonal da posição inserida

    Parâmetros:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - pos (int): A posição do tabuleiro (um número entre 1 e o número total de casas)

    Retorna:
    - Um tuplo formado por dois tuplos:
        - O primeiro tuplo contém as posições da diagonal, por ordem crescente
        - O segundo tuplo contém as posições da antidiagonal, por ordem decrescente
    """
    m = n_linhas(tab)
    n = n_colunas(tab)
    pos -= 1
    linha = pos // n                                  #determina a linha em que está situada
    coluna = pos % n                                  #determina a coluna em que está situado
    diagonal, antidiagonal = [], []

    #determinar a diagonal
    lin, col = linha, coluna
    while lin >= 0 and col >= 0:                      #calcula todas as posições para cima e para a esquerda da inserida
        diagonal += [lin * n + col + 1]
        lin -= 1
        col -= 1
    lin, col = linha + 1, coluna + 1
    while lin < m and col < n:                        #calcula todas as posições para baixo e para a direita da inserida
        diagonal += [lin * n + col + 1]
        lin += 1
        col += 1

    #determinar a antidiagonal
    lin, col = linha, coluna
    while lin >= 0 and col < n:                       #calcula todas as posições para cima e para a direita da inserida
        antidiagonal += [lin * n + col + 1]
        lin -= 1
        col += 1
    lin, col = linha + 1, coluna - 1
    while lin < m and col >= 0:                       #calcula todas as posições para baixo e para a esquerda da inserida
        antidiagonal += [lin * n + col + 1]
        lin += 1
        col -= 1
    
    diag = sorted(diagonal)                           #ordena por ordem crescente os números referentes às posições
    antidiag = sorted(antidiagonal, reverse=True)     #ordena por ordem decrescente os números referentes às posições
    
    return (tuple(diag), tuple(antidiag))

#função 2.1.8 que devolve uma cadeia de caracteres que representa o tabuleiro
def tabuleiro_para_str(tab):
    """
    Converte um tabuleiro (representado por um tuplo de tuplos) em uma cadeia de caracteres

    A função transforma o tabuleiro numa representação gráfica onde:
    - O valor "-1" (2º jogador) é representado por "O"
    - O valor "1" (1º jogador) é representado por "X"
    - O valor "0" "espaço livre) é representado por "+"
    - As casas jogáveis são separadas por "---"
    - As linhas do tabuleiro são separadas por uma linha de "|"

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos

    Retorna:
    - Uma string que representa graficamente o tabuleiro
    """
    res = ""

    #converte os números para os símbolos correspondentes 
    def transforma(num):
        """
        Converte os números que representam os jogadores e o espaço vazio para os símbolos correspondentes

        Parâmetro:
        - num (int): O número de uma posição do tabuleiro

        Retorna:
        - Uma string que equivale ao número ("X" = 1, "O" = -1, "+" = 0)
        """
        if num == 1:                                  #transforma o 1(1º jogador) em X
            return "X"
        elif num == 0:                                #transofrma o 0(espaço livre) em +
            return "+"
        elif num == -1:                               #transforma o -1(2º jogador) em O
            return "O"
            
    #converte todas os tuplos, exceto o último, que representam linhas de tabuleiro para os símbolos correspondentes
    for i in tab[:-1]:
        sep = "|"
        res += f"{transforma(i[0])}"                  #converte a primeira posição de cada linha, menos a última para o seu símbolo correspondente

        for num in i[1:]:
            res += f"---{transforma(num)}"            #adiciona 3 traços para separar cada posição do tabuleiro
            sep += "   |"                             #atualiza os | para ficarem com as distâncias certas

        res += f"\n{sep}\n"                           #adiciona as |
    
    res += f"{transforma(tab[-1][0])}"                #converte a primeira posição da última linha para o seu símbolo correspondente

    #converte os outros valores da última linha          
    for num in tab[-1][1:]:
        res += f"---{transforma(num)}"

    return res                                        #retorna o tabuleiro

#2.2 - FUNÇÕES DE INSPEÇÃO E MANIPULAÇÃO DO TABULEIRO

#função 2.2.1 que analiza se posição inserida corresponde a uma posição do tabuleiro
def eh_posicao_valida(tab, pos):
    """
    Analiza se a posição inseirda correponde a uma posição válida

    Uma posição é válida quando:
    - Está dentro dos limites do tabuleiro

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - pos (int): A posição do tabuleiro (um número entre 1 e o número total de casas)

    Retorna:
    - True, se a posição for válida no tabuleiro
    - False, caso contrário

    Levanta:
    - ValueError: Caso o tabuleiro ou a posição não sejam válidos
    """
    #gera os erros associados aos argumentos inseridos
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError("eh_posicao_valida: argumentos invalidos")

    dimensao = obtem_dimensao(tab)                    #utiliza a função 2.1.3 para achar quantas linhas e colunas tem o tabuleiro
    area = dimensao[0] * dimensao[1]                  #calcula o número de casas que o tabuleiro tem
    if pos <= area:
        return True
    else:
        return False 

#função 2.2.2 que analiza se a posição inserida corresponde a uma posição livre
def eh_posicao_livre(tab, pos):
    """
    Analiza se a posição inseirda correponde a uma posição livre

    Uma posição diz-se livre quando o seu valor é 0, ou seja, não está ocupada por nenhum jogador

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - pos (int): A posição do tabuleiro (um número entre 1 e o número total de casas)

    Retorna:
    - True, se a posição estiver livre
    - False, caso contrário

    Levanta:
    - ValueError: Caso o tabuleiro ou a posição não sejam válidos
    """
    #gera os erros associados aos argumentos inseridos
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos):
        raise ValueError("eh_posicao_livre: argumentos invalidos")
    
    #utiliza a função 2.1.4 para ler o valor de cada posição 
    if obtem_valor(tab, pos) == 0:
        return True
    else:
        return False

#função 2.2.3 que devolve por ordem crescente todas as posições livres do tabuleiro
def obtem_posicoes_livres(tab):
    """
    Devole por ordem crescente todas as posições livres do tabuleiro

    Uma posição diz-se livre quando o seu valor é 0, ou seja, não está ocupada por nenhum jogador

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos

    Retorna:
    - Um tuplo que contém todas as posições livres do tabuleiro por ordem crescente

    Levanta:
    - ValueError: Caso o tabuleiro não seja válido
    """
    #gera um erro com base na função eh_tabuleiro (função 2.1.1 que analiza se o argumento corresponde a um tabuleiro)
    if not eh_tabuleiro(tab):
        raise ValueError("obtem_posicoes_livres: argumento invalido")
    
    res = ()
    n_posicoes = n_linhas(tab) * n_colunas(tab)
    for i in range(1, (n_posicoes + 1)):
        if eh_posicao_livre(tab, i):          #utiliza a função 2.2.2 para achar as posições livres
            res += (i,)

    return res

#função 2.2.4 que devolve um tuplo com todas as posições ocupados por um jogador
def obtem_posicoes_jogador(tab, jog):
    """
    Devole todas as posições do tabuleiro ocupados por um jogador

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - jog (int): O jogador, sendo "1" referente ao 1º jogador e "-1" referente ao 2º jogador

    Retorna:
    - Um tuplo que contém todas as posições do tabuleiro ocupadas por um jogador

    Levanta:
    - ValueError: Caso o tabuleiro não seja válido ou o valor do jog não seja 1 ou -1
    """
    #gera os erros associados aos argumentos inseridos
    if not eh_tabuleiro(tab) or type(jog) != int or jog not in (1, -1):
        raise ValueError("obtem_posicoes_jogador: argumentos invalidos")

    res = ()
    n_posicoes = n_linhas(tab) * n_colunas(tab)
    for i in range(1, (n_posicoes + 1)):
        if obtem_valor(tab, i) == jog:                 #utiliza a função 2.1.4 para ler o valor de cada posição 
            res += (i,)

    return res

#função 2.2.5 que devolve um tuplo por ordem crescente com todas as posições adjacentes (horizontal, vertical e diagonal) à inserida
def obtem_posicoes_adjacentes(tab, pos):
    """
    Devole um tuplo com todas as posições adjacentes (horizontal, vertical e diagonal) à inserida

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - pos (int): A posição do tabuleiro (um número entre 1 e o número total de casas)

    Retorna:
    - Um tuplo que contém todas as posições adjacentes do tabuleiro por ordem crescente

    Levanta:
    - ValueError: Caso o tabuleiro ou a posição não sejam válidos
    """
    #gera os erros associados aos argumentos inseridos
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos):
        raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")

    col = obtem_coluna(tab, pos)                      #utiliza a função 2.1.5 para obter todas as posições da coluna da posição inserida
    lin = obtem_linha(tab, pos)                       #utiliza a função 2.1.6 para obter todas as posições da linha da posição inserida
    diag = obtem_diagonais(tab, pos)                  #utiliza a função 2.1.7 para obter todas as posições das diagonais da posição inserida
    res = []
    
    #encontra a posição inserida na coluna
    for i in range(len(col)):
        if  col[i] == pos:
            if i > 0:                                 #adiciona ao tuplo a posição acima da inserida, caso exista
                res.append(col[i - 1])
            if i < len(col) - 1:                      #adiciona ao tuplo a posição abaixo da inserida, caso exista
                res.append(col[i + 1])
    
    #encontra a posição inserida na linha
    for i in range(len(lin)):
        if lin[i] == pos:
            if i > 0:                                 #adiciona ao tuplo a posição à esquerda da inserida, caso exista
                res.append(lin[i - 1])
            if i < len(lin) - 1:                      #adiciona ao tuplo a posição à direita da inserida, caso exista
                res.append(lin[i + 1])

    #encontra a posição na diagonal
    for i in range(len(diag[0])):
        if i < len(diag[0]) and diag[0][i] == pos:
            if i > 0:                                 #adiciona ao tuplo a posição acima e à esquerda da inserida, caso exista
                res.append(diag[0][i - 1])
            if i < len(diag[0]) - 1:                  #adiciona ao tuplo a posição abaixo e à direita da inserida, caso exista
                res.append(diag[0][i + 1])

    #encontra a posição na antidiagonal
    for i in range(len(diag[1])):
        if i < len(diag[1]) and diag[1][i] == pos:
            if i > 0:                                 #adiciona ao tuplo a posição abaixo e à esquerda da inserida, caso exista
                res.append(diag[1][i - 1])
            if i < len(diag[1]) - 1:                  #adiciona ao tuplo a posição acima e à direita da inserida, caso exista
                res.append(diag[1][i + 1])

    res = sorted(res)                                 #ordena as posições por ordem crescente

    return tuple(res)                                 #retorna todas as posições adjacentes em forma de tuplo

#função 2.2.6 que devolve um tuplo com as posições por ordem crescente de distância ao centro do tabuleiro
def ordena_posicoes_tabuleiro(tab, tup):
    """
    Ordena um tuplo de posições por ordem crescente de distância ao centro do tabuleiro

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - tup (tup): Um tuplo que contém as posições que vão ser ordenadas

    Retorna:
    - Um tuplo que contém todas as posições ordenadas pela distância ao centro do tabuleiro, e caso tenham as mesma distância, por ordem crescente

    Levanta:
    - ValueError: Caso o tabuleiro ou as posições inseridas não sejam válidas ou o tup não seja um tuplo e/ou tenha mais posições que o tabuleiro
    """
    #gera os erros associados aos argumentos inseridos
    if not eh_tabuleiro(tab) or type(tup) != tuple or (n_colunas(tab) * n_linhas(tab)) < len(tup):
        raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")

    for i in range(len(tup)):

        #gera os erros associados aos argumentos inseridos
        if not eh_posicao(tup[i]) or not eh_posicao_valida(tab, tup[i]):
            raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
    
    m = len(tab)
    n = len(tab[0])
    centro = (m // 2) * n + n // 2 + 1                #determina o centro do tabuleiro
    linha_c = (centro - 1) // n                       #determina a linha em que está situado o centro do tabuleiro
    coluna_c = (centro - 1) % n                       #determina a coluna em que está situado o centro do tabuleiro
    res = []
    adj = obtem_posicoes_adjacentes(tab, centro)      #utiliza a função 2.2.5 para obter todas as posições a uma distância de 1 ao centro

    #função para calcular a distância de uma posição ao centro
    def distancia_ao_centro(pos):
        """
        Calcula a distância de uma posição ao centro do tabuleiro

        Parâmetro:
        - pos (int): A posição do tabuleiro (um número entre 1 e o número total de casas)

        Retorna:
        - Um número inteiro que representa a distância da posição ao centro
        """
        linha_pos = (pos - 1) // n                    #determina a linha em que está situado uma posição
        coluna_pos = (pos - 1) % n                    #determina a coluna em que está situado uma posição
        return max(abs(linha_pos - linha_c), abs(coluna_pos - coluna_c))

    #determina todas as posições com uma distância ao centro de 0 ou 1
    for i in tup:
        if i == centro:                               #mete em primeiro lugar no tuplo a posição que corresponde o centro
            res = [i] + res
        
        for c in range(len(adj)):
            if i == adj[c]:                           #mete, depois da posição do centro, todas as posições com uma distância de 1 ao centro
                res += [i]
    
    #determina todas as posições com uma distância ao centro de 2 ou mais
    for i in tup:
        if distancia_ao_centro(i) >= 2 and i not in adj:
            res += [i]

    #mete as posições com 2 ou mais de distância ao centro por ordem de distância ao mesmo e os com a mesma distância por ordem crescente 
    res = sorted(res, key=lambda pos: (distancia_ao_centro(pos), pos))

    return tuple(res)                                 #retorna todas as posições adjacentes em forma de tuplo

#função 2.2.7 que devolve um tabuleiro com uma nova pedra do jogador indicado na posição inserida
def marca_posicao(tab, pos, jog):
    """
    Atualiza o tabuleiro com a jogada de um jogador em uma posição inserida por este

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - pos (int): A posição do tabuleiro (um número entre 1 e o número total de casas)
    - jog (int): O jogador, sendo "1" referente ao 1º jogador e "-1" referente ao 2º jogador

    Retorna:
    - Um novo tabuleiro com a jogada aplicada

    Levanta:
    - ValueError: Caso o tabuleiro ou a posição inserida não sejam válidos ou se a posição já estiver ocupada ou o valor do jog não seja 1 ou -1
    """
    #gera os erros associados aos argumentos inseridos
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos) or not eh_posicao_livre(tab, pos) \
     or type(jog) != int or jog not in (1, -1):
        raise ValueError("marca_posicao: argumentos invalidos")

    res = []
    linha = (pos - 1) // n_colunas(tab)               #determina a linha em que está situado uma posição
    coluna = (pos - 1) % n_colunas(tab)               #determina a coluna em que está situado uma posição

    for i in range(len(tab)):
        nova_linha = []
        for c in range(len(tab[i])):
            if i == linha and c == coluna:
                nova_linha.append(jog)                #altera o valor da posição inserida
            else:
                nova_linha.append(tab[i][c])          #junta os valores das posições não selecionadas
        res.append(tuple(nova_linha))

    #faz com que o tuplo volte a ser constituido por vários tuplos em que cada um representa uma linha do tabuleiro
    final = tuple(res)

    return final

#função 2.2.8 que analiza se existe uma linha, que contem a posição inserida, que tenha k ou mais pedras consecutivas do mesmo jogador
def verifica_k_linhas(tab, pos, jog, k):
    """
    Analiza se existe uma linha, que contem a posição inserida, que tenha k ou mais pedras consecutivas do mesmo jogador

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - pos (int): A posição do tabuleiro (um número entre 1 e o número total de casas)
    - jog (int): O jogador, sendo "1" referente ao 1º jogador e "-1" referente ao 2º jogador
    - k (int): O número mínimo de peças consecutivas que o jogador tem de ter

    Retorna:
    - True, se existir uma sequencia de k ou mais peças consecutivas do jogador
    - False, caso contrário

    Levanta:
    - ValueError: Caso algum dos argumentos fornecidos for inválido
    """
    #gera os erros associados aos argumentos inseridos
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos) or \
     type(jog) != int or jog not in (1, -1) or type(k) != int or k <= 0:
        raise ValueError("verifica_k_linhas: argumentos invalidos")
    
    col = obtem_coluna(tab, pos)                      #utiliza a função 2.1.5 para obter todas as posições da coluna da posição inserida
    lin = obtem_linha(tab, pos)                       #utiliza a função 2.1.6 para obter todas as posições da linha da posição inserida
    dig = obtem_diagonais(tab, pos)                   #utiliza a função 2.1.7 para obter todas as posições das diagonais da posição inserida
    contador_l, contador_c, contador_d, contador_ad = 0, 0, 0, 0

    #verifica se a peça da posição inserida corresponde ao jogador inserido
    if jog != obtem_valor(tab, pos):
        return False

    #verifica se existe k posições consecutivas do mesmo jogador na coluna da posição inserida 
    for i in range(len(col)):
        if obtem_valor(tab, col[i]) == jog:
            contador_c += 1                           #adiciona 1 caso o valor da posição represente uma posição do jogador inserido
            if contador_c >= k and pos in col[i - k + 1:i + 1]:
                return True
        else:
            contador_c = 0                            #reseta o contador caso duas posições consecutivas não sejam do mesmo jogador

    #verifica se existe k posições consecutivas do mesmo jogador na linha da posição inserida
    for i in range(len(lin)):
        if obtem_valor(tab, lin[i]) == jog:
            contador_l += 1                           #adiciona 1 caso o valor da posição represente uma posição do jogador inserido
            if contador_l >= k and pos in lin[i - k + 1:i + 1]:
                return True
        else:
            contador_l = 0                            #reseta o contador caso duas posições consecutivas não sejam do mesmo jogador

    #verifica se existe k posições consecutivas do mesmo jogador na diagonal da posição inserida
    for i in range(len(dig[0])):
        if obtem_valor(tab, dig[0][i]) == jog:
            contador_d += 1                           #adiciona 1 caso o valor da posição represente uma posição do jogador inserido
            if contador_d >= k and pos in dig[0][i - k + 1:i + 1]:
                return True
        else:
            contador_d = 0                            #reseta o contador caso duas posições consecutivas não sejam do mesmo jogador

    #verifica se existe k posições consecutivas do mesmo jogador na antidiagonal da posição inserida
    for i in range(len(dig[1])):
        if obtem_valor(tab, dig[1][i]) == jog:
            contador_ad += 1                          #adiciona 1 caso o valor da posição represente uma posição do jogador inserido
            if contador_ad >= k and pos in dig[1][i - k + 1:i + 1]:
                return True
        else:
            contador_ad = 0                           #reseta o contador caso duas posições consecutivas não sejam do mesmo jogador

    return False

#2.3 - FUNÇÕES DE JOGO

#2.3.1 que analiza se o jogo já terminou (True) ou não (False)
def eh_fim_jogo(tab, k):
    """
    Verifica se o jogo já terminou

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - k (int): O número mínimo de peças consecutivas que o jogador tem de ter

    Retorna:
    - True, se o jogo já terminou
    - False, caso contrário

    Levanta:
    - ValueError: Caso algum dos argumentos fornecidos for inválido
    """
    #gera os erros associados aos argumentos inseridos
    if not eh_tabuleiro(tab) or type(k) != int or k <= 0:
        raise ValueError("eh_fim_jogo: argumentos invalidos")
    
    for i in range(1, n_colunas(tab) * n_linhas(tab) + 1):

        #utiliza a função 2.2.8 para verificar se o jogador de pedras pretas tem k pedras consecutivas
        if verifica_k_linhas(tab, i, 1, k):
            return True
        
        #utiliza a função 2.2.8 para verificar se o jogador de pedras brancas tem k pedras consecutivas
        if verifica_k_linhas(tab, i, -1, k):
            return True
        
    #utiliza a função 2.2.3 para verificar se não existem mais posições livres no tabuleiro
    if obtem_posicoes_livres(tab) == ():
        return True
    
    return False

#função 2.3.2 que devolve uma posição introduzida manualmente pelo jogador
def escolhe_posicao_manual(tab):
    """
    Pede ao jogador que insira manualmente uma posição válida e livre do tabuleiro

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos

    Retorna:
    - A posição escolhida pelo jogador

    Levanta:
    - ValueError: Se o tabuleiro fornecido for inválido
    """
    #gera um erro com base na função eh_tabuleiro (função 2.1.1 que analiza se o argumento corresponde a um tabuleiro)
    if not eh_tabuleiro(tab):
        raise ValueError("escolhe_posicao_manual: argumento invalido")

    #pede ao jogador para inserir uma posição do tabuleiro
    pos = input("Turno do jogador. Escolha uma posicao livre: ")
    if pos.isnumeric():
        pos = int(pos)


    #utiliza a função 2.2.3 para verificar se a posição inserida corresponde a uma posição livre do tabuleiro
    while pos not in obtem_posicoes_livres(tab):

        #pede ao jogador para inserir uma posição do tabuleiro
        pos = input("Turno do jogador. Escolha uma posicao livre: ")
        if pos.isnumeric():
            pos = int(pos)
    
    return pos

#função que corresponde à estratégia facil
def estrategia_facil(tab, jog):
    """
    Determina a estratégia fácil para a jogada do computador

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - jog (int): O jogador, sendo "1" referente ao 1º jogador e "-1" referente ao 2º jogador

    Retorna:
    - A posição onde o computador deve colocar a sua peça
    """
    n_posicoes = n_colunas(tab) * n_linhas(tab)
    adj = ()
    lista_adj = []

    #utiliza a função 2.2.6 para ordenar as posições por ordem crescente de distância ao centro do tabuleiro
    pos = ordena_posicoes_tabuleiro(tab, tuple(range(1, n_posicoes + 1)))

    #analiza se existe uma posição livre e adjacente a uma pedra branca já presente
    for p in obtem_posicoes_jogador(tab, jog):        #utiliza a função 2.2.4 para calcular todas as posições do jogador inserido
        adj += obtem_posicoes_adjacentes(tab, p)      #utiliza a função 2.2.5 para calcular as posições adjacentes a uma posição do jogador inserido

    #vê se não existe dentro do tuplo das posições adjacentes uma posição repetida
    for el in adj:
        if el not in lista_adj:
            lista_adj.append(el)
    lista_adj = tuple(lista_adj)

    ordem = ordena_posicoes_tabuleiro(tab, lista_adj)
    #utiliza a função 2.2.6 para ordenar as posições por ordem crescente de distância ao centro do tabuleiro
    for i in ordem:
        if eh_posicao_livre(tab, i):                  #utiliza a função 2.2.2 para calcular a 1º posição adjacente à inserida que está livre
            return i                                  #retorna a posição onde a pedra vai ser inserida
    
    #caso não exista nenhuma posição livre e adjacente a uma pedra branca já presente
    for c in pos:
        if eh_posicao_livre(tab, c):                  #utiliza a função 2.2.2 para calcular a 1º posição livre
            return c                                  #retorna a posição onde a pedra vai ser inserida
    
#função que corresponde à estratégia normal
def estrategia_normal(tab, jog, k):
    """
    Determina a estratégia normal para a jogada do computador

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - jog (int): O jogador, sendo "1" referente ao 1º jogador e "-1" referente ao 2º jogador
    - k (int): O número mínimo de peças consecutivas que o jogador tem de ter

    Retorna:
    - A posição onde o computador deve colocar a sua peça
    """
    n_posicoes = n_colunas(tab) * n_linhas(tab)
    posicao = ordena_posicoes_tabuleiro(tab, tuple(range(1, n_posicoes + 1)))

    #verifica se consegue fazer uma linha com L pedras consecutivas
    for L in range(k, 0, -1):

        #encontra a melhor posição para fazer uma linha com L peças seguidas
        for pos in ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab)):
            tab_simulado = marca_posicao(tab, pos, jog)
            if verifica_k_linhas(tab_simulado, pos, jog, L):
                return pos
        
        #caso seja necessário, bloqueia o adversário
        for pos in ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab)):
            tab_simulado = marca_posicao(tab, pos, -jog)
            if verifica_k_linhas(tab_simulado, pos, -jog, L):
                return pos
    
    #caso não haja nehuma posição que consiga meter k peças seguidas ou não seja preciso bloquear o adversário, joga na posição livre mais central
    for c in posicao:
        if eh_posicao_livre(tab, c):          #utiliza a função 2.2.2 para calcular a 1º posição livre
            return c 

#função que corresponde à estratégia dificil
def estrategia_dificil(tab, jog, k):
    """
    Determina a estratégia difícil para a jogada do computador

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - jog (int): O jogador, sendo "1" referente ao 1º jogador e "-1" referente ao 2º jogador
    - k (int): O número mínimo de peças consecutivas que o jogador tem de ter

    Retorna:
    - A posição onde o computador deve colocar a sua peça
    """
    pos_livres = ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab))

    #verifica se é possível ganhar o jogo
    for pos in pos_livres:
        tab_simulado = marca_posicao(tab, pos, jog)
        if verifica_k_linhas(tab_simulado, pos, jog, k):
            return pos

    #caso não consiga ganahr o jogo, verifica se o adversário consegue ganahr e bloqueia-o
    for pos in pos_livres:
        tab_simulado = marca_posicao(tab, pos, -jog)
        if verifica_k_linhas(tab_simulado, pos, -jog, k):
            return pos
    
    #caso não consiga uma das cenas anteriores, simula várias jogadas para saber qual a melhor posição para jogar
    for pos in pos_livres:
        tab_simulado = tab
        jogada_1 = 1
        #simula o jogo
        while not eh_fim_jogo(tab_simulado, k):
            if jogada_1 == 1:
                pos_simulado = pos
            else:
                pos_simulado = estrategia_normal(tab_simulado, jog, k)
            tab_simulado = marca_posicao(tab_simulado, pos_simulado, jog)
            
            #caso consiga ganhar, retorna essa posição que levou a isso
            if verifica_k_linhas(tab_simulado, pos_simulado, jog, k):
                return pos
            
            #caso dê fim do jogo, sai do loop
            elif eh_fim_jogo(tab_simulado, k):
                break

            pos_simulado = estrategia_normal(tab_simulado, -jog, k)
            tab_simulado = marca_posicao(tab_simulado, pos_simulado, -jog)
            jogada_1 += 1

    m = n_linhas(tab)
    n = n_colunas(tab)
    centro = (m // 2) * n + n // 2 + 1

    #se o centro for uma posição livre, não joga nesta 
    if centro in pos_livres:
        return pos_livres[1]
    
    else:
        return pos_livres[0]

#função 2.3.3 que devolve a posição escolhida automaticamente consoante a estratégia selecionada
def escolhe_posicao_auto(tab, jog, k, lvl):
    """
    Escolhe a posição que o computador irá jogar com base no nível de dificuldade escolhido

    Parâmetro:
    - tab (tup): O tabuleiro válido que é um tuplo de tuplos
    - jog (int): O jogador, sendo "1" referente ao 1º jogador e "-1" referente ao 2º jogador
    - k (int): O número mínimo de peças consecutivas que o jogador tem de ter
    - lvl (str): O nível de dificuldade desejado ("facil", "normal", "dificl")

    Retorna:
    - Um inteiro que corresponde à posição escolhida pelo computador

    Levanta:
    - ValueError: Caso algum dos argumentos fornecidos for inválido
    """
    #gera os erros associados aos argumentos inseridos
    if not eh_tabuleiro(tab) or type(jog) != int or jog not in (1, -1) or \
     type(k) != int or k <= 0 or eh_fim_jogo(tab, k) or (lvl != "facil" and lvl != "normal" and lvl != "dificil"):
        raise ValueError("escolhe_posicao_auto: argumentos invalidos")

    if lvl == "facil":
        return estrategia_facil(tab, jog)

    elif lvl == "normal":
        return estrategia_normal(tab, jog, k)
    
    elif lvl == "dificil":
        return estrategia_dificil(tab, jog, k)
    
#função 2.3.4 que permite jogar um jogo completo
def jogo_mnk(cfg, jog, lvl):
    """
    Permite jogar um jogo completo

    Parâmetro:
    - cfg (tup): Um tuplo que contem 3 informações: O número de linhas (m) ou número de colunas (n) e o número de peças consecutivas para ganhar o jogo (k)
    - jog (int): O jogador, sendo "1" referente ao 1º jogador e "-1" referente ao 2º jogador
    - lvl (str): O nível de dificuldade desejado ("facil", "normal", "dificl")

    Retorna:
    - Uma mensagem a dizer quem ganhou o jogo

    Levanta:
    - ValueError: Caso algum dos argumentos fornecidos for inválido
    """
    #gera os erros associados aos argumentos inseridos
    if type(cfg) != tuple or len(cfg) != 3 or 100 < cfg[0] < 2 or 100 < cfg[1] < 2 or type(cfg[2]) != int or cfg[2] <= 0 \
     or cfg[2] > 100 or type(jog) != int or jog not in (1, -1) or (lvl != "facil" and lvl != "normal" and lvl != "dificil"):
        raise ValueError("jogo_mnk: argumentos invalidos")

    #gera um erro caso o tuplo não seja formado por números inteiros
    for num in cfg:
        if type(num) != int:
            raise ValueError("jogo_mnk: argumentos invalidos")
    
    tup_int = ()
    print("Bem-vindo ao JOGO MNK.")

    #cria um tabuleiro com todos os espaços livres das dimensões inseridas
    tup_int += (0,) * cfg[1]
    tab = ((tup_int),) * cfg[0]

    #gera um erro com base na função eh_tabuleiro (função 2.1.1 que analiza se o argumento corresponde a um tabuleiro)
    if not eh_tabuleiro(tab):
        raise ValueError("jogo_mnk: argumentos invalidos")

    #Caso a posição escolhida pelo jogador seja 1 (pedras pretas)
    if jog == 1:
        print("O jogador joga com 'X'.")
        print(tabuleiro_para_str(tab))
        pos = escolhe_posicao_manual(tab)
        tab = marca_posicao(tab, pos, 1)
        print(tabuleiro_para_str(tab))
    
        while not eh_fim_jogo(tab, cfg[2]):
            print("Turno do computador (" + lvl + "):")
            pos_adv = escolhe_posicao_auto(tab, -1, cfg[2], lvl)
            tab = marca_posicao(tab, pos_adv, -1)
            print(tabuleiro_para_str(tab))

            #verifica se o jogador perdeu
            if verifica_k_linhas(tab, pos_adv, -1, cfg[2]):
                print("DERROTA")
                return -1

            #verifica se o jogo acabou em empate
            if obtem_posicoes_livres(tab) == ():
                print("EMPATE")
                return 0

            nova_pos = escolhe_posicao_manual(tab)
            tab = marca_posicao(tab, nova_pos, 1)
            print(tabuleiro_para_str(tab))
        
            #verifica se o jogador ganhou
            if verifica_k_linhas(tab, nova_pos, 1, cfg[2]):
                print("VITORIA")
                return 1
            
            #verifica se o jogo acabou em empate
            if obtem_posicoes_livres(tab) == ():
                print("EMPATE")
                return 0

    #Caso a posição escolhida pelo jogador seja -1 (pedras brancas)
    else:
        print("O jogador joga com 'O'.")
        print(tabuleiro_para_str(tab))
        print("Turno do computador (" + lvl + "):")
        pos_adv = escolhe_posicao_auto(tab, 1, cfg[2], lvl)
        tab = marca_posicao(tab, pos_adv, 1)
        print(tabuleiro_para_str(tab))

        while eh_fim_jogo(tab, cfg[2]) == False:
            
            nova_pos = escolhe_posicao_manual(tab)
            tab = marca_posicao(tab, nova_pos, -1)
            print(tabuleiro_para_str(tab))

            #verifica se o jogador ganhou
            if verifica_k_linhas(tab, nova_pos, -1, cfg[2]):
                print("VITORIA")
                return -1
            
            #verifica se o jogo acabou empatado
            if obtem_posicoes_livres(tab) == ():
                print("EMPATE")
                return 0
            
            print("Turno do computador (" + lvl + "):")
            pos_adv = escolhe_posicao_auto(tab, 1, cfg[2], lvl)
            tab = marca_posicao(tab, pos_adv, 1)
            print(tabuleiro_para_str(tab))

            #verifica se o jogador perdeu
            if verifica_k_linhas(tab, pos_adv, 1, cfg[2]):
                print("DERROTA")
                return 1

            #verifica se o jogo acabou empatado
            if obtem_posicoes_livres(tab) == ():
                print("EMPATE")
                return 0