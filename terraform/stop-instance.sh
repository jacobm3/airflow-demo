aws ec2 stop-instances --instance-ids $(terraform output --raw airflow_instance_id)
