import numpy as np


class VetoresOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio!")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, " - ", self.valores[i])

    def insere(self, valor):
        # Se a ultima posição do vetor for igual a sua capcidade
        # Printar que a máxima foi atingida
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade máxima atingida!")
            return
        # vai ser útil para quando formos inserir pela primeira vez
        posicao = 0
        # Vamos correr todos os elementos do vetor
        for i in range(self.ultima_posicao + 1):
            # A posição varia de acordo que avançamos no vetor
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            # A posição subsequente de x1 vai receber o valor atual
            self.valores[x + 1] = self.valores[x]
            # Decrementa até o valor de x for igual a posição
            x -= 1
        # Após remanejar os elementos vamos inserir o valor
        self.valores[posicao] = valor
        self.ultima_posicao += 1

vetor = VetoresOrdenado(10)
vetor.imprime()

vetor.insere(6)

vetor.insere(4)
vetor.insere(3)
vetor.insere(5)
vetor.insere(1)
vetor.insere(8)
vetor.imprime()