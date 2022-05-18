
from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
with DAG(
    'parallel_sleeping_dag',
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
    description='Parallel sleepy DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='t2_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 10 )  + 1 ]s;date',
    )

    t3 = BashOperator(
        task_id='t3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 10 )  + 1 ]s;date',
    )

    t4 = BashOperator(
        task_id='t4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 10 )  + 1 ]s;date',
    )

    t5 = BashOperator(
        task_id='t5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 10 )  + 1 ]s;date',
    )

    t1 >> [t2, t3, t4, t5]


