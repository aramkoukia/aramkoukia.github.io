---
layout: post
title: "Save cost of AWSEC2 by turning off and on instances based on a schedule"
date: 2023-01-17
description: "ou can use AWS Auto Scaling or AWS Lambda to schedule the start and stop of your EC2 instances."
image: https://cdn-images-1.medium.com/max/800/0*RWfxDi1PaZ7jNqDv.png
medium_url: https://medium.com/@aramkoukia/save-cost-of-awsec2-by-turning-off-and-on-instances-based-on-a-schedule-ba1853c4e828
---

### Save cost of AWS EC2 by turning off and on instances based on a schedule

![](https://cdn-images-1.medium.com/max/800/0*RWfxDi1PaZ7jNqDv.png)*Image from GeekWire.com*

ou can use AWS Auto Scaling or AWS Lambda to schedule the start and stop of your EC2 instances.

- AWS Auto Scaling allows you to automatically scale your Amazon EC2 instances based on a schedule. You can set up scheduled scaling actions that automatically increase or decrease the number of instances in your Auto Scaling group.
- AWS Lambda allows you to run code without provisioning or managing servers. You can use Lambda to schedule the start and stop of your EC2 instances. For example, you can create a Lambda function that starts and stops your instances on a schedule.

Additionally, you can also use EC2 Scheduler, a service which enables you to schedule the start and stop of your EC2 instances using Amazon CloudWatch Events and AWS Lambda, which is a serverless compute service.

Please note that, if you are using reserved instances, you may not want to stop and start instances as it would impact the availability of those instances and would not be cost effective.

Here’s an example of how you can use AWS Lambda and CloudWatch Events to stop and start your EC2 instances on a schedule:

1. Create a new Lambda function using the “AWS Lambda blueprint for Scheduled Events”
2. In the function’s code, you can use the AWS SDK for Python (Boto3) to stop and start your instances

```
import boto3def lambda_handler(event, context):    ec2 = boto3.client('ec2')    # Replace the instance ID with your own    instance_id = 'i-1234567890abcdef0'    if event['action'] == 'stop':        ec2.stop_instances(InstanceIds=[instance_id])    elif event['action'] == 'start':        ec2.start_instances(InstanceIds=[instance_id])
```

In the CloudWatch Events, create a new rule and set the schedule to when you want the instances to start and stop. For example, to stop the instance at 9pm and start it again at 6am the next day, you can use the following cron expressions:

- `cron(0 21 * * ? *)` for stopping instances
- `cron(0 6 * * ? *)` for starting instances

In the CloudWatch Events, configure the target of the rule to be the Lambda function you created.

This is a simple example of how you can use Lambda and CloudWatch Events to stop and start your instances on a schedule. You can also add more instances and use tags to target multiple instances at once.

Please note that you should have the appropriate permissions set up in your AWS IAM roles to be able to execute EC2 actions.
