#!/bin/bash

echo "Generating data..."
echo ""

mkdir -p MySQL/Datamarts
mkdir -p MySQL/Facts_Table

mkdir -p MongoDB/MongoDB_Mass

python3 DataMassGenerator.py


echo ""
echo ""


echo "Creating DB in MySQL..."
echo ""

echo "source mk_indexed_db.sql;" | mysql


echo "Filling Datamarts in MySQL..."
echo ""

echo "LOAD DATA LOCAL INFILE 'MySQL/Datamarts/datamart_carroceria.csv' INTO TABLE PROJETO_BANCO_2. FIELDS TERMINATED BY ';' (MATERIAL, TIPO, ALTURA, LARGURA, BLINDAGEM, COR, QTD_FAROL, MOD_FAROL, STATUS)" | sudo mysql
echo "LOAD DATA LOCAL INFILE 'MySQL/Datamarts/datamart_eletrica.csv' INTO TABLE PROJETO_BANCO_2. FIELDS TERMINATED BY ';' (MOD_CHICOTE, QTD_SENSORES, INJ_ELETRONICA, BATERIA, STATUS)" | sudo mysql
echo "LOAD DATA LOCAL INFILE 'MySQL/Datamarts/datamart_interior.csv' INTO TABLE PROJETO_BANCO_2. FIELDS TERMINATED BY ';' (VOLANTE, PAINEL, BANCOS, MOD_MOSTRADORES, MOD_COMP_BORDO, MOD_SIST_AC, STATUS)" | sudo mysql
echo "LOAD DATA LOCAL INFILE 'MySQL/Datamarts/datamart_motor.csv' INTO TABLE PROJETO_BANCO_2. FIELDS TERMINATED BY ';' (TIPO, QTD_CILINDROS, QTD_POTENCIA, QTD_LITRAGEM, QTD_VALVULAS, QTD_TORQUE, SOBREALIM, TIPO_ESCAPE, STATUS)" | sudo mysql
echo "LOAD DATA LOCAL INFILE 'MySQL/Datamarts/datamart_rodas.csv' INTO TABLE PROJETO_BANCO_2. FIELDS TERMINATED BY ';' (ARO, TALA_PNEU, COR, STATUS)" | sudo mysql	
echo "LOAD DATA LOCAL INFILE 'MySQL/Datamarts/datamart_transmissao.csv' INTO TABLE PROJETO_BANCO_2. FIELDS TERMINATED BY ';' (TIPO, NUM_MARCHAS, TRACAO, STATUS)" | sudo mysql
echo "LOAD DATA LOCAL INFILE 'MySQL/Datamarts/datamart_vidros.csv' INTO TABLE PROJETO_BANCO_2. FIELDS TERMINATED BY ';' (MODELO, BLINDAGEM, OPACIDADE, STATUS)" | sudo mysql


echo ""
echo ""


echo "Filling Facts Table in MySQL..."

echo "SET bulk_insert_buffer_size = 1024 * 1024 * 256; LOAD DATA LOCAL INFILE 'MySQL/Facts_Table/mass_tabela_fatos.csv' INTO TABLE PROJETO_BANCO_2.CARRO FIELDS TERMINATED BY ';' (MODELO, ID_CARROCERIA, ID_MOTOR, ID_ELETRICA, ID_RODAS, ID_VIDROS, ID_TRANSMISSAO, ID_INTERIOR);" | sudo mysql


echo ""
echo ""


echo "Creating DB in MongoDB..."
echo "use carros_db" | mongo

echo "Loading data into MongoDB ..."
mongoimport --jsonArray -d 'carros_db' -c 'carros' MongoDB/MongoDB_Mass/mass_mongo.json

