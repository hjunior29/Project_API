from flask import Flask, jsonify, render_template, request
import jwt

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # importando arquivo html
        return render_template("index_2.html")
    else:
        # pegando login e senha do formulário
        login = request.form.get("login")
        password = request.form.get("password")

        # login e senha corretos
        login_pass = "aluno"
        password_pass = "easycredito"

        # autenticando login e senha
        if login == login_pass and password == password_pass:
            # gerando token
            encoded_jwt = jwt.encode({'token': ''}, "secret", algorithm='HS256')
            jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
            token = jsonify({'token': encoded_jwt})
            return token
        else:
            # retornando erro de senha ou login
            return '<h1>Login ou senha inválido</h1>'
if __name__ == "__main__":
    app.run()