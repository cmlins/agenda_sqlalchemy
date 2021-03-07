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

from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pessoa.sqlite3'
app.secret_key = "alquimia"

db = SQLAlchemy(app)
class pessoas(db.Model):
    pessoa_id = db.Column('pessoa_id', db.Integer, primary_key = True)
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
   return render_template('show_all.html', pessoas = pessoas.query.all())

@app.route('/excluir', methods = ['GET', 'POST'])
def excluir():
    if request.method == 'POST':
        # flash(request.method)
        pessoa = request.form['pessoa_id']
        # flash(f'id: {pessoa}')
        user = pessoas.query.get(pessoa)
        # flash(f'user: {user}')
        db.session.delete(user)
        db.session.commit()
        flash('Pessoa excluída com sucesso')
    return redirect(url_for('show_all'))    

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['nome'] or not request.form['email'] or not request.form['telefone']:
         flash('Campos de preenchimento obrigatório', 'error')
      else:
         pessoa = pessoas(request.form['nome'], request.form['email'], request.form['telefone'], request.form['data_nasc'])
         
         db.session.add(pessoa)
         db.session.commit()
         flash('Pessoa adicionada com sucesso')
         return redirect(url_for('show_all'))
   return render_template('new.html')




if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
