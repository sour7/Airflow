from airflow import DAG
from datetime import datetime,  timedelta
from airflow.operators.python import PythonOperator

default_args ={
    'owner': 'sourabh',
    'start_date': datetime(2021, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

def greet (name, age):
    print(f"Hello, World! I'm {name} and I'm {age} years old")
    

with DAG(
    description='A simple pythonoperator example',
    dag_id='example_python_operator_v2',
    default_args=default_args,
    start_date=datetime(2024, 10, 6),
    schedule_interval='@daily',  # Run every day
) as dag:
    task1 = PythonOperator(
        task_id='print_hello_world',
        python_callable=greet,  # The function to be called
        op_kwargs={ 'name':"Tom", 'age':11}
    )
    task1   