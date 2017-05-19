import boto3

ElbClient = boto3.client('elb')
SgClient = boto3.client('ec2')

for ElbDocument in ElbClient.describe_load_balancers()['LoadBalancerDescriptions']:

    if ElbDocument['Scheme'] == "internet-facing":
        print(ElbDocument['LoadBalancerName'])

        # print(SgClient.describe_security_groups(GroupIds=ElbDocument['SecurityGroups'])['SecurityGroups'][0]['IpPermissions'][0]['IpRanges'])
        for SgCidr in SgClient.describe_security_groups(GroupIds=ElbDocument['SecurityGroups'])['SecurityGroups'][0]['IpPermissions'][0]['IpRanges']:
            print(SgCidr['CidrIp'])
        print("\n")
        # break



