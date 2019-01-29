# -*- coding: utf-8 -*-
__author__ = 'Luís Vtório'

# -*- encoding:utf-8
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = load_iris()

df = pd.DataFrame(data.data, columns=data.feature_names)
x = df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)']]
y = df['petal width (cm)']

x_train, x_teste, y_train, y_teste = train_test_split(x, y, test_size=0.5, random_state=101)
lm = LogisticRegression()
lm.fit(x_train, y_train)
predicao = lm.predict(x_teste)

# cr = classification_report(y_teste,predicao)

# mtx = confusion_matrix(y_teste,predicao)
# acc = accuracy_score(y_teste,predicao)
print(predicao)

np.n