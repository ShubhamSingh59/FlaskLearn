from flask import Flask, render_template, render_template_string
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
@app.route('/')
@app.route('/home') 
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    item = [
        {'id':1, 'name':'Shubham', 'price':500},
        {'id':2, 'name':'Sumer', 'price':500},
        {'id':3, 'name':'Karan', 'price':500}
    ]
    return render_template('market.html', item = item)


if __name__ == '__main__':
    app.run(debug=True) 