from random import randint, choice
from pprint import pprint
from json import dump, dumps
from subprocess import Popen
from csv import writer


# =========== CARROCERIA ===========

material_carroceria = ['AÇO',
                       'FIBRA DE CARBONO',
                       'FIBRA DE VIDRO',
                       'ALUMÍNIO']

tipo_carroceria = ['SEDAN',
                   'COUPÉ',
                   'HATCH',
                   'SUV',
                   'PICAPE']

alturas_carroceria = {'SEDAN': 1500,
                      'COUPÉ': 1350,
                      'HATCH': 1400,
                      'SUV': 1700,
                      'PICAPE': 1900}

larguras_carroceria = {'SEDAN': 1690,
                      'COUPÉ': 1660,
                      'HATCH': 1800,
                      'SUV': 1820,
                      'PICAPE': 1900}

blindagem_carroceria = [0,1]

cor_carroceria = ['VERMELHO',
         'VERDE',
         'AMARELO',
         'AZUL',
         'PRATA',
         'PRETO',
         'BRANCO']

qtd_farol = [4,6,8,12]

mod_farol = ['LED','XENON','NORMAL']

# =========== ELETRICA ===========

mod_chicote = {'SEDAN': 'CHICSEDAN20190001',
               'COUPÉ': 'CHICCOUPE20190001',
               'HATCH': 'CHICHATCH20190001',
               'SUV': 'CHICSUV20190001',
               'PICAPE': 'CHICPICAPE20190001'}

qtd_sensores = {'SEDAN': 6,
                'COUPÉ': 8,
                'HATCH': 6,
                'SUV': 10,
                'PICAPE': 12}

inj_eletronica = [0,1]

bateria = {'SEDAN': '50aH',
           'COUPÉ': '75aH',
           'HATCH': '50aH',
           'SUV': '60aH',
           'PICAPE': '70aH'}

# =========== INTERIOR ===========

volantes = ['VOLMOD0001','VOLMOD0002']

painel = {'SEDAN': 'PAINSEDAN20190001',
          'COUPÉ': 'PAINCOUPE20190001',
          'HATCH': 'PAINHATCH20190001',
          'SUV': 'PAINSUV20190001',
          'PICAPE': 'PAINPICAPE20190001'}

bancos = ['COURO','TECIDO']

mod_mostradores = {'SEDAN': 'MOSTRSEDAN20190001',
                   'COUPÉ': 'MOSTRCOUPE20190001',
                   'HATCH': 'MOSTRHATCH20190001',
                   'SUV': 'MOSTRSUV20190001',
                   'PICAPE': 'MOSTRPICAPE20190001'}

mod_comp_bordo = {'SEDAN': 'COMPBORSEDAN20190001',
                   'COUPÉ': 'COMPBORCOUPE20190001',
                   'HATCH': 'COMPBORHATCH20190001',
                   'SUV': 'COMPBORSUV20190001',
                   'PICAPE': 'COMPBORPICAPE20190001'}

mod_sist_ac = {'SEDAN': 'SISTACSEDAN20190001',
               'COUPÉ': 'SISTACCOUPE20190001',
               'HATCH': 'SISTACHATCH20190001',
               'SUV': 'SISTACSUV20190001',
               'PICAPE': 'SISTACPICAPE20190001'}


# =========== MOTOR ===========

tipo_motor = {'SEDAN': '1.6_16V',
              'COUPÉ': '1.6_16V',
              'HATCH': '1.0_16V',
              'SUV': '2.0_16V',
              'PICAPE': '2.5_24V'}

qtd_cilindros = {'SEDAN': 4,
                 'COUPÉ': 4,
                 'HATCH': 4,
                 'SUV': 4,
                 'PICAPE': 6}


qtd_potencia = {'SEDAN': 116,
                'COUPÉ': 122,
                'HATCH': 67,
                'SUV': 166,
                'PICAPE': 190}

qtd_litragem = {'SEDAN': '1.6',
                'COUPÉ': '1.6',
                'HATCH': '1.0',
                'SUV': '1.8',
                'PICAPE': '2.4'}

qtd_valvulas = {'SEDAN': 16,
                'COUPÉ': 16,
                'HATCH': 16,
                'SUV': 16,
                'PICAPE': 24}

