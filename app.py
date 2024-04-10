from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def home():
    data1 = float(request.form['i1']) 
    data2 = float(request.form['i2'])
    data3 = float(request.form['i3'])
    data4 = float(request.form['i4'])
    data5 = float(request.form['i5'])
    data6 = float(request.form['i6'])
    data7 = float(request.form['i7'])
    data8 = float(request.form['i8'])
    data9 = float(request.form['i9'])
    data10 = float(request.form['i10'])
    data11 = float(request.form['i11'])
    data12 = float(request.form['i12'])
    data13 = float(request.form['i13'])
    arr = np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13]])
    pred = model.predict(arr)
    return render_template('after.html', data = pred)  


if __name__ == "__main__" :
    app.run(debug=True)