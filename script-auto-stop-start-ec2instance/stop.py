import json
import boto3

# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g., 'us-east-1'
region = 'us-east-1'

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)

	# Enter tag name of Stop
    filter = [{'Name': 'tag:Stop', 'Values': ['yes']}]

    instances = ec2.describe_instances(Filters=filter)

    #ec2.stop_instances(InstanceIds=instances)

    # Get instance ID
    instancesid = instances.get('Reservations')[0].get('Instances')[0].get('InstanceId')
    stop_instances = []
    stop_instances.append(instancesid)

    # Stop instance
    ec2.stop_instances(InstanceIds=stop_instances)
    print('Instances Stopped ' + str(instancesid))
