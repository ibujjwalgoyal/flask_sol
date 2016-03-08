from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/enter',methods = ['POST', 'GET'])
def enter():
   if request.method == 'POST':
      a = request.form['nm1']  
      b = request.form['nm2']
      return a+b
   
if __name__ == '__main__':
   app.run(debug = True)
