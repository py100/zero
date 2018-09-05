#! python3
#coding=utf8

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn import metrics

class linear:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def train(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, random_state=1)
        self.linreg = LinearRegression()
        self.linreg.fit(self.x_train, self.y_train)
        # print(self.linreg.intercept_)
        # print(self.linreg.coef_)

    def evaluate(self):
        y_pred = self.linreg.predict(self.x_test)
        self.mse = metrics.mean_squared_error(self.y_test, y_pred)
        self.r2 = self.linreg.score(self.x_test, self.y_test)
        self.result = dict()
        self.result['mse'] = self.mse
        self.result['r2'] = self.r2

    def getresult(self):
        return self.result

class ridge:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def train(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, random_state=1)
        self.model = Ridge()
        self.model.fit(self.x_train, self.y_train)
        # print(self.model.intercept_)
        # print(self.model.coef_)

    def evaluate(self):
        y_pred = self.model.predict(self.x_test)
        self.mse = metrics.mean_squared_error(self.y_test, y_pred)
        self.r2 = self.model.score(self.x_test, self.y_test)
        self.result = dict()
        self.result['mse'] = self.mse
        self.result['r2'] = self.r2

    def getresult(self):
        return self.result

class elasticnet:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def train(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, random_state=1)
        self.model = ElasticNet()
        self.model.fit(self.x_train, self.y_train)
        # print(self.model.intercept_)
        # print(self.model.coef_)

    def evaluate(self):
        y_pred = self.model.predict(self.x_test)
        self.mse = metrics.mean_squared_error(self.y_test, y_pred)
        self.r2 = self.model.score(self.x_test, self.y_test)
        self.result = dict()
        self.result['mse'] = self.mse
        self.result['r2'] = self.r2

    def getresult(self):
        return self.result
