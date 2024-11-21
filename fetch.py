import json
import mysql.connector

def lambda_handler(event, context):
    connection = mysql.connector.connect(
        host="serverless.czwas2qmalmw.ap-south-1.rds.amazonaws.com",
        user="admin", 
        password="1q2w3e4r", 
        database="serverless"  
    )

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM serverless")
    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return data


#pip install mysql-connector-python