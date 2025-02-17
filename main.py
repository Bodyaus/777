from flask import Flask, redirect, url_for, session, request, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
   return render_template("index.html") 


@app.route('/after_login')
def after_login():
   return render_template("after_login.html") 
@app.route('/tickets')
def tickets():
   return render_template("tickets.html") 

@app.route('/forma', methods=['post'])
def forma():
   return 'lzre.'

if __name__ == '__main__':
   app.run(debug=True)

#i want to make a tour agency site with slideble images, some text:the main idea of site is to show tourists cool places in different countrys