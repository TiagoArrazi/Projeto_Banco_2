from pymongo import MongoClient
from pymysql import connect
from flask import Flask, render_template
from json import dump
import time

app = Flask(__name__)  # flask application


@app.route('/mysql')
def get_from_mysql():
    mysql_conn = connect('localhost', 'banco_2', '123456', 'PROJETO_BANCO_2')  # MySQL connection

    with mysql_conn:

        query = """SELECT C.MODELO AS 'MODELO CARRO',CRC.TIPO AS 'TIPO CARROCERIA',CRC.STATUS AS 'STATUS CARROCERIA'
                   FROM CARRO AS C
                   INNER JOIN CARROCERIA AS CRC
                   WHERE (CRC.COR = 'VERMELHO' OR CRC.COR = 'PRATA') AND CRC.ID_CARROCERIA = C.ID_CARROCERIA
                   ORDER BY C.MODELO;"""

        cursor = mysql_conn.cursor()

        start = time.time()

        cursor.execute(query)

        response = cursor.fetchall()

        end = time.time()

        with open('mysql_response', 'w+') as mysql_resp:
            mysql_resp.write(
                'MODELO | TIPO CARROCERIA | STATUS CARROCERIA\n\n'
            )
            for element in response:
                mysql_resp.write("{}\n".format(str(element)))

    return '< QUERY PROCESSED > --- {} lines in {} seconds'.format(len(response), end - start)


@app.route('/mongodb')
def get_from_mongodb():

    mongo_client = MongoClient('localhost', 27017)  # MongoDB client creation
    db = mongo_client['carros_db']  # MongoDB database selection
    carros = db['carros']

    # cor_match = {"$match": {"$or": [{"carroceria.cor": "VERMELHO"},
    #                                 {"carroceria.cor": "PRATA"}]
    #                         }
    #              }
    #
    # sort = {"$sort": {"modelo": 1}}
    #
    # project = {"$project": {
    #     "_id": 0,
    #     "MODELO CARRO": "$modelo",
    #     "TIPO CARROCERIA": "$carroceria.tipo",
    #     "STATUS CARROCERIA": "$carroceria.status"}}
    #
    # start = time.time()
    #
    # print('Executing aggregation...')
    # results = list(carros.aggregate([cor_match, sort, project]))
    #
    # end = time.time()

    # with open('mongodb_response.json', 'w+') as mongo_resp:
    #     dump(list(results), mongo_resp)

    # return '< AGGREGATION PROCESSED > --- {} documents in {} seconds'.format(len(results), end - start)

    cor_match = {"$match": {"$or": [
        {"carroceria.cor": "VERMELHO"},
        {"carroceria.cor": "PRATA"}]}}

    sort = {"$sort": {"modelo": 1}}
    count = {"$count": "contador"}

    project = {"$project": {
        "_id": 0,
        "MODELO CARRO": "$modelo",
        "TIPO CARROCERIA": "$carroceria.tipo",
        "STATUS CARROCERIA": "$carroceria.status"}}

    start = time.time()
    cursor = carros.aggregate([cor_match, sort, project])
    end = time.time()
    tempo = end - start

    carros_html = carros.aggregate([cor_match, {"$limit": 10}, sort, project])
    carros_count_doc = db.command({"aggregate": "carros",
                                   "pipeline": [cor_match, sort, count],
                                   "cursor": {}})

    return render_template('mongodb.html',
                           carrosHtml=list(carros_html),
                           carrosCount=carros_count_doc["cursor"]["firstBatch"][0]["contador"],
                           time=tempo)


if __name__ == '__main__':
    app.run(debug=True)
