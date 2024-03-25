from flask import Flask, render_template, render_template_string, request, redirect, url_for
from flask_mysqldb import MySQL
import config
app = Flask(__name__)

app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB
mysql = MySQL(app)
@app.route('/')
@app.route('/home') 
def home_page():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM jobs")
    data = cur.fetchall()
    cur.close()
    print(data)
    return render_template('home.html',data=data)

@app.route('/market')
def market_page():
    item = [
        {'id':1, 'name':'Shubham', 'price':500},
        {'id':2, 'name':'Sumer', 'price':500},
        {'id':3, 'name':'Karan', 'price':500}
    ]
    return render_template('market.html', item = item)


@app.route('/jobs')
def jobs_page():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM jobs")
    data = cur.fetchall()
    cur.close()
    #print(data)
    return render_template('jobs.html',data=data)


if __name__ == '__main__':
    app.run(debug=True) 