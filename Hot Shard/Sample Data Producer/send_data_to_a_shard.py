# Install boto3
'''
	pip install boto3
'''

# Import req. libraries
import json
import boto3

# Create a kinesis client
client = boto3.client('kinesis')

# Set kinesis stream name variable
kinesisDataStreamName = "hot-shard-demo"

# Set number of messages to send variable
numberOfMessagesToSend = 10

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
		ExplicitHashKey = "1" # shard 0
		# ExplicitHashKey = "113427455640312821154458202477256070486" # shard 1
		# ExplicitHashKey = "226854911280625642308916404954512140971" # shard 2
		# ...
	)

	print("Message # " + str(counter) + " sent to " + str(response['ShardId']))
	
	counter = counter + 1

	# If the message was not sucssfully sent print an error message
	if response['ResponseMetadata']['HTTPStatusCode'] != 200:
		print('Error!')
		print(response)
