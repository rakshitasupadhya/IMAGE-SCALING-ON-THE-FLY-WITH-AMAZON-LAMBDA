import os
import json
from io import BytesIO
from PIL import Image
import boto3

s3 = boto3.client('s3')
BUCKET = os.environ.get('BUCKET')
BUCKET_URL = os.environ.get('BUCKET_URL')

def lambda_handler(event, context):
    # Parse request parameters to get width, height, and bucket key
    #key = event['rawPath'][1:]
    #params = key.split('/')
    size = event['queryStringParameters']['size']
    path = event['queryStringParameters']['image']

    dimensions = size.split("x")
    width = int(dimensions[0])
    height = int(dimensions[1])

    # Fetch the original image from S3
    response = s3.get_object(Bucket=BUCKET, Key=path)
    original_image = response['Body'].read()

    # Resize the image using Pillow
    image = Image.open(BytesIO(original_image))
    image = image.resize((width, height), Image.LANCZOS)
    
    # Create a buffer to save the resized image
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)
    resized_image_data = buffer.read()
    new_key= "{size}_{key}".format(size=size, key=path)

    # Upload the resized image to S3
    resized_key = new_key
    s3.put_object(
        Body=resized_image_data,
        Bucket=BUCKET,
        Key=resized_key,
        ContentType="image/jpeg",
        ContentDisposition="inline"
    )

    # Generate the Lambda response
    response = {
        "statusCode": 301,
        "headers": {"location": f"{BUCKET_URL}/{resized_key}"},
        "body": ""
    }

    return response
