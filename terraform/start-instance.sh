aws ec2 start-instances --instance-ids $(terraform output --raw airflow_instance_id)

sleep 5

terraform apply
