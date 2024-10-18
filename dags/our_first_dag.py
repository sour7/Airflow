from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'sourabh',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)  # Retry every two minutes if task execution fails
}

with DAG(
    dag_id="our_first_dag_v4",  # unique dag id
    default_args=default_args,
    description="this is first dag",
    start_date=datetime(2021, 7, 29, 2, 2),  # dag start time at 29/07/2021 at 2 AM
    schedule_interval='@daily'  # frequency of task execution
) as dag:
    task1 = BashOperator(
        task_id='this_is_1st_task',
        bash_command="echo Hello world, this is my first task"
    )
    task2 = BashOperator(
        task_id='this_is_2nd_task',
        bash_command="echo Hello world, this is my second task and will run after task one "
    )
    task3 =BashOperator(
        task_id='this_is_3rd_task',
        bash_command="echo Hello world, this is my third task and will run after task1 and at same time task2"
    )
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    #bit shift operator
    task1 >> [task2, task3] # type: ignore

 