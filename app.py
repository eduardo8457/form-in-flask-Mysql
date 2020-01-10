
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'suplan'


mysql.init_app(app)

# @app.route('/', methods=['GET', 'POST'])
# def retorn_url():
#     return render_template('index.html')



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        nome = details['name']
        Departamento = details['Departamento']
        dataResposta = details['dtresposta']
        quantidadeRealizada = details['qtrealizada']
        quantidadeReal = details['qtreal']
        valorProvisionado = details['valorP']
        valorUtilizado = details['valorU']
        ResultadoFinal = details['rfinal']
        Observacao = details['obs']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbquestionario(nome, Departamento, dataResposta, quantidadeRealizada,quantidadeReal, valorProvisionado, valorUtilizado, ResultadoFinal, Observacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nome, Departamento, dataResposta, quantidadeRealizada,quantidadeReal, valorProvisionado, valorUtilizado, ResultadoFinal, Observacao))
        mysql.connection.commit()
        cur.close()
    return render_template('cadastro.html')
    

if __name__ == '__main__':
    app.run(debug=True)


