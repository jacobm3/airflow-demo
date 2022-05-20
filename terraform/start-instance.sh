#!/bin/bash -x 

aws ec2 start-instances --instance-ids $(terraform output --raw airflow_instance_id)
aws ec2 start-instances --instance-ids $(terraform output --raw vault_instance_id)

sleep 5

terraform apply
