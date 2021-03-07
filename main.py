'''
Atividade feita por:
Cinthya Lins
Fabiana Sugamele
Isa Guaraldo

Seguindo o exemplo do exercicio mostrado em sala de aula, mudar a entidade pessoas para a entidade pessoa, 
onde os campos serão: 
id (inteiro PK), 
nome (texto), 
email (texto), 
telefone (apenas 1) (texto) e 
data nascimento (texto).
Opcional: Fazer a exclusão de um registro também
'''

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pessoa.sqlite3'

db = SQLAlchemy(app)
class pessoas(db.Model):
    id = db.Column('pessoa_id', db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(50))
    telefone = db.Column(db.String(11))
    data_nasc = db.Column(db.String(10))

    def __init__(self, nome, email, telefone, data_nasc):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data_nasc = data_nasc

@app.route('/')
def show_all():
   return render_template('show_all.html', pessoas = pessoas.query.all() )
