"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys
from operator import itemgetter, attrgetter


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).
def ler(nome):
    filename = open(nome,"r")
    texto = filename.read()
    filename.close()
    texto = texto.lower()
    texto = texto.split()
    return texto

def contar(filename):
    arquivo = ler(filename)
    palavra, quantidades = [], []
    for p in arquivo:
        if p not in palavra:
            palavra.append(p)
    for l in palavra:
        quantidades.append(arquivo.count(l))
    words = list(zip(palavra, quantidades))
    return words

def print_words(filename):
    words = contar(filename)
    for p in words:
        palavra, quantidade = p
        print(palavra, quantidade)

def print_top(filename):
    words = contar(filename)
    words = sorted(words,key=itemgetter(1),reverse= True)
    cont = 0
    for p in words:
        cont +=1
        if cont < 20:
            palavra, quantidade = p
            print(palavra,quantidade)

'''
# SOLUÇÃO FINAL (HENRIQUE B.) ###

def report(words):
    return '\n'.join([f'{w} {qty}' for w, qty in words])


def asc(counter):
    return sorted(counter.items())


def top(counter, qty=20):
    return sorted(counter.items(), reverse=True, key=lambda t: t[-1])[:qty]


def read(filename):
    with open(filename) as f:
        return f.read()


def count(content):
    words = content.lower().split()
    return Counter(words)


def count_words(filename):
    return report(asc(count(read(filename))))


def top_words(filename):
    return report(top(count(read(filename))))

'''



# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
