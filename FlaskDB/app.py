from pymongo import MongoClient
from pymysql import connect
from flask import Flask, make_response
from json import dumps
import time

app = Flask(__name__)  # flask application

# ==================== MySQL connection ==================================

mysql_conn = connect('localhost', 'banco_2', '123456', 'PROJETO_BANCO_2')  # MySQL connection

# ==================== MongoDB client ====================================

mongo_client = MongoClient('localhost', 27017)  # MongoDB client creation
db = mongo_client['carros_db']  # MongoDB database selection
carros = db['carros']


@app.route('/mysql')
def get_from_mysql():
    with mysql_conn:
        query = """SELECT C.MODELO AS 'MODELO CARRO',CRC.TIPO AS 'TIPO CARROCERIA',CRC.STATUS AS 'STATUS CARROCERIA',
                   INTR.VOLANTE AS 'MODELO VOLANTE', INTR.BANCOS AS 'TIPO BANCO', TRNSM.TIPO AS 'TIPO TRANSMISSÃO'
                   FROM CARRO AS C  
                   INNER JOIN CARROCERIA AS CRC
                   INNER JOIN INTERIOR AS INTR
                   INNER JOIN TRANSMISSAO AS TRNSM
                   WHERE (CRC.ID_CARROCERIA = C.ID_CARROCERIA AND (CRC.COR = 'VERMELHO' OR CRC.COR = 'PRATA' 
                   OR CRC.COR = 'PRETO' OR CRC.COR = 'AZUL')) AND 
                   (INTR.ID_INTERIOR = C.ID_INTERIOR AND (INTR.BANCOS = 'COURO' OR INTR.BANCOS = 'TECIDO')) AND
                   (TRNSM.ID_TRANSMISSAO = C.ID_TRANSMISSAO AND 
                   (TRNSM.TIPO = 'AUTOMATICO' OR TRNSM.TIPO = 'AUTOMATIZADO')) 
                   ORDER BY C.MODELO;"""

        cursor = mysql_conn.cursor()

        start = time.time()

        cursor.execute(query)
        response = cursor.fetchall()

        end = time.time()

        with open('mysql_response', 'w+') as mysql_resp:
            mysql_resp.write(
                'MODELO | TIPO CARROCERIA | STATUS CARROCERIA | MODELO VOLANTE | TIPO BANCO | TIPO TRANSM.\n\n'
            )
            for element in response:
                mysql_resp.write("{}\n".format(str(element)))

    return '< QUERY PROCESSED > --- {} lines in {} seconds'.format(len(response), end - start)


@app.route('/mongodb')
def get_from_mongodb():

    color_match = {
            "$match": {
                "$or": [
                    {"carroceria.cor": "VERMELHO"},
                    {"carroceria.cor": "PRATE"},
                    {"carroceria.cor": "AZUL"},
                    {"carroceria.cor": "PRETO"}
                ]
            }
        }
    # limit = {"$limit": 10}
    #
    # sort = {
    #     "$sort": {
    #         "modelo": 1
    #     }
    # }
    #
    # project = {
    #
    #     "$project": {
    #         "_id": 0,
    #         "MODELO CARRO": "$modelo",
    #         "TIPO CARROCERIA": "$carroceria.tipo",
    #         "STATUS CARROCERIA": "$carroceria.status",
    #         "MODELO VOLANTE": "$interior.volante",
    #         "TIPO BANCO": "$interior.bancos"
    #     }
    # }

    start_find = time.time()
    # mongo_cursor = carros.aggregate([color_match])
    mongo_cursor = carros.find()
    end_find = time.time()

    start_count = time.time()
    count = len(list(mongo_cursor))
    end_count = time.time()

    start_write = time.time()
    with open('mongo_response', 'w+') as mongo_resp:
        for doc in list(mongo_cursor):
            mongo_resp.write(dumps(doc, default=str))
    end_write = time.time()

    response = make_response("""< QUERY PROCESSED > --- {} documents returned in {} seconds
                    --- {} seconds to count documents
                    --- {} seconds to write in file""".format(count,
                                                              end_find - start_find,
                                                              end_count - start_count,
                                                              end_write - start_write)
                             )

    response.headers["content-type"] = "text/plain"
    return response


if __name__ == '__main__':
    app.run(debug=True)
