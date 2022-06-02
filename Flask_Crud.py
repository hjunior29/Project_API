from flask import Flask,render_template,request,redirect, abort, jsonify
from models import db,EmployeeModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index_2.html")
    else:
        login = request.form.get("login")
        password = request.form.get("password")
        login_pass = "aluno"
        password_pass = "easycredito"

        if login == login_pass and password == password_pass:
            return redirect('/data/create')
        else:
            return redirect('/')

@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
    if request.method == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        cnpj = request.form.get('cnpj')
        nasc = request.form.get('nasc')
        employee = EmployeeModel(nome=nome, cpf=cpf, email=email, telefone=telefone, cnpj=cnpj, nasc=nasc)
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')
    return redirect('/')


@app.route('/data')
def RetrieveList():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html',employees = employees)

@app.route('/data/<string:cpf>')
def RetrieveEmployee(cpf):
    employee = EmployeeModel.query.filter_by(cpf=cpf)
    if employee:
        return render_template('data.html', employee = employee)
    else:
        return f"O usuário com o cpf ={cpf} não existe"
    return redirect('/data')

@app.route('/data/<string:cpf>/update',methods = ['GET','POST'])
def update(cpf):
    employee = EmployeeModel.query.filter_by(cpf=cpf).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            nome = request.form.get('nome')
            cpf = request.form.get('cpf')
            email = request.form.get('email')
            telefone = request.form.get('telefone')
            cnpj = request.form.get('cnpj')
            nasc = request.form.get('nasc')
            employee = EmployeeModel(nome=nome, cpf=cpf, email=email, telefone=telefone, cnpj=cnpj, nasc=nasc)
            db.session.add(employee)
            db.session.commit()
            return redirect('/data')
        return f"O usuário com o cpf ={cpf} não existe"

    return render_template('update.html', employee = employee)


@app.route('/data/<string:cpf>/delete', methods=['GET','POST'])
def delete(cpf):
    employee = EmployeeModel.query.filter_by(cpf=cpf).one()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/data')
        else:
            abort(404)
    else:
        return render_template('delete.html')
    return redirect('/data')
if __name__ == '__main__':
    app.run()