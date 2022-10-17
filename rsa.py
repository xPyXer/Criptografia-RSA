# Trabalho APS - Criptografia RSA
import random


# Calculo do MDC
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


# Verifica se é primo
def verificaPrimo(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num <2:
        return False
    for n in range(3, int(num**0.5) + 1, 2):
        if num % n == 0:
            return False
    return True


# Algoritmo de Euclides estendido
def inversoMultiplicativo(a, m):
    for x in range(1, m):
        if(a * x) % m == 1:
            return x
    return -1


# Gerando as chaves publica (p) e privada (q)
def gerarChaves(p, q):
    if not (verificaPrimo(p) and verificaPrimo(q)):
        raise print('Ambos os números devem ser primos!')
    elif p == q:
        raise print('Os valores inseridos não podem ser iguais!')
    # Módulo para encontrar o Produto de p e q
    n = p * q
    # Função Totiente de Euler (descobrir a quantidade de coprimos)
    tot = (p-1) * (q-1)
    # Gera um número aleátorio entre 1 e os coprimos do número fornecido
    e = random.randrange(1, tot)
    g = mdc(e, tot)
    while g != 1:
        e = random.randrange(1, tot)
        g = mdc(e, tot)
    # Gerando a chave privada por meio do Algoritmo de Euclides extendido
    d = inversoMultiplicativo(e, tot)
    return ((e, n), (d, n))    # (e,n) -> Pública / (d, n) Privada


# Encripitando
def encrypt(cp, texto):
    chave, n = cp
    # Converta cada letra do texto em números com base no caractere usando a^b mod m
    cifra = [pow(ord(char), chave, n) for char in texto]
    return cifra


# Decripitando
def decripitando(cp, textoCifrado):
    chave, n = cp
    aux = [str(pow(char, chave, n)) for char in textoCifrado]
    decript = [chr(int(char2)) for char2 in aux]
    return ''.join(decript)


# Prints e Inputs

# Obtendo 2 números primos diferentes "p" e "q"
p = int(input("\033[1:34m Digite um número primo (ex: 17, 19, 23, etc): \033[m"))
q = int(input("\033[1:34m Digite outro número primo diferente do anterior: \033[m"))
# var Publica recebe o valor de p / var Privada recebe o valor de q
publica, privada = gerarChaves(p, q)


print(f"\033[1:33m Sua chave pública é: \033[m\033[4:35m{publica}\033[m")
print(f"\033[1:33m Sua chave privada é: \033[m\033[4:31m{privada}\033[m")
mensagem = input("\033[1:34mDigite a mensagem a ser criptografada: \033[m")
encriptMsg = encrypt(publica, mensagem)


print("\033[1:33m Sua mensagem cripitografada é:\033[35m", ''.join(map(lambda x: str(x) + " ", encriptMsg)))
print(f"\033[1:33m Descripitografe sua mensagem com a chave: \033[4:31m{privada} \033[m")


print(" ")
print(" ")
print('\033[1:34m Digite [ dec ], caso queira decripitar \033[m ')
palavra = input('\033[1:32m>>> \033[m')


if 'dec' in palavra:
    input("\033[1:34m Digite a mensagem encripitada: \033[m")
    input("\033[1:34m Digite a chave privada para decripitar: \033[m")
    print("\033[1:34m Sua mensagem decripitada é: \033[m", decripitando(privada, encriptMsg))