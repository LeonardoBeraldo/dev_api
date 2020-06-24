from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id':0,'nome':'Leonardo','habilidades': ['Python', 'Flask']},
    {'id':1,'nome': 'Beraldo', 'habilidades': ['Python', 'Django']}
]

#Devolve um desenvolvedor por ID e também altera e exclui
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Desenvolvedor de ID {} não existe".format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = "Erro desconhecido! Procure o desenvolvedor da API"
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify((dados))
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensaagem': 'Registro excluído'})

#lista todos os desenvolvedores e inclui
@app.route("/dev/", methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
        #return jsonify({'status':'sucesso', 'mensagem':'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)