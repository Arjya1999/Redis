
from flask import Flask,render_template,url_for,request
import pickle

# load the model from disk
data={"name":"Arjya Basu","gender":"male","Age":"22"}

app = Flask(__name__)
'''
@app.route('/')
def home():
	return render_template('home.html')
'''
@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
 
        return data
    else:
        return data

if __name__ == '__main__':
	app.run(debug=True)
