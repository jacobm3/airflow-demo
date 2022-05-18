aws ec2 start-instances --instance-ids $(terraform output --raw instance_id)

sleep 5

terraform apply
