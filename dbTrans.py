import boto3

def dbPartitionKey(assetChart, time):
    partitionKey = assetChart + time
    return partitionKey

def buyOrder(assetChart, time, response):
    dynamodb = boto3.client('dynamodb')

    partitionKey = dbPartitionKey(assetChart, time)
    timestamp =  float(response['timestamp'])
    qty = float(response['original_amount'])
    price = float(response['price'])
    sold = False

    item = {
        'assetchart': partitionKey,
        'timestamp': timestamp,
        'qty': qty,
        'price': price,
        'sold': sold
    }

    # Add the item to the database
    response = dynamodb.put_item(
        TableName='Gemini_Trades',
        Item=item
    )
    
    # Print the response
    print(response)

def sellOrder(assetChart, time):
    # Create a DynamoDB client
    dynamodb = boto3.client('dynamodb')

    partitionKey = dbPartitionKey(assetChart, time)
    
    # Define the query parameters
    query_params = {
        'TableName': 'Gemini_Trades',
        'KeyConditionExpression': 'partitionKey = :pk',
        'ExpressionAttributeValues': {
            ':pk': {'S': partitionKey}
        },
        'ScanIndexForward': False,
        'Limit': 1
    }
    
    # Query the database
    response = dynamodb.query(**query_params)
    
    # Extract the item with the highest timestamp
    item = response['Items'][0] if 'Items' in response else None
    
    # Print the item
    print(item)