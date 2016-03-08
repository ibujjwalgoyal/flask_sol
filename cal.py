from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/enter',methods = ['POST', 'GET'])
def enter():
   if request.method == 'POST':
      a = request.form['nm1']  
      b = request.form['nm2']
      a = a-0
      b = b-0
      return a+b
   else:
      a = request.args.get('nm1') 
      b = request.args.get('nm2')
      return a+b

if __name__ == '__main__':
   app.run(debug = True)
