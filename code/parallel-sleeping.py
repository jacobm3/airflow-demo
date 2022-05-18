
from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
with DAG(
    'parallel_sleeping_dag_v04',
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
    schedule_interval=timedelta(hours=6),
    start_date=datetime(2022, 5, 10),
    catchup=True,
    max_active_runs=10,
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
        bash_command='date; sleep $[ ( $RANDOM % 5 )  + 1 ]s;date',
    )

    t3 = BashOperator(
        task_id='t3_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 5 )  + 1 ]s;date',
    )

    t4 = BashOperator(
        task_id='t4_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 5 )  + 1 ]s;date',
    )

    t5 = BashOperator(
        task_id='t5_sleep',
        depends_on_past=False,
        bash_command='date; sleep $[ ( $RANDOM % 5 )  + 1 ]s;date',
    )

    t1 >> [t2, t3, t4, t5]


