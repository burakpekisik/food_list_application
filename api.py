from flask import json, Flask, Response
from flask_mysqldb import MySQL
from userInfo import host, user, password, database

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = user
app.config['MYSQL_PASSWORD'] = password
app.config['MYSQL_DB'] = database
app.config['JSON_AS_ASCII'] = False

class CreateApi():
    @app.route('/gazi/menu/<date>', methods=['GET'])
    def FindMenu(date):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM gazi WHERE date = %s", (date,))
        data = cursor.fetchall()
        json_string = json.dumps(data,ensure_ascii = False)
        cursor.close()
        response = Response(json_string,content_type="application/json; charset=utf-8" )
        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
    # app.run(debug=True)
