"""
Formula:

perceptron = x1 * w1 + x2 * w2 + ... + xn * wn

np.dot(x, w)

"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def target_decode(_y):
    """
        Convert os targets em vetor
    """
    _dic = {1: 'setosa', 0: 'versicolor'}
    return _dic[_y]


def target_encode(_y):
    """
        Convert os targets em vetor
    """
    _dic = {'setosa': np.array([1]), 'versicolor': np.array([0])}
    return _dic[_y]


class Perceptron_Iris:

    def __init__(self, learning_rate=0.05, epochs=1000):
        self.__lr = learning_rate
        self.__epochs = epochs
        self.__bias = []
        self.__weights = []

    def predict(self, _X):
        soma = np.dot(_X, self.__weights) + self.__bias
        return 1 if soma > 0 else 0

    def fit(self, _X, _Y):
        self.__bias = np.zeros(1)
        self.__weights = np.zeros(X_train.shape[1])
        # string = "Esperado:{}, Previsto:{}, Bias:{}, Weights: {}, Erro: {}"
        acertos = 0
        erros = 0

        for _ in range(self.__epochs):
            for x, target in zip(_X, _Y):
                predict = self.predict(x)
                erro = target - predict
                self.__weights += self.__lr * erro * x
                self.__bias += self.__lr * erro

                if target == predict:
                    acertos += 1
                else:
                    erros += 1

            # if _ % 10 == 0:
            #     print(string.format(target, predict, self.__bias, self.__weights, erro))
        t = acertos + erros
        print("{}% acertos, {}% erros".format(round(acertos / t * 100, 2), round(erros / t * 100, 2)))


if __name__ == '__main__':
    df = pd.read_csv('iris.csv', sep=',', encoding='latin1')

    X = df.drop('species', axis=1)
    y = df['species']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=35)

    X_train = np.array(X_train[1:].astype(float))
    y_train = np.array(y_train.apply(target_encode))

    model = Perceptron_Iris()
    model.fit(X_train, y_train)
