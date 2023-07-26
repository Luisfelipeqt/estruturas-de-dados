import numpy as np


class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade # Tamanho do VETOR
        self.ultima_posicao = -1 # A última posição do vetor é sempre -1 e será acrecentada conforme adicionarmos valor no Array
        self.valores = np.empty(self.capacidade, dtype = int) # Onde teremos os dados do VETOR, e ele será do tamanho do argumento


    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1: # Se o tamanho do Vetor for -1 significa que está vazio
            print("O vetor esta vazio!")
        else:
            for i in range(self.ultima_posicao + 1): # Iteração até a última posição do VETOR
                print(i, " - ", self.valores[i]) # Printar a posição e os valores em cada posição do Array

    # O(1) - O(2)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1: # Se o tamanho do VETOR for do tamanho de sua capacidade, significa que o VETOR está cheio, serve para não passarmos da capacidade e nem adicionarmos valores em espaço inexistente
            print("Capacidade maxima atingida!")

        else:
            self.ultima_posicao += 1 # Se não estouramos a capacidade do vetor nós iremos incrementar a ultima posição, ou seja se a última posição está em 0 e adicionamos agora é 1
            self.valores[self.ultima_posicao] = valor # Adicionaremos o valor do parametro na última posição do VETOR

    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1): # Irá percorrer todo o VETOR
            if valor == self.valores[i]: # Se o valor for igual a algum velor dentro do VETOR 
                return i # Retorna o valor do parametro caso esse valor se encontre no VETOR
        return -1 # Retorna -1 se o elemento não existir no vetor
    
    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor) # Vamos pesquisar o valor
        if posicao == -1: # Se a posição for -1 significa que o vetor está vazio
            return -1 # Retorna vazio
        else:
            for i in range(posicao, self.ultima_posicao): # Começamos a procurar a partir da posição encontrada na pesquisa
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1

                





vetor = VetorNaoOrdenado(5)
vetor.imprime()
vetor.insere(2)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)
vetor.imprime()
print("---------------------------")
print("---------------------------")
print("---------------------------")
vetor.excluir(5)
vetor.imprime()
print("---------------------------")
print("---------------------------")
print("---------------------------")
vetor.excluir(8)
vetor.imprime()
print("---------------------------")
print("---------------------------")
print("---------------------------")
vetor.excluir(3)
vetor.imprime()