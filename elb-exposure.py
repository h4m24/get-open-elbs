import boto3

ElbClient = boto3.client('elb')
SgClient = boto3.client('ec2')

for ElbDocument in ElbClient.describe_load_balancers()['LoadBalancerDescriptions']:

    if ElbDocument['Scheme'] == "internet-facing":


        for SgCidr in SgClient.describe_security_groups(GroupIds=ElbDocument['SecurityGroups'])['SecurityGroups'][0]['IpPermissions'][0]['IpRanges']:
            if SgCidr['CidrIp'] == "0.0.0.0/0":
                print("\n")
                print(ElbDocument['LoadBalancerName'])
                print(SgCidr['CidrIp'])




