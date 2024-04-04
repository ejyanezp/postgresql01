import os
import utilities
import psycopg2
import traceback

# Crear la conexión con la BD
location = os.environ.get('DB_CONNECTION_PARAMS', '/dev/postgresql')
conn_params = utilities.get_parameters([location])
conn = psycopg2.connect(host=conn_params['host'], database=conn_params['database'],
                        user=conn_params['username'], password=conn_params['password'])


def lambda_handler(event, context):
    try:
        with conn.cursor() as cur:
            cur.execute(f'SELECT * FROM "Employee" where id =\'{event["id"]}\'')
            results = cur.fetchall()
            cur.close()
            # conexion.close()   ## Por qué no la cierro?
    except (Exception, psycopg2.DatabaseError) as error:
        traceback.print_exc()
        #  Realizamos rollback en caso de que el query  falle, para poder seguir haciendo querys con la conexion
        conn.rollback()
        # Levantar una excepción más genérica para que frontend no conozca la causa precisa del error
        # para evitar que los hackers obtengan información
        raise RuntimeError('HTTP 500. Error de ejecución')
    return results
