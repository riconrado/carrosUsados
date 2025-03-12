from flask import Flask, jsonify
from bd import conn
from sqlalchemy import text

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_carros():
    query = text("SELECT marca,modelo,ano,preco FROM veiculos ORDER BY ano DESC limit 100")
    cursor = conn.cursor()
    carros = conn.execute(query).fetchall()
    conn.close()

    carros = [tuple(row) for row in carros] # Transforma Objeto 'row' em 'tuple' para poder ser formatado em json
    return jsonify(carros, 200) # Status code 200 = OK
    

@app.route('/lista_marcas', methods=['GET'])
def get_marcas():
    query = text("SELECT DISTINCT marca FROM veiculos ORDER BY marca")
    marcas = conn.execute(query).fetchall()
    # conn.close()
    marcas = [tuple(row) for row in marcas] # Transforma Objeto 'row' em 'tuple' para poder ser formatado em json
    return jsonify(marcas, 200) # Status code 200 = OK


@app.route('/lista_modelos/<marca>', methods=['GET'])
def get_modelos(marca):

    query = text(f"SELECT DISTINCT concat(modelo,' - ',ano) descricao,preco FROM veiculos WHERE marca = '{marca}' GROUP by modelo,ano ORDER BY modelo")
    modelos = conn.execute(query).fetchall()
    # conn.close()

    modelos = [tuple(row) for row in modelos] # Transforma Objeto 'row' em 'tuple' para poder ser formatado em json
    return jsonify(modelos, 200)

if __name__ == '__main__':
    app.run(debug=True)