from flask import Flask, render_template, request
import flask
from flask_cors import cross_origin
import pickle

app = Flask(__name__)

@app.route('/',methods = ['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            CRIM = float(request.form['CRIM'])
            ZN = float(request.form['ZN'])
            INDUS = float(request.form['INDUS'])
            CHAS = float(request.form['CHAS'])
            NOX = float(request.form['NOX'])
            RM = float(request.form['RM'])
            AGE = float(request.form['AGE'])
            DIS = float(request.form['DIS'])
            RAD = float(request.form['RAD'])
            TAX = float(request.form['TAX'])
            PTRATIO = float(request.form['PTRATIO'])
            B = float(request.form['B'])
            LSTAT = float(request.form['LSTAT'])

            filename = 'linear_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))
            prediction = loaded_model.predict([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])
            return render_template('results.html',prediction=prediction)
        except Exception as e:
            print('Error is: ',e)

if __name__ == '__main__':
    app.run(debug=True)
