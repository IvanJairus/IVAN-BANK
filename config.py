from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_PORT'] = 3366
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'testdb'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

mysql.init_app(app)