qtd_torque = {'SEDAN': 19,
              'COUPÉ': 16.3,
              'HATCH': 9,
              'SUV': 20,
              'PICAPE': 43}

sobrealim = {'SEDAN': 'ASPIRADO',
             'COUPÉ': 'TURBO',
             'HATCH': 'ASPIRADO',
             'SUV': 'TURBO',
             'PICAPE': 'SUPERCHARGER'}

escape = {'SEDAN': 'SAIDA UNICA',
          'COUPÉ': 'SAIDA DUPLA TRASEIRA',
          'HATCH': 'SAIDA UNICA',
          'SUV': 'SAIDA DUPLA TRASEIRA',
          'PICAPE': 'SAIDA DUPLA TRASEIRA'}

# =========== RODAS ============

aro = {'SEDAN': 18,
       'COUPÉ': 17,
       'HATCH': 17,
       'SUV': 20,
       'PICAPE': 17}

tala_pneu = {'SEDAN': 205,
             'COUPÉ': 205,
             'HATCH': 205,
             'SUV': 225,
             'PICAPE': 265}

cor_roda = ['PRETO','PRATA']

# =========== TRANSMISSAO ===========

tipo_transmissao = ['MANUAL','AUTOMATICO','AUTOMATIZADO']

num_marchas = {'SEDAN': 7,
               'COUPÉ': 6,
               'HATCH': 6,
               'SUV': 6,
               'PICAPE': 8}

tracao = {'SEDAN': '2x4',
          'COUPÉ': '4x4',
          'HATCH': '2x4',
          'SUV': '2x4',
          'PICAPE': '4x4'}

# =========== VIDROS ===========

modelo_vidro = {'SEDAN': 'VIDROSEDAN20190001',
                'COUPÉ': 'VIDROCOUPE20190001',
                'HATCH': 'VIDROHATCH20190001',
                'SUV': 'VIDROSUV20190001',
                'PICAPE': 'VIDROPICAPE20190001'}

blindagem_vidro = [0,1]

opacidade = ['G5','G20','G35','G50']

# =========== STATUS ===========

status = ['EM PRODUÇÃO','NÃO ESTÁ EM PRODUÇÃO']


# =========== INSERTS DATAMARTS===========

