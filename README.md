# Kinesis Data Stream CloudWatch

<img width="275" alt="map-user" src="https://img.shields.io/badge/cloudformation template deployments-0-blue"> <img width="85" alt="map-user" src="https://img.shields.io/badge/views-204-green"> <img width="125" alt="map-user" src="https://img.shields.io/badge/unique visits-075-green">

A demo that will intially deploy a Kinesis data stream with 4 shards and sample python scripts run in Cloud9 that purposly send a higher volume of messages to a single shard on Kinesis. This sets up a scenario with where a Kinesis data stream has a *hot* shard. Subseqently you enable enhanced monitoring on the Kinesis data stream and deploy a CloudWatch dashboard to identify the *hot* shard

## Instructions

1. Deploy CloudFormation for Kinesis + Cloud9

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=kinesis-cloud9&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/kinesis_Cloud9.yaml)

The CloudFormation will deploy the following architecture

<img width="400" alt="OpenSearch_demo_VPC_Architecture" src="https://github.com/ev2900/Kinesis_Data_Stream_Hot_Shard_Demo/blob/main/Architecture/architecture-diagram.png">

2. Enable enhanced shard-level metrics on the Kinesis data stream

* Navigate to the [Kinesis Data Stream Console](https://us-east-1.console.aws.amazon.com/kinesis/home?region=us-east-1#/streams/list)
* Click on *hot-shard-data-stream*
* Navigate to the *Configuration* tab
* Enable all *Enhanced (shard-level) metrics*

3. Send data to Kinesis via. Python scripts in Cloud9
* Navigate to the [Cloud9 console](https://us-east-1.console.aws.amazon.com/cloud9/home?region=us-east-1#)
* Click on the *kinesis-cloud9* enviorment
* Run each script in a seperate Cloud9 terminal
  * ```python Kinesis_Data_Stream_Monitoring/Data_Producer/2a_send_data_to_a_shard_0.py```
  * ```python Kinesis_Data_Stream_Monitoring/Data_Producer/2b_send_data_to_a_shard_1.py```
  * ```python Kinesis_Data_Stream_Monitoring/Data_Producer/2c_send_data_to_a_shard_2.py```
  * ```python Kinesis_Data_Stream_Monitoring/Data_Producer/2d_send_data_to_a_shard_3.py```

4. Deploy CloudWatch dashboard

The CloudFormation will deploy a CloudWatch dashboard

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=cloudwatch-dashboard&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/cloud_watch_dashboard.yaml)

The cloudwatch dashboard will produce a graph that looks something like the image below. Notice that the message count is higher for shard-0000 ... compared to the other shards

<img width="739" alt="cloud_watch_chart" src="https://user-images.githubusercontent.com/5414004/175348018-cf4f2db4-92e4-404d-8302-c3a379ca123f.png">

shard-0000 ... is our hot shard!
