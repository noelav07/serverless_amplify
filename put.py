import json
import mysql.connector

def lambda_handler(event, context):
    id = event['id']
    name = event['name']
    
    connection = mysql.connector.connect(
        host="serverless.czwas2qmalmw.ap-south-1.rds.amazonaws.com",
        user="admin", 
        password="1q2w3e4r", 
        database="serverless"  
    )
    
    cursor = connection.cursor()
    
    insert_query = """
        INSERT INTO serverless (id, name)
        VALUES (%s, %s)
    """
    values = (id, name)  
    
    try:
        cursor.execute(insert_query, values)
        connection.commit() 
        result_message = "Data Saved Successfully!"
    except Exception as e:
        connection.rollback() 
        result_message = f"Error saving data: {e}"
    finally:

        cursor.close()
        connection.close()
    
    return {
        'statusCode': 200 if "Successfully" in result_message else 500,
        'body': json.dumps(result_message)
    }
