from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'sourabh',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)  # Retry every two minutes if task execution fails
}

with DAG(
    dag_id="our_dag_with_cron_expression_v03",  # unique dag id
    default_args=default_args,
    description="this is first dag with cron",
    start_date=datetime(2024, 10, 5),
    schedule_interval='0 2 * * Wed',
) as dag:
    task1 = BashOperator(
        task_id='this_is_1st_task',
        bash_command="echo this is my bash command from cron"
    )

    task1
