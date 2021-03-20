import json
import boto3

# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g., 'us-east-1'
region = 'us-east-1'

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)

    # Enter tag name of Start
    filter = [{'Name': 'tag:Start', 'Values': ['yes']}]

    instances = ec2.describe_instances(Filters=filter)

    #ec2.start_instances(InstanceIds=instances)

    # Get instance ID
    instancesid = instances.get('Reservations')[0].get('Instances')[0].get('InstanceId')
    start_instances = []
    start_instances.append(instancesid)

    # Start instance
    ec2.start_instances(InstanceIds=start_instances)
    print('Instances Started ' + str(instancesid))
