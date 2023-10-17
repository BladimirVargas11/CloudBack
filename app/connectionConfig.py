import pymysql
import sys
import boto3
import os

ENDPOINT="xtremelab-db.clxwodsgcd1d.us-east-2.rds.amazonaws.com"
PORT=3306
USER="admin"
REGION="us-east-2"
DBNAME="filesdb"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets las credenciales de .aws/credentials
session = boto3.Session(aws_access_key_id="AKIAXGYRZECKWFDZH56L",
                        aws_secret_access_key="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",
                        region_name="us-east-2")
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)
def connect():
    try: 

        conn =  pymysql.connect(host=ENDPOINT,
                                user=USER,
                                passwd=token,
                                port=PORT,
                                database=DBNAME,
                                ssl_ca='./us-east-2-bundle.pem',
                                bind_address=ENDPOINT,connect_timeout=5)
        print("Conexion exitosa")
    except Exception as e:
        print("Database connection failed due to {}".format(e))
                