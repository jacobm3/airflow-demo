echo -n "State: "
aws ec2 describe-instances --instance-ids $(terraform output --raw instance_id) \
 | jq -r ".Reservations[] | .Instances[] | .State.Name"
