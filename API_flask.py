from flask import Flask
from flask import jsonify
import jwt

login = input("Login: ")
password = input("Password: ")
login_pass = "aluno"
password_pass = "easycredito"

app = Flask(__name__)

@app.route("/teste",methods=['GET'])

def index():
    encoded_jwt = jwt.encode({'token': ''}, "secret", algorithm='HS256')
    jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
    if login == login_pass and password == password_pass:
        return jsonify({'token': encoded_jwt})

if __name__ == "__main__":
    app.run()