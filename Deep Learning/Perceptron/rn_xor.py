import numpy as np


# https://towardsdatascience.com/how-to-build-a-simple-neural-network-from-scratch-with-python-9f011896d2f3


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def inicializar_parametro(n_x, n_h, n_y):
    """
    Inicializador de parametros
    W = pesos da  rede 
    B = Bias
    """
    W1 = np.random.randn(n_h, n_x)
    b1 = np.zeros((n_y, 1))

    W2 = np.random.randn(n_y, n_h)
    b2 = np.zeros((n_y, 1))

    parametros = {
        "W1": W1,
        "W2": W2,
        "b1": b1,
        "b2": b2
    }
    return parametros


def forward_prop(X, parametros):
    """
    Função de propagação
    """
    W1 = parametros["W1"]
    b1 = parametros["b1"]
    W2 = parametros["W2"]
    b2 = parametros["b2"]

    Z1 = np.dot(W1, X) + b1
    A1 = np.tanh(Z1)

    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)

    cache = {"A1": A1, "A2": A2}

    return A2, cache


def calculate_cost(A2, Y, m):
    """
    Função de perda
    """
    cost = -np.sum(np.multiply(Y, np.log(A2)) + np.multiply(1 - Y, np.log(1 - A2))) / m
    custo = np.squeeze(cost)

    return custo


def backward_prop(X, Y, _cache, _parameters, _number_exemple_train):
    """
    BACK PROPAGATION
    """
    A1 = _cache["A1"]
    A2 = _cache["A2"]

    W2 = _parameters["W2"]

    dZ2 = A2 - Y
    dW2 = np.dot(dZ2, A1.T) / _number_exemple_train
    db2 = np.sum(dZ2, axis=1, keepdims=True) / _number_exemple_train
    dZ1 = np.multiply(np.dot(W2.T, dZ2), 1 - np.power(A1, 2))
    dW1 = np.dot(dZ1, X.T) / _number_exemple_train
    db1 = np.sum(dZ1, axis=1, keepdims=True) / _number_exemple_train

    grads = {
        "dW1": dW1,
        "db1": db1,
        "dW2": dW2,
        "db2": db2
    }

    return grads


def update_parameters(parameters, grads, learning_rate):
    """
    atualiza os valores da rede
    """

    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]

    dW1 = grads["dW1"]
    db1 = grads["db1"]
    dW2 = grads["dW2"]
    db2 = grads["db2"]

    W1 = W1 - learning_rate * dW1
    b1 = b1 - learning_rate * db1
    W2 = W2 - learning_rate * dW2
    b2 = b2 - learning_rate * db2

    new_parameters = {
        "W1": W1,
        "W2": W2,
        "b1": b1,
        "b2": b2
    }

    return new_parameters


def model(X, Y, n_x, n_h, n_y, num_of_epocs, learning_rate, _number_exemple_train):
    parameters = inicializar_parametro(n_x, n_h, n_y)

    for i in range(0, num_of_epocs + 1):
        a2, cache = forward_prop(X, parameters)

        # custa da rede
        cost = calculate_cost(a2, Y, _number_exemple_train)

        # back propagation
        grads = backward_prop(X, Y, cache, parameters, _number_exemple_train)

        # atualiza os parametros da rede
        parameters = update_parameters(parameters, grads, learning_rate)

        if i % 100 == 0:
            print('Custo após interação # {:d}: {:f}'.format(i, cost))

    return parameters


def predict(X, parameters):
    a2, cache = forward_prop(X, parameters)
    yhat = a2
    yhat = np.squeeze(yhat)

    _y_predict = 1 if yhat >= 0.5 else 0

    return _y_predict


if __name__ == "__main__":
    np.random.seed(2)

    # Os 4 exemplos de treinamento por colunas
    _X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])

    # As saídas do XOR para cada exemplo em X
    _Y = np.array([[0, 1, 1, 0]])

    # Numeros de exemplos de treinamento
    _number_exemple_train = _X.shape[1]

    # Definir os hiperparâmetros
    _n_x = 2  # Numeros de neurônios na primeira camada
    _n_h = 3  # Numeros de neurônios na camada oculta
    _n_y = 1  # Numeros de neurônios na camada de saída
    _num_of_epocs = 1000  # Número de interações (epocas)
    _learning_rate = 0.3  # taxa de aprendizagem

    trained_parameters = model(_X, _Y, _n_x, _n_h, _n_y, _num_of_epocs, _learning_rate, _number_exemple_train)

    # Teste o vetor 2X1 para calcular o XOR de seus elementos.
    # Você pode tentar qualquer um desses: (0, 0), (0, 1), (1, 0), (1, 1)
    X_test = np.array([[1], [1]])
    y_predict = predict(X_test, trained_parameters)
    # Imprimir o resultado
    print('Previsão da RN ({:d}, {:d}) é {:d}'.format(X_test[0][0], X_test[1][0], y_predict))
