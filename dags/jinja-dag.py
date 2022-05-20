
from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
with DAG(
    'jinja_dag_v00',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    description='DAG dynamically generated with jinja2',
    schedule_interval=timedelta(hours=6),
    start_date=datetime(2022, 5, 10),
    catchup=False,
    max_active_runs=1,
    tags=['example'],
) as dag:

    t0 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )



    t1 = BashOperator(
        task_id='t1_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t0 >> t1

  
    t1_1 = BashOperator(
        task_id='t1_1_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t1 >> t1_1

  
    t1_1_1 = BashOperator(
        task_id='t1_1_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_0
    t1_1 >> t1_1_1
    

  
    t1_1_2 = BashOperator(
        task_id='t1_1_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_1
    t1_1_1 >> t1_1_2
    

  
    t1_1_3 = BashOperator(
        task_id='t1_1_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_2
    t1_1_2 >> t1_1_3
    

  
    t1_1_4 = BashOperator(
        task_id='t1_1_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_3
    t1_1_3 >> t1_1_4
    

  
    t1_1_5 = BashOperator(
        task_id='t1_1_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_4
    t1_1_4 >> t1_1_5
    

  
    t1_1_6 = BashOperator(
        task_id='t1_1_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_5
    t1_1_5 >> t1_1_6
    

  
    t1_1_7 = BashOperator(
        task_id='t1_1_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_6
    t1_1_6 >> t1_1_7
    

  
    t1_1_8 = BashOperator(
        task_id='t1_1_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_7
    t1_1_7 >> t1_1_8
    

  
    t1_1_9 = BashOperator(
        task_id='t1_1_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_8
    t1_1_8 >> t1_1_9
    

  
    t1_1_10 = BashOperator(
        task_id='t1_1_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_9
    t1_1_9 >> t1_1_10
    

  
    t1_1_11 = BashOperator(
        task_id='t1_1_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_10
    t1_1_10 >> t1_1_11
    

  
    t1_1_12 = BashOperator(
        task_id='t1_1_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_11
    t1_1_11 >> t1_1_12
    

  
    t1_1_13 = BashOperator(
        task_id='t1_1_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_12
    t1_1_12 >> t1_1_13
    

  
    t1_1_14 = BashOperator(
        task_id='t1_1_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_13
    t1_1_13 >> t1_1_14
    

  
    t1_1_15 = BashOperator(
        task_id='t1_1_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_14
    t1_1_14 >> t1_1_15
    

  
    t1_1_16 = BashOperator(
        task_id='t1_1_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_15
    t1_1_15 >> t1_1_16
    

  
    t1_1_17 = BashOperator(
        task_id='t1_1_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_16
    t1_1_16 >> t1_1_17
    

  
    t1_1_18 = BashOperator(
        task_id='t1_1_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_17
    t1_1_17 >> t1_1_18
    

  
    t1_1_19 = BashOperator(
        task_id='t1_1_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_1,
    # else link to t1_1_18
    t1_1_18 >> t1_1_19
    

  
  
    t1_2 = BashOperator(
        task_id='t1_2_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t1 >> t1_2

  
    t1_2_1 = BashOperator(
        task_id='t1_2_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_0
    t1_2 >> t1_2_1
    

  
    t1_2_2 = BashOperator(
        task_id='t1_2_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_1
    t1_2_1 >> t1_2_2
    

  
    t1_2_3 = BashOperator(
        task_id='t1_2_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_2
    t1_2_2 >> t1_2_3
    

  
    t1_2_4 = BashOperator(
        task_id='t1_2_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_3
    t1_2_3 >> t1_2_4
    

  
    t1_2_5 = BashOperator(
        task_id='t1_2_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_4
    t1_2_4 >> t1_2_5
    

  
    t1_2_6 = BashOperator(
        task_id='t1_2_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_5
    t1_2_5 >> t1_2_6
    

  
    t1_2_7 = BashOperator(
        task_id='t1_2_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_6
    t1_2_6 >> t1_2_7
    

  
    t1_2_8 = BashOperator(
        task_id='t1_2_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_7
    t1_2_7 >> t1_2_8
    

  
    t1_2_9 = BashOperator(
        task_id='t1_2_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_8
    t1_2_8 >> t1_2_9
    

  
    t1_2_10 = BashOperator(
        task_id='t1_2_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_9
    t1_2_9 >> t1_2_10
    

  
    t1_2_11 = BashOperator(
        task_id='t1_2_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_10
    t1_2_10 >> t1_2_11
    

  
    t1_2_12 = BashOperator(
        task_id='t1_2_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_11
    t1_2_11 >> t1_2_12
    

  
    t1_2_13 = BashOperator(
        task_id='t1_2_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_12
    t1_2_12 >> t1_2_13
    

  
    t1_2_14 = BashOperator(
        task_id='t1_2_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_13
    t1_2_13 >> t1_2_14
    

  
    t1_2_15 = BashOperator(
        task_id='t1_2_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_14
    t1_2_14 >> t1_2_15
    

  
    t1_2_16 = BashOperator(
        task_id='t1_2_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_15
    t1_2_15 >> t1_2_16
    

  
    t1_2_17 = BashOperator(
        task_id='t1_2_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_16
    t1_2_16 >> t1_2_17
    

  
    t1_2_18 = BashOperator(
        task_id='t1_2_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_17
    t1_2_17 >> t1_2_18
    

  
    t1_2_19 = BashOperator(
        task_id='t1_2_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_2,
    # else link to t1_2_18
    t1_2_18 >> t1_2_19
    

  
  
    t1_3 = BashOperator(
        task_id='t1_3_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t1 >> t1_3

  
    t1_3_1 = BashOperator(
        task_id='t1_3_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_0
    t1_3 >> t1_3_1
    

  
    t1_3_2 = BashOperator(
        task_id='t1_3_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_1
    t1_3_1 >> t1_3_2
    

  
    t1_3_3 = BashOperator(
        task_id='t1_3_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_2
    t1_3_2 >> t1_3_3
    

  
    t1_3_4 = BashOperator(
        task_id='t1_3_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_3
    t1_3_3 >> t1_3_4
    

  
    t1_3_5 = BashOperator(
        task_id='t1_3_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_4
    t1_3_4 >> t1_3_5
    

  
    t1_3_6 = BashOperator(
        task_id='t1_3_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_5
    t1_3_5 >> t1_3_6
    

  
    t1_3_7 = BashOperator(
        task_id='t1_3_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_6
    t1_3_6 >> t1_3_7
    

  
    t1_3_8 = BashOperator(
        task_id='t1_3_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_7
    t1_3_7 >> t1_3_8
    

  
    t1_3_9 = BashOperator(
        task_id='t1_3_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_8
    t1_3_8 >> t1_3_9
    

  
    t1_3_10 = BashOperator(
        task_id='t1_3_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_9
    t1_3_9 >> t1_3_10
    

  
    t1_3_11 = BashOperator(
        task_id='t1_3_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_10
    t1_3_10 >> t1_3_11
    

  
    t1_3_12 = BashOperator(
        task_id='t1_3_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_11
    t1_3_11 >> t1_3_12
    

  
    t1_3_13 = BashOperator(
        task_id='t1_3_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_12
    t1_3_12 >> t1_3_13
    

  
    t1_3_14 = BashOperator(
        task_id='t1_3_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_13
    t1_3_13 >> t1_3_14
    

  
    t1_3_15 = BashOperator(
        task_id='t1_3_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_14
    t1_3_14 >> t1_3_15
    

  
    t1_3_16 = BashOperator(
        task_id='t1_3_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_15
    t1_3_15 >> t1_3_16
    

  
    t1_3_17 = BashOperator(
        task_id='t1_3_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_16
    t1_3_16 >> t1_3_17
    

  
    t1_3_18 = BashOperator(
        task_id='t1_3_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_17
    t1_3_17 >> t1_3_18
    

  
    t1_3_19 = BashOperator(
        task_id='t1_3_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_3,
    # else link to t1_3_18
    t1_3_18 >> t1_3_19
    

  
  
    t1_4 = BashOperator(
        task_id='t1_4_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t1 >> t1_4

  
    t1_4_1 = BashOperator(
        task_id='t1_4_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_0
    t1_4 >> t1_4_1
    

  
    t1_4_2 = BashOperator(
        task_id='t1_4_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_1
    t1_4_1 >> t1_4_2
    

  
    t1_4_3 = BashOperator(
        task_id='t1_4_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_2
    t1_4_2 >> t1_4_3
    

  
    t1_4_4 = BashOperator(
        task_id='t1_4_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_3
    t1_4_3 >> t1_4_4
    

  
    t1_4_5 = BashOperator(
        task_id='t1_4_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_4
    t1_4_4 >> t1_4_5
    

  
    t1_4_6 = BashOperator(
        task_id='t1_4_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_5
    t1_4_5 >> t1_4_6
    

  
    t1_4_7 = BashOperator(
        task_id='t1_4_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_6
    t1_4_6 >> t1_4_7
    

  
    t1_4_8 = BashOperator(
        task_id='t1_4_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_7
    t1_4_7 >> t1_4_8
    

  
    t1_4_9 = BashOperator(
        task_id='t1_4_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_8
    t1_4_8 >> t1_4_9
    

  
    t1_4_10 = BashOperator(
        task_id='t1_4_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_9
    t1_4_9 >> t1_4_10
    

  
    t1_4_11 = BashOperator(
        task_id='t1_4_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_10
    t1_4_10 >> t1_4_11
    

  
    t1_4_12 = BashOperator(
        task_id='t1_4_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_11
    t1_4_11 >> t1_4_12
    

  
    t1_4_13 = BashOperator(
        task_id='t1_4_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_12
    t1_4_12 >> t1_4_13
    

  
    t1_4_14 = BashOperator(
        task_id='t1_4_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_13
    t1_4_13 >> t1_4_14
    

  
    t1_4_15 = BashOperator(
        task_id='t1_4_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_14
    t1_4_14 >> t1_4_15
    

  
    t1_4_16 = BashOperator(
        task_id='t1_4_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_15
    t1_4_15 >> t1_4_16
    

  
    t1_4_17 = BashOperator(
        task_id='t1_4_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_16
    t1_4_16 >> t1_4_17
    

  
    t1_4_18 = BashOperator(
        task_id='t1_4_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_17
    t1_4_17 >> t1_4_18
    

  
    t1_4_19 = BashOperator(
        task_id='t1_4_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t1_4,
    # else link to t1_4_18
    t1_4_18 >> t1_4_19
    

  
  



    t2 = BashOperator(
        task_id='t2_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t0 >> t2

  
    t2_1 = BashOperator(
        task_id='t2_1_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t2 >> t2_1

  
    t2_1_1 = BashOperator(
        task_id='t2_1_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_0
    t2_1 >> t2_1_1
    

  
    t2_1_2 = BashOperator(
        task_id='t2_1_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_1
    t2_1_1 >> t2_1_2
    

  
    t2_1_3 = BashOperator(
        task_id='t2_1_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_2
    t2_1_2 >> t2_1_3
    

  
    t2_1_4 = BashOperator(
        task_id='t2_1_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_3
    t2_1_3 >> t2_1_4
    

  
    t2_1_5 = BashOperator(
        task_id='t2_1_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_4
    t2_1_4 >> t2_1_5
    

  
    t2_1_6 = BashOperator(
        task_id='t2_1_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_5
    t2_1_5 >> t2_1_6
    

  
    t2_1_7 = BashOperator(
        task_id='t2_1_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_6
    t2_1_6 >> t2_1_7
    

  
    t2_1_8 = BashOperator(
        task_id='t2_1_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_7
    t2_1_7 >> t2_1_8
    

  
    t2_1_9 = BashOperator(
        task_id='t2_1_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_8
    t2_1_8 >> t2_1_9
    

  
    t2_1_10 = BashOperator(
        task_id='t2_1_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_9
    t2_1_9 >> t2_1_10
    

  
    t2_1_11 = BashOperator(
        task_id='t2_1_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_10
    t2_1_10 >> t2_1_11
    

  
    t2_1_12 = BashOperator(
        task_id='t2_1_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_11
    t2_1_11 >> t2_1_12
    

  
    t2_1_13 = BashOperator(
        task_id='t2_1_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_12
    t2_1_12 >> t2_1_13
    

  
    t2_1_14 = BashOperator(
        task_id='t2_1_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_13
    t2_1_13 >> t2_1_14
    

  
    t2_1_15 = BashOperator(
        task_id='t2_1_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_14
    t2_1_14 >> t2_1_15
    

  
    t2_1_16 = BashOperator(
        task_id='t2_1_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_15
    t2_1_15 >> t2_1_16
    

  
    t2_1_17 = BashOperator(
        task_id='t2_1_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_16
    t2_1_16 >> t2_1_17
    

  
    t2_1_18 = BashOperator(
        task_id='t2_1_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_17
    t2_1_17 >> t2_1_18
    

  
    t2_1_19 = BashOperator(
        task_id='t2_1_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_1,
    # else link to t2_1_18
    t2_1_18 >> t2_1_19
    

  
  
    t2_2 = BashOperator(
        task_id='t2_2_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t2 >> t2_2

  
    t2_2_1 = BashOperator(
        task_id='t2_2_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_0
    t2_2 >> t2_2_1
    

  
    t2_2_2 = BashOperator(
        task_id='t2_2_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_1
    t2_2_1 >> t2_2_2
    

  
    t2_2_3 = BashOperator(
        task_id='t2_2_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_2
    t2_2_2 >> t2_2_3
    

  
    t2_2_4 = BashOperator(
        task_id='t2_2_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_3
    t2_2_3 >> t2_2_4
    

  
    t2_2_5 = BashOperator(
        task_id='t2_2_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_4
    t2_2_4 >> t2_2_5
    

  
    t2_2_6 = BashOperator(
        task_id='t2_2_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_5
    t2_2_5 >> t2_2_6
    

  
    t2_2_7 = BashOperator(
        task_id='t2_2_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_6
    t2_2_6 >> t2_2_7
    

  
    t2_2_8 = BashOperator(
        task_id='t2_2_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_7
    t2_2_7 >> t2_2_8
    

  
    t2_2_9 = BashOperator(
        task_id='t2_2_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_8
    t2_2_8 >> t2_2_9
    

  
    t2_2_10 = BashOperator(
        task_id='t2_2_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_9
    t2_2_9 >> t2_2_10
    

  
    t2_2_11 = BashOperator(
        task_id='t2_2_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_10
    t2_2_10 >> t2_2_11
    

  
    t2_2_12 = BashOperator(
        task_id='t2_2_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_11
    t2_2_11 >> t2_2_12
    

  
    t2_2_13 = BashOperator(
        task_id='t2_2_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_12
    t2_2_12 >> t2_2_13
    

  
    t2_2_14 = BashOperator(
        task_id='t2_2_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_13
    t2_2_13 >> t2_2_14
    

  
    t2_2_15 = BashOperator(
        task_id='t2_2_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_14
    t2_2_14 >> t2_2_15
    

  
    t2_2_16 = BashOperator(
        task_id='t2_2_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_15
    t2_2_15 >> t2_2_16
    

  
    t2_2_17 = BashOperator(
        task_id='t2_2_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_16
    t2_2_16 >> t2_2_17
    

  
    t2_2_18 = BashOperator(
        task_id='t2_2_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_17
    t2_2_17 >> t2_2_18
    

  
    t2_2_19 = BashOperator(
        task_id='t2_2_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_2,
    # else link to t2_2_18
    t2_2_18 >> t2_2_19
    

  
  
    t2_3 = BashOperator(
        task_id='t2_3_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t2 >> t2_3

  
    t2_3_1 = BashOperator(
        task_id='t2_3_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_0
    t2_3 >> t2_3_1
    

  
    t2_3_2 = BashOperator(
        task_id='t2_3_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_1
    t2_3_1 >> t2_3_2
    

  
    t2_3_3 = BashOperator(
        task_id='t2_3_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_2
    t2_3_2 >> t2_3_3
    

  
    t2_3_4 = BashOperator(
        task_id='t2_3_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_3
    t2_3_3 >> t2_3_4
    

  
    t2_3_5 = BashOperator(
        task_id='t2_3_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_4
    t2_3_4 >> t2_3_5
    

  
    t2_3_6 = BashOperator(
        task_id='t2_3_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_5
    t2_3_5 >> t2_3_6
    

  
    t2_3_7 = BashOperator(
        task_id='t2_3_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_6
    t2_3_6 >> t2_3_7
    

  
    t2_3_8 = BashOperator(
        task_id='t2_3_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_7
    t2_3_7 >> t2_3_8
    

  
    t2_3_9 = BashOperator(
        task_id='t2_3_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_8
    t2_3_8 >> t2_3_9
    

  
    t2_3_10 = BashOperator(
        task_id='t2_3_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_9
    t2_3_9 >> t2_3_10
    

  
    t2_3_11 = BashOperator(
        task_id='t2_3_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_10
    t2_3_10 >> t2_3_11
    

  
    t2_3_12 = BashOperator(
        task_id='t2_3_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_11
    t2_3_11 >> t2_3_12
    

  
    t2_3_13 = BashOperator(
        task_id='t2_3_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_12
    t2_3_12 >> t2_3_13
    

  
    t2_3_14 = BashOperator(
        task_id='t2_3_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_13
    t2_3_13 >> t2_3_14
    

  
    t2_3_15 = BashOperator(
        task_id='t2_3_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_14
    t2_3_14 >> t2_3_15
    

  
    t2_3_16 = BashOperator(
        task_id='t2_3_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_15
    t2_3_15 >> t2_3_16
    

  
    t2_3_17 = BashOperator(
        task_id='t2_3_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_16
    t2_3_16 >> t2_3_17
    

  
    t2_3_18 = BashOperator(
        task_id='t2_3_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_17
    t2_3_17 >> t2_3_18
    

  
    t2_3_19 = BashOperator(
        task_id='t2_3_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_3,
    # else link to t2_3_18
    t2_3_18 >> t2_3_19
    

  
  
    t2_4 = BashOperator(
        task_id='t2_4_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t2 >> t2_4

  
    t2_4_1 = BashOperator(
        task_id='t2_4_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_0
    t2_4 >> t2_4_1
    

  
    t2_4_2 = BashOperator(
        task_id='t2_4_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_1
    t2_4_1 >> t2_4_2
    

  
    t2_4_3 = BashOperator(
        task_id='t2_4_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_2
    t2_4_2 >> t2_4_3
    

  
    t2_4_4 = BashOperator(
        task_id='t2_4_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_3
    t2_4_3 >> t2_4_4
    

  
    t2_4_5 = BashOperator(
        task_id='t2_4_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_4
    t2_4_4 >> t2_4_5
    

  
    t2_4_6 = BashOperator(
        task_id='t2_4_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_5
    t2_4_5 >> t2_4_6
    

  
    t2_4_7 = BashOperator(
        task_id='t2_4_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_6
    t2_4_6 >> t2_4_7
    

  
    t2_4_8 = BashOperator(
        task_id='t2_4_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_7
    t2_4_7 >> t2_4_8
    

  
    t2_4_9 = BashOperator(
        task_id='t2_4_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_8
    t2_4_8 >> t2_4_9
    

  
    t2_4_10 = BashOperator(
        task_id='t2_4_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_9
    t2_4_9 >> t2_4_10
    

  
    t2_4_11 = BashOperator(
        task_id='t2_4_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_10
    t2_4_10 >> t2_4_11
    

  
    t2_4_12 = BashOperator(
        task_id='t2_4_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_11
    t2_4_11 >> t2_4_12
    

  
    t2_4_13 = BashOperator(
        task_id='t2_4_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_12
    t2_4_12 >> t2_4_13
    

  
    t2_4_14 = BashOperator(
        task_id='t2_4_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_13
    t2_4_13 >> t2_4_14
    

  
    t2_4_15 = BashOperator(
        task_id='t2_4_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_14
    t2_4_14 >> t2_4_15
    

  
    t2_4_16 = BashOperator(
        task_id='t2_4_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_15
    t2_4_15 >> t2_4_16
    

  
    t2_4_17 = BashOperator(
        task_id='t2_4_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_16
    t2_4_16 >> t2_4_17
    

  
    t2_4_18 = BashOperator(
        task_id='t2_4_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_17
    t2_4_17 >> t2_4_18
    

  
    t2_4_19 = BashOperator(
        task_id='t2_4_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t2_4,
    # else link to t2_4_18
    t2_4_18 >> t2_4_19
    

  
  



    t3 = BashOperator(
        task_id='t3_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t0 >> t3

  
    t3_1 = BashOperator(
        task_id='t3_1_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t3 >> t3_1

  
    t3_1_1 = BashOperator(
        task_id='t3_1_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_0
    t3_1 >> t3_1_1
    

  
    t3_1_2 = BashOperator(
        task_id='t3_1_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_1
    t3_1_1 >> t3_1_2
    

  
    t3_1_3 = BashOperator(
        task_id='t3_1_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_2
    t3_1_2 >> t3_1_3
    

  
    t3_1_4 = BashOperator(
        task_id='t3_1_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_3
    t3_1_3 >> t3_1_4
    

  
    t3_1_5 = BashOperator(
        task_id='t3_1_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_4
    t3_1_4 >> t3_1_5
    

  
    t3_1_6 = BashOperator(
        task_id='t3_1_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_5
    t3_1_5 >> t3_1_6
    

  
    t3_1_7 = BashOperator(
        task_id='t3_1_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_6
    t3_1_6 >> t3_1_7
    

  
    t3_1_8 = BashOperator(
        task_id='t3_1_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_7
    t3_1_7 >> t3_1_8
    

  
    t3_1_9 = BashOperator(
        task_id='t3_1_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_8
    t3_1_8 >> t3_1_9
    

  
    t3_1_10 = BashOperator(
        task_id='t3_1_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_9
    t3_1_9 >> t3_1_10
    

  
    t3_1_11 = BashOperator(
        task_id='t3_1_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_10
    t3_1_10 >> t3_1_11
    

  
    t3_1_12 = BashOperator(
        task_id='t3_1_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_11
    t3_1_11 >> t3_1_12
    

  
    t3_1_13 = BashOperator(
        task_id='t3_1_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_12
    t3_1_12 >> t3_1_13
    

  
    t3_1_14 = BashOperator(
        task_id='t3_1_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_13
    t3_1_13 >> t3_1_14
    

  
    t3_1_15 = BashOperator(
        task_id='t3_1_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_14
    t3_1_14 >> t3_1_15
    

  
    t3_1_16 = BashOperator(
        task_id='t3_1_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_15
    t3_1_15 >> t3_1_16
    

  
    t3_1_17 = BashOperator(
        task_id='t3_1_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_16
    t3_1_16 >> t3_1_17
    

  
    t3_1_18 = BashOperator(
        task_id='t3_1_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_17
    t3_1_17 >> t3_1_18
    

  
    t3_1_19 = BashOperator(
        task_id='t3_1_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_1,
    # else link to t3_1_18
    t3_1_18 >> t3_1_19
    

  
  
    t3_2 = BashOperator(
        task_id='t3_2_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t3 >> t3_2

  
    t3_2_1 = BashOperator(
        task_id='t3_2_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_0
    t3_2 >> t3_2_1
    

  
    t3_2_2 = BashOperator(
        task_id='t3_2_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_1
    t3_2_1 >> t3_2_2
    

  
    t3_2_3 = BashOperator(
        task_id='t3_2_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_2
    t3_2_2 >> t3_2_3
    

  
    t3_2_4 = BashOperator(
        task_id='t3_2_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_3
    t3_2_3 >> t3_2_4
    

  
    t3_2_5 = BashOperator(
        task_id='t3_2_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_4
    t3_2_4 >> t3_2_5
    

  
    t3_2_6 = BashOperator(
        task_id='t3_2_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_5
    t3_2_5 >> t3_2_6
    

  
    t3_2_7 = BashOperator(
        task_id='t3_2_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_6
    t3_2_6 >> t3_2_7
    

  
    t3_2_8 = BashOperator(
        task_id='t3_2_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_7
    t3_2_7 >> t3_2_8
    

  
    t3_2_9 = BashOperator(
        task_id='t3_2_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_8
    t3_2_8 >> t3_2_9
    

  
    t3_2_10 = BashOperator(
        task_id='t3_2_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_9
    t3_2_9 >> t3_2_10
    

  
    t3_2_11 = BashOperator(
        task_id='t3_2_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_10
    t3_2_10 >> t3_2_11
    

  
    t3_2_12 = BashOperator(
        task_id='t3_2_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_11
    t3_2_11 >> t3_2_12
    

  
    t3_2_13 = BashOperator(
        task_id='t3_2_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_12
    t3_2_12 >> t3_2_13
    

  
    t3_2_14 = BashOperator(
        task_id='t3_2_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_13
    t3_2_13 >> t3_2_14
    

  
    t3_2_15 = BashOperator(
        task_id='t3_2_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_14
    t3_2_14 >> t3_2_15
    

  
    t3_2_16 = BashOperator(
        task_id='t3_2_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_15
    t3_2_15 >> t3_2_16
    

  
    t3_2_17 = BashOperator(
        task_id='t3_2_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_16
    t3_2_16 >> t3_2_17
    

  
    t3_2_18 = BashOperator(
        task_id='t3_2_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_17
    t3_2_17 >> t3_2_18
    

  
    t3_2_19 = BashOperator(
        task_id='t3_2_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_2,
    # else link to t3_2_18
    t3_2_18 >> t3_2_19
    

  
  
    t3_3 = BashOperator(
        task_id='t3_3_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t3 >> t3_3

  
    t3_3_1 = BashOperator(
        task_id='t3_3_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_0
    t3_3 >> t3_3_1
    

  
    t3_3_2 = BashOperator(
        task_id='t3_3_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_1
    t3_3_1 >> t3_3_2
    

  
    t3_3_3 = BashOperator(
        task_id='t3_3_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_2
    t3_3_2 >> t3_3_3
    

  
    t3_3_4 = BashOperator(
        task_id='t3_3_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_3
    t3_3_3 >> t3_3_4
    

  
    t3_3_5 = BashOperator(
        task_id='t3_3_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_4
    t3_3_4 >> t3_3_5
    

  
    t3_3_6 = BashOperator(
        task_id='t3_3_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_5
    t3_3_5 >> t3_3_6
    

  
    t3_3_7 = BashOperator(
        task_id='t3_3_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_6
    t3_3_6 >> t3_3_7
    

  
    t3_3_8 = BashOperator(
        task_id='t3_3_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_7
    t3_3_7 >> t3_3_8
    

  
    t3_3_9 = BashOperator(
        task_id='t3_3_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_8
    t3_3_8 >> t3_3_9
    

  
    t3_3_10 = BashOperator(
        task_id='t3_3_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_9
    t3_3_9 >> t3_3_10
    

  
    t3_3_11 = BashOperator(
        task_id='t3_3_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_10
    t3_3_10 >> t3_3_11
    

  
    t3_3_12 = BashOperator(
        task_id='t3_3_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_11
    t3_3_11 >> t3_3_12
    

  
    t3_3_13 = BashOperator(
        task_id='t3_3_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_12
    t3_3_12 >> t3_3_13
    

  
    t3_3_14 = BashOperator(
        task_id='t3_3_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_13
    t3_3_13 >> t3_3_14
    

  
    t3_3_15 = BashOperator(
        task_id='t3_3_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_14
    t3_3_14 >> t3_3_15
    

  
    t3_3_16 = BashOperator(
        task_id='t3_3_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_15
    t3_3_15 >> t3_3_16
    

  
    t3_3_17 = BashOperator(
        task_id='t3_3_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_16
    t3_3_16 >> t3_3_17
    

  
    t3_3_18 = BashOperator(
        task_id='t3_3_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_17
    t3_3_17 >> t3_3_18
    

  
    t3_3_19 = BashOperator(
        task_id='t3_3_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_3,
    # else link to t3_3_18
    t3_3_18 >> t3_3_19
    

  
  
    t3_4 = BashOperator(
        task_id='t3_4_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t3 >> t3_4

  
    t3_4_1 = BashOperator(
        task_id='t3_4_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_0
    t3_4 >> t3_4_1
    

  
    t3_4_2 = BashOperator(
        task_id='t3_4_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_1
    t3_4_1 >> t3_4_2
    

  
    t3_4_3 = BashOperator(
        task_id='t3_4_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_2
    t3_4_2 >> t3_4_3
    

  
    t3_4_4 = BashOperator(
        task_id='t3_4_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_3
    t3_4_3 >> t3_4_4
    

  
    t3_4_5 = BashOperator(
        task_id='t3_4_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_4
    t3_4_4 >> t3_4_5
    

  
    t3_4_6 = BashOperator(
        task_id='t3_4_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_5
    t3_4_5 >> t3_4_6
    

  
    t3_4_7 = BashOperator(
        task_id='t3_4_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_6
    t3_4_6 >> t3_4_7
    

  
    t3_4_8 = BashOperator(
        task_id='t3_4_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_7
    t3_4_7 >> t3_4_8
    

  
    t3_4_9 = BashOperator(
        task_id='t3_4_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_8
    t3_4_8 >> t3_4_9
    

  
    t3_4_10 = BashOperator(
        task_id='t3_4_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_9
    t3_4_9 >> t3_4_10
    

  
    t3_4_11 = BashOperator(
        task_id='t3_4_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_10
    t3_4_10 >> t3_4_11
    

  
    t3_4_12 = BashOperator(
        task_id='t3_4_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_11
    t3_4_11 >> t3_4_12
    

  
    t3_4_13 = BashOperator(
        task_id='t3_4_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_12
    t3_4_12 >> t3_4_13
    

  
    t3_4_14 = BashOperator(
        task_id='t3_4_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_13
    t3_4_13 >> t3_4_14
    

  
    t3_4_15 = BashOperator(
        task_id='t3_4_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_14
    t3_4_14 >> t3_4_15
    

  
    t3_4_16 = BashOperator(
        task_id='t3_4_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_15
    t3_4_15 >> t3_4_16
    

  
    t3_4_17 = BashOperator(
        task_id='t3_4_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_16
    t3_4_16 >> t3_4_17
    

  
    t3_4_18 = BashOperator(
        task_id='t3_4_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_17
    t3_4_17 >> t3_4_18
    

  
    t3_4_19 = BashOperator(
        task_id='t3_4_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t3_4,
    # else link to t3_4_18
    t3_4_18 >> t3_4_19
    

  
  



    t4 = BashOperator(
        task_id='t4_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t0 >> t4

  
    t4_1 = BashOperator(
        task_id='t4_1_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t4 >> t4_1

  
    t4_1_1 = BashOperator(
        task_id='t4_1_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_0
    t4_1 >> t4_1_1
    

  
    t4_1_2 = BashOperator(
        task_id='t4_1_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_1
    t4_1_1 >> t4_1_2
    

  
    t4_1_3 = BashOperator(
        task_id='t4_1_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_2
    t4_1_2 >> t4_1_3
    

  
    t4_1_4 = BashOperator(
        task_id='t4_1_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_3
    t4_1_3 >> t4_1_4
    

  
    t4_1_5 = BashOperator(
        task_id='t4_1_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_4
    t4_1_4 >> t4_1_5
    

  
    t4_1_6 = BashOperator(
        task_id='t4_1_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_5
    t4_1_5 >> t4_1_6
    

  
    t4_1_7 = BashOperator(
        task_id='t4_1_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_6
    t4_1_6 >> t4_1_7
    

  
    t4_1_8 = BashOperator(
        task_id='t4_1_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_7
    t4_1_7 >> t4_1_8
    

  
    t4_1_9 = BashOperator(
        task_id='t4_1_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_8
    t4_1_8 >> t4_1_9
    

  
    t4_1_10 = BashOperator(
        task_id='t4_1_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_9
    t4_1_9 >> t4_1_10
    

  
    t4_1_11 = BashOperator(
        task_id='t4_1_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_10
    t4_1_10 >> t4_1_11
    

  
    t4_1_12 = BashOperator(
        task_id='t4_1_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_11
    t4_1_11 >> t4_1_12
    

  
    t4_1_13 = BashOperator(
        task_id='t4_1_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_12
    t4_1_12 >> t4_1_13
    

  
    t4_1_14 = BashOperator(
        task_id='t4_1_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_13
    t4_1_13 >> t4_1_14
    

  
    t4_1_15 = BashOperator(
        task_id='t4_1_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_14
    t4_1_14 >> t4_1_15
    

  
    t4_1_16 = BashOperator(
        task_id='t4_1_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_15
    t4_1_15 >> t4_1_16
    

  
    t4_1_17 = BashOperator(
        task_id='t4_1_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_16
    t4_1_16 >> t4_1_17
    

  
    t4_1_18 = BashOperator(
        task_id='t4_1_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_17
    t4_1_17 >> t4_1_18
    

  
    t4_1_19 = BashOperator(
        task_id='t4_1_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_1,
    # else link to t4_1_18
    t4_1_18 >> t4_1_19
    

  
  
    t4_2 = BashOperator(
        task_id='t4_2_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t4 >> t4_2

  
    t4_2_1 = BashOperator(
        task_id='t4_2_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_0
    t4_2 >> t4_2_1
    

  
    t4_2_2 = BashOperator(
        task_id='t4_2_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_1
    t4_2_1 >> t4_2_2
    

  
    t4_2_3 = BashOperator(
        task_id='t4_2_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_2
    t4_2_2 >> t4_2_3
    

  
    t4_2_4 = BashOperator(
        task_id='t4_2_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_3
    t4_2_3 >> t4_2_4
    

  
    t4_2_5 = BashOperator(
        task_id='t4_2_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_4
    t4_2_4 >> t4_2_5
    

  
    t4_2_6 = BashOperator(
        task_id='t4_2_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_5
    t4_2_5 >> t4_2_6
    

  
    t4_2_7 = BashOperator(
        task_id='t4_2_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_6
    t4_2_6 >> t4_2_7
    

  
    t4_2_8 = BashOperator(
        task_id='t4_2_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_7
    t4_2_7 >> t4_2_8
    

  
    t4_2_9 = BashOperator(
        task_id='t4_2_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_8
    t4_2_8 >> t4_2_9
    

  
    t4_2_10 = BashOperator(
        task_id='t4_2_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_9
    t4_2_9 >> t4_2_10
    

  
    t4_2_11 = BashOperator(
        task_id='t4_2_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_10
    t4_2_10 >> t4_2_11
    

  
    t4_2_12 = BashOperator(
        task_id='t4_2_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_11
    t4_2_11 >> t4_2_12
    

  
    t4_2_13 = BashOperator(
        task_id='t4_2_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_12
    t4_2_12 >> t4_2_13
    

  
    t4_2_14 = BashOperator(
        task_id='t4_2_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_13
    t4_2_13 >> t4_2_14
    

  
    t4_2_15 = BashOperator(
        task_id='t4_2_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_14
    t4_2_14 >> t4_2_15
    

  
    t4_2_16 = BashOperator(
        task_id='t4_2_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_15
    t4_2_15 >> t4_2_16
    

  
    t4_2_17 = BashOperator(
        task_id='t4_2_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_16
    t4_2_16 >> t4_2_17
    

  
    t4_2_18 = BashOperator(
        task_id='t4_2_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_17
    t4_2_17 >> t4_2_18
    

  
    t4_2_19 = BashOperator(
        task_id='t4_2_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_2,
    # else link to t4_2_18
    t4_2_18 >> t4_2_19
    

  
  
    t4_3 = BashOperator(
        task_id='t4_3_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t4 >> t4_3

  
    t4_3_1 = BashOperator(
        task_id='t4_3_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_0
    t4_3 >> t4_3_1
    

  
    t4_3_2 = BashOperator(
        task_id='t4_3_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_1
    t4_3_1 >> t4_3_2
    

  
    t4_3_3 = BashOperator(
        task_id='t4_3_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_2
    t4_3_2 >> t4_3_3
    

  
    t4_3_4 = BashOperator(
        task_id='t4_3_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_3
    t4_3_3 >> t4_3_4
    

  
    t4_3_5 = BashOperator(
        task_id='t4_3_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_4
    t4_3_4 >> t4_3_5
    

  
    t4_3_6 = BashOperator(
        task_id='t4_3_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_5
    t4_3_5 >> t4_3_6
    

  
    t4_3_7 = BashOperator(
        task_id='t4_3_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_6
    t4_3_6 >> t4_3_7
    

  
    t4_3_8 = BashOperator(
        task_id='t4_3_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_7
    t4_3_7 >> t4_3_8
    

  
    t4_3_9 = BashOperator(
        task_id='t4_3_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_8
    t4_3_8 >> t4_3_9
    

  
    t4_3_10 = BashOperator(
        task_id='t4_3_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_9
    t4_3_9 >> t4_3_10
    

  
    t4_3_11 = BashOperator(
        task_id='t4_3_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_10
    t4_3_10 >> t4_3_11
    

  
    t4_3_12 = BashOperator(
        task_id='t4_3_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_11
    t4_3_11 >> t4_3_12
    

  
    t4_3_13 = BashOperator(
        task_id='t4_3_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_12
    t4_3_12 >> t4_3_13
    

  
    t4_3_14 = BashOperator(
        task_id='t4_3_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_13
    t4_3_13 >> t4_3_14
    

  
    t4_3_15 = BashOperator(
        task_id='t4_3_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_14
    t4_3_14 >> t4_3_15
    

  
    t4_3_16 = BashOperator(
        task_id='t4_3_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_15
    t4_3_15 >> t4_3_16
    

  
    t4_3_17 = BashOperator(
        task_id='t4_3_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_16
    t4_3_16 >> t4_3_17
    

  
    t4_3_18 = BashOperator(
        task_id='t4_3_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_17
    t4_3_17 >> t4_3_18
    

  
    t4_3_19 = BashOperator(
        task_id='t4_3_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_3,
    # else link to t4_3_18
    t4_3_18 >> t4_3_19
    

  
  
    t4_4 = BashOperator(
        task_id='t4_4_sleep',
        depends_on_past=False,
        bash_command='date',
    )
    t4 >> t4_4

  
    t4_4_1 = BashOperator(
        task_id='t4_4_1_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_0
    t4_4 >> t4_4_1
    

  
    t4_4_2 = BashOperator(
        task_id='t4_4_2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_1
    t4_4_1 >> t4_4_2
    

  
    t4_4_3 = BashOperator(
        task_id='t4_4_3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_2
    t4_4_2 >> t4_4_3
    

  
    t4_4_4 = BashOperator(
        task_id='t4_4_4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_3
    t4_4_3 >> t4_4_4
    

  
    t4_4_5 = BashOperator(
        task_id='t4_4_5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_4
    t4_4_4 >> t4_4_5
    

  
    t4_4_6 = BashOperator(
        task_id='t4_4_6_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_5
    t4_4_5 >> t4_4_6
    

  
    t4_4_7 = BashOperator(
        task_id='t4_4_7_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_6
    t4_4_6 >> t4_4_7
    

  
    t4_4_8 = BashOperator(
        task_id='t4_4_8_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_7
    t4_4_7 >> t4_4_8
    

  
    t4_4_9 = BashOperator(
        task_id='t4_4_9_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_8
    t4_4_8 >> t4_4_9
    

  
    t4_4_10 = BashOperator(
        task_id='t4_4_10_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_9
    t4_4_9 >> t4_4_10
    

  
    t4_4_11 = BashOperator(
        task_id='t4_4_11_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_10
    t4_4_10 >> t4_4_11
    

  
    t4_4_12 = BashOperator(
        task_id='t4_4_12_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_11
    t4_4_11 >> t4_4_12
    

  
    t4_4_13 = BashOperator(
        task_id='t4_4_13_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_12
    t4_4_12 >> t4_4_13
    

  
    t4_4_14 = BashOperator(
        task_id='t4_4_14_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_13
    t4_4_13 >> t4_4_14
    

  
    t4_4_15 = BashOperator(
        task_id='t4_4_15_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_14
    t4_4_14 >> t4_4_15
    

  
    t4_4_16 = BashOperator(
        task_id='t4_4_16_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_15
    t4_4_15 >> t4_4_16
    

  
    t4_4_17 = BashOperator(
        task_id='t4_4_17_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_16
    t4_4_16 >> t4_4_17
    

  
    t4_4_18 = BashOperator(
        task_id='t4_4_18_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_17
    t4_4_17 >> t4_4_18
    

  
    t4_4_19 = BashOperator(
        task_id='t4_4_19_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 3 )  + 1 ]s;date',
    )

    # if p==1, link to t4_4,
    # else link to t4_4_18
    t4_4_18 >> t4_4_19
    

  
  




