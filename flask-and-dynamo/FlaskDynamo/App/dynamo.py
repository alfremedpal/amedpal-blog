import boto3

def init_dynamo(table_name="FlaskDynamo"):
    dynamodb = boto3.resource(
        "dynamodb", 
        region_name="region", 
        aws_access_key_id="access_key", 
        aws_secret_access_key="secret_key")
    
    table = dynamodb.Table(table_name)
    
    return table