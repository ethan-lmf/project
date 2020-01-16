# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/12')
# def index():
#     return "Hello World!"
#
# if __name__ == '__main__':
#     app.run()

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from flask import Flask
app = Flask(__name__)


@app.route('/svm')
def index():
model = svm.SVC(kernel='linear', C=12)
model.fit(x_train,y_train)
model.score(x_test,y_test)

predicted = model.predict(x_test)
score1 =accuracy_score(y_test,predicted)


     return predicted,score1


@app.route('/LogisticRegression')
def index():
lr=LogisticRegression()
lr.fit(x_train,y_train)

predict_y=lr.predict(x_test)
score=accuracy_score(y_test,predict_y)

     return predict_y,score1

if __name__ == '__main__':
    app.run(debug = True,port=8080)