# import numpy as np
#
#
# class funcao_ativacao:
#     def sigmoid(self, s):
#         # activation function
#         return 1 / (1 + np.exp(-s))
#
#
# class Neural_Network(funcao_ativacao):
#     def __init__(self, imput, output, qtd_camada):
#         # parameters
#         self._input_size = imput
#         self._output_size = output
#         self._qtd_camadas = qtd_camada
#         self._qtd_neuronios_camada_oculta = 5
#
#     def _pesos(self, camada_imput, qtd_neuronios):
#         return np.random.randn(camada_imput, qtd_neuronios)
#
#
# if __name__ == '__main__':
#     X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
#     y = np.array(([92], [86], [89]), dtype=float)
#
#     X = X / np.amax(X, axis=0)
#     y = y / 100
#
#     print(X, y)
