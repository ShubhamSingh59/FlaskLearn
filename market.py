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
#def test_db_connection():
#    try:
#        # Attempt to establish a connection to the database
#        mysql.connection.ping()
#        return 'Connection to MySQL database successful'
#    except Exception as e:
#        return f'Error connecting to MySQL database: {e}'

#if __name__ == '__main__':
#    app.run(debug=True)
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


@app.route('/jobs')
def jobs_page():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM jobs")
    data = cur.fetchall()
    cur.close()
    print(data)
    return render_template('jobs.html',data=data)

@app.route('/login', methods=['POST'])
def login_page():
    if request.method == 'POST':
        id = request.form['id']
        username = request.form['username']
        email = request.form['inputEmail4']
        password = request.form['inputPassword4']

        cur = mysql.connection.cursor()
        try:
            cur.execute("insert into user (id, username, email, password) values (%s, %s, %s, %s)", (id, username, email, password))
            mysql.connection.commit()
            app.logger.info('Student added successfully: id - %s, username - %s, email - %s, password - %s,', id,username, email, password)
        finally:
            cur.close()
            
        return redirect(url_for('home_page'))

        

if __name__ == '__main__':
    app.run(debug=True) 