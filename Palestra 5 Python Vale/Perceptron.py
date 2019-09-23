"""
Formula:

perceptron = x1 * w1 + x2 * w2 + ... + xn * wn

np.dot(x, w)

"""
import numpy as np


class Perceptron:
    def __init__(self, num_entradas, epochs=15, learning_rate=0.001):
        self.__epochs = epochs
        self.__learning_rate = learning_rate
        self.__weights = np.zeros(num_entradas)
        self.__bias = np.zeros(1)

    def predict(self, entradas):
        soma = np.dot(entradas, self.__weights) + self.__bias
        return 1 if soma > 0 else 0

    def fit(self, X_input, Y):
        string = "Esperado:{}, Previsto:{}, Bias:{}, Weights: {}, Erro: {}"
        for _ in range(self.__epochs):
            for x, y in zip(X_input, Y):
                predict = self.predict(x)
                erro = y - predict
                self.__weights += self.__learning_rate * erro * np.array(x)
                self.__bias += self.__learning_rate * erro

            # if _ % 10 == 0:
            print(string.format(y, predict, self.__bias, self.__weights, erro))


if __name__ == '__main__':
    from datetime import datetime

    start = datetime.now()
    x_input = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y_and = np.array([0, 0, 0, 1])  # AND

    model = Perceptron(len(x_input[0]))
    model.fit(x_input, y_and)

    print('Tempo decorrido:', datetime.now() - start)
