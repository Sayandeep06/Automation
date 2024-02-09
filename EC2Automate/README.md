Lambda function to check on instances and restart them if they stopped running

We used Event Bridge to call Lambda function every 1 hr then use the

Boto3 sdk inside the lambda function to talk to EC2

Edit the execution role in lambda function to give permission

to talk to EC2

Change timeout config to 20+ secs in lambda

Add a trigger to the lambda function and set it to event-bridge

Schedule expressions to use cron jobs on Event Bridge and set the Schedule Expression to

cron(0/60***?*)

then add