with open('datamarts.sql', 'w+') as datamart:

    # CARROCERIA
    carroceria_mongo = []
    for modelo in tipo_carroceria:
        for material in material_carroceria:
            for blindagem in blindagem_carroceria:
                for cor in cor_carroceria:
                    for q_farol in qtd_farol:
                        for m_farol in mod_farol:

                            rndStatus = status[randint(0,1)];
                            datamart.write(f"INSERT INTO CARROCERIA (MATERIAL,TIPO,ALTURA,LARGURA,BLINDAGEM,COR,QTD_FAROL,MOD_FAROL,STATUS) VALUES ('{material}','{modelo}',{alturas_carroceria[modelo]},{larguras_carroceria[modelo]},{blindagem},'{cor}',{q_farol},'{m_farol}','{rndStatus}');\n")

                            carroceria_mongo.append({
                                "material": material,
                                "tipo": modelo,
                                "altura": alturas_carroceria[modelo],
                                "largura": larguras_carroceria[modelo],
                                "blindagem": blindagem,
                                "cor": cor,
                                "qtd_farol": q_farol,
                                "mod_farol": m_farol,
                                "status": rndStatus
                            })


    # ELETRICA
    eletrica_mongo = []
    for modelo in tipo_carroceria:
        for inj in inj_eletronica:

            rndStatus = status[randint(0,1)]
            datamart.write(f"INSERT INTO ELETRICA (MOD_CHICOTE,QTD_SENSORES,INJ_ELETRONICA,BATERIA,STATUS) VALUES ('{mod_chicote[modelo]}',{qtd_sensores[modelo]},{inj},'{bateria[modelo]}','{rndStatus}');\n")

            eletrica_mongo.append({
                    "mod_chicote": mod_chicote[modelo],
                    "qtd_sensores": qtd_sensores[modelo],
                    "inj_eletronica": inj,
                    "bateria": bateria[modelo],
                    "status": rndStatus
            })


    # INTERIOR
    interior_mongo = []
    for modelo in tipo_carroceria:
        for volante in volantes:
            for banco in bancos:

                rndStatus = status[randint(0,1)]
                datamart.write(f"INSERT INTO INTERIOR (VOLANTE,PAINEL,BANCOS,MOD_MOSTRADORES,MOD_COMP_BORDO,MOD_SIST_AC,STATUS) VALUES ('{volante}','{painel[modelo]}','{banco}','{mod_mostradores[modelo]}','{mod_comp_bordo[modelo]}','{mod_sist_ac[modelo]}','{rndStatus}');\n")

                interior_mongo.append({
                        "volante": volante,
                        "painel": painel[modelo],
                        "bancos": banco,
                        "mod_mostradores": mod_mostradores[modelo],
                        "mod_comp_bordo": mod_comp_bordo[modelo],
                        "mod_sist_ac": mod_sist_ac[modelo],
                        "status": rndStatus
                })

    # MOTOR
    motor_mongo = []
    for modelo in tipo_carroceria:

        rndStatus = status[randint(0,1)]
        datamart.write(f"INSERT INTO MOTOR (TIPO,QTD_CILINDROS,QTD_POTENCIA,QTD_LITRAGEM,QTD_VALVULAS,QTD_TORQUE,SOBREALIM,TIPO_ESCAPE,STATUS) VALUES ('{tipo_motor[modelo]}',{qtd_cilindros[modelo]},{qtd_potencia[modelo]},'{qtd_litragem[modelo]}',{qtd_valvulas[modelo]},{qtd_torque[modelo]},'{sobrealim[modelo]}','{escape[modelo]}','{rndStatus}');\n")

        motor_mongo.append({
                "tipo": tipo_motor[modelo],
                "qtd_cilindros": qtd_cilindros[modelo],
                "qtd_potencia": qtd_potencia[modelo],
                "qtd_litragem": qtd_litragem[modelo],
                "qtd_valvulas": qtd_valvulas[modelo],
                "qtd_torque": qtd_torque[modelo],
                "sobrealim": sobrealim[modelo],
                "tipo_escape": escape[modelo],
                "status": rndStatus
        })

    # RODAS
    rodas_mongo = []
    for modelo in tipo_carroceria:
        for cor in cor_roda:

            rndStatus = status[randint(0,1)]
            datamart.write(f"INSERT INTO RODAS (ARO,TALA_PNEU,COR,STATUS) VALUES ({aro[modelo]},{tala_pneu[modelo]},'{cor}','{rndStatus}');\n")

            rodas_mongo.append({
                    "aro": aro[modelo],
                    "tala": tala_pneu[modelo],
                    "cor": cor,
                    "status": rndStatus
            })

    # TRANSMISSAO
    transmissao_mongo = []
    for modelo in tipo_carroceria:
        for transmissao in tipo_transmissao:

            rndStatus = status[randint(0,1)]
            datamart.write(f"INSERT INTO TRANSMISSAO (TIPO,NUM_MARCHAS,TRACAO,STATUS) VALUES ('{transmissao}',{num_marchas[modelo]},'{tracao[modelo]}','{rndStatus}');\n")

            transmissao_mongo.append({
                    "tipo": transmissao,
                    "num_marchas": num_marchas[modelo],
                    "tracao": tracao[modelo],
                    "status": rndStatus
            })

    # VIDROS
    vidros_mongo = []
    for modelo in tipo_carroceria:
        for opac in opacidade:
            for blindagem in blindagem_vidro:

                rndStatus = status[randint(0,1)]
                datamart.write(f"INSERT INTO VIDROS (MODELO,BLINDAGEM,OPACIDADE,STATUS) VALUES ('{modelo_vidro[modelo]}',{blindagem},'{opac}','{rndStatus}');\n")

                vidros_mongo.append({
                        "modelo": modelo_vidro[modelo],
                        "blindagem": blindagem,
                        "opacidade": opac,
                        "status": rndStatus
                })


# =========== INSERTS TABELA DE FATOS ===========

