import os
import json

# Run AWS CLI command
cmd_output = os.popen('aws kinesis describe-stream --stream-name hot-shard-data-stream')
shard_info_raw = cmd_output.read()

# Convert output to JSON
json_object = json.loads(shard_info_raw)


# Get each shard info
print('--')

for shard in json_object["StreamDescription"]["Shards"]:
    print('ShardId = ' + shard["ShardId"])
    print('Start Hashkey = ' + shard["HashKeyRange"]["StartingHashKey"])
    print('End Hashkey = ' + shard["HashKeyRange"]["EndingHashKey"])
    print('--')