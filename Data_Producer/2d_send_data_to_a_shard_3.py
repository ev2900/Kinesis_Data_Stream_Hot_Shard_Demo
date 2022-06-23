# ---------------
# If required ...
# 
# pip install boto3
# pip install json
# pip install time
# pip install random
#
# ---------------

# Import req. libraries
import json
import boto3
import time
import random

# Configure a permanent session
'''
client = boto3.client(
	'kinesis',
	aws_access_key_id="<access_key_id>",
    aws_secret_access_key="<secret_key_id>"
)
'''

# Set hash value for messages
hashkeyvalue = "255211775190703847597530955573826158593"

# Create a kinesis client
client = boto3.client('kinesis')

# Set kinesis stream name variable
kinesisDataStreamName = "hot-shard-data-stream"

# Set number of messages to send variable
numberOfMessagesToSend = 1000000

# Create the message that will be send to Kinesis
messageBody = {
	"messageBody": "sample message from Cloud9"
}

# Send messages to Kinesis data stream
counter = 0

for message in range(0, numberOfMessagesToSend):
	
	# Send message to Kinesis DataStream
	response = client.put_record(
		StreamName = kinesisDataStreamName,
		Data = json.dumps(messageBody),
		PartitionKey = str(hash(range(0,1))),
		ExplicitHashKey = hashkeyvalue # shard 3
	)

	print("Message # " + str(counter) + " sent to " + str(response['ShardId']))
	
	counter = counter + 1
	
	time.sleep(random.uniform(2, 15))

	# If the message was not sucssfully sent print an error message
	if response['ResponseMetadata']['HTTPStatusCode'] != 200:
		print('Error!')
		print(response)