carrocerias_sedan = list(range(1,673))
carrocerias_coupe = list(range(673,1345))
carrocerias_hatch = list(range(1345,2017))
carrocerias_suv = list(range(2017,2689))
carrocerias_picape = list(range(2689,3361))
lista_modelos = [carrocerias_sedan,carrocerias_coupe,carrocerias_hatch,carrocerias_suv,carrocerias_picape]

eletrica_sedan = [1, 2]
eletrica_coupe = [3, 4]
eletrica_hatch = [5, 6]
eletrica_suv = [7, 8]
eletrica_picape = [9, 10]

interior_sedan = list(range(1, 5))
interior_coupe = list(range(5, 9))
interior_hatch = list(range(9, 13))
interior_suv = list(range(13, 17))
interior_picape = list(range(17, 20))

motor_sedan = 1
motor_coupe = 2
motor_hatch = 3
motor_suv = 4
motor_picape = 5

rodas_sedan = [1, 2]
rodas_coupe = [3, 4]
rodas_hatch = [5, 6]
rodas_suv = [7, 8]
rodas_picape = [9, 10]

transmissao_sedan = list(range(1, 4))
transmissao_coupe = list(range(4, 7))
transmissao_hatch = list(range(7, 10))
transmissao_suv = list(range(10, 13))
transmissao_picape = list(range(13, 16))

vidro_sedan = list(range(1, 9))
vidro_coupe = list(range(9, 17))
vidro_hatch = list(range(17, 25))
vidro_suv = list(range(25, 33))
vidro_picape = list(range(33, 41))

document_list = []
with open('mass_tabela_fatos.csv', 'w+') as mass:
    with open('mass_mongol.json', 'w+') as mass_mongo:

        mass_writer = writer(mass, delimiter=';')

        for i in range(2500000):
            modelo = choice(choice(lista_modelos))

            if modelo in carrocerias_sedan:
                carroceria = choice(carrocerias_sedan)
                eletrica = choice(eletrica_sedan)
                interior = choice(interior_sedan)
                motor = motor_sedan
                rodas = choice(rodas_sedan)
                transmissao = choice(transmissao_sedan)
                vidros = choice(vidro_sedan)

            elif modelo in carrocerias_coupe:
                carroceria = choice(carrocerias_coupe)
                eletrica = choice(eletrica_coupe)
                interior = choice(interior_coupe)
                motor = motor_coupe
                rodas = choice(rodas_coupe)
                transmissao = choice(transmissao_coupe)
                vidros = choice(vidro_coupe)

            elif modelo in carrocerias_hatch:
                carroceria = choice(carrocerias_hatch)
                eletrica = choice(eletrica_hatch)
                interior = choice(interior_hatch)
                motor = motor_hatch
                rodas = choice(rodas_hatch)
                transmissao = choice(transmissao_hatch)
                vidros = choice(vidro_hatch)

            elif modelo in carrocerias_suv:
                carroceria = choice(carrocerias_suv)
                eletrica = choice(eletrica_suv)
                interior = choice(interior_suv)
                motor = motor_suv
                rodas = choice(rodas_suv)
                transmissao = choice(transmissao_suv)
                vidros = choice(vidro_suv)

            elif modelo in carrocerias_picape:
                carroceria = choice(carrocerias_picape)
                eletrica = choice(eletrica_picape)
                interior = choice(interior_picape)
                motor = motor_picape
                rodas = choice(rodas_picape)
                transmissao = choice(transmissao_picape)
                vidros = choice(vidro_picape)

            modelo_carro = f"{carroceria}-{motor}-{eletrica}-{rodas}-{vidros}-{transmissao}-{interior}"

            mass_writer.writerow([modelo_carro, carroceria, motor, eletrica, rodas, vidros, transmissao, interior])

            document_list.append({"carroceria": carroceria_mongo[carroceria - 1],
                                  "eletrica": eletrica_mongo[eletrica - 1],
                                  "interior": interior_mongo[interior - 1],
                                  "motor": motor_mongo[motor - 1],
                                  "rodas": rodas_mongo[rodas - 1],
                                  "transmissao": transmissao_mongo[transmissao - 1],
                                  "vidros": vidros_mongo[vidros - 1],
                                  "modelo": modelo_carro})

        dump(document_list, mass_mongo, ensure_ascii=False)
