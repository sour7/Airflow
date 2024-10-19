from airflow import DAG
from datetime import datetime,  timedelta
from airflow.operators.python import PythonOperator

default_args ={
    'owner': 'sourabh',
    'start_date': datetime(2021, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

def greet (ti): # here ti means task instance since 'Xccoms' can only pull can only be called by typing 'ti'
    # name= ti.xcom_pull(task_ids='get_name')
    first_name= ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name= ti.xcom_pull(task_ids='get_name', key='last_name')
    age= ti.xcom_pull(task_ids= 'get_age',  key='age')
    print(f"Hello, World! I'm {first_name} {last_name} and I'm {age} years old")

def get_name(ti):
    # return "Jerry"   
    ti.xcom_push(key="first_name", value="John")
    ti.xcom_push(key="last_name", value="Doe") 

def get_age(ti):
    ti.xcom_push(key='age', value=19)


with DAG(
    description='A simple pythonoperator example',
    dag_id='example_python_operator_v06',
    default_args=default_args,
    start_date=datetime(2024, 10, 6),
    schedule_interval='@daily',  # Run every day
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,  # The function to be called
        op_kwargs={'age':11}
    ) 
    task2= PythonOperator(
        task_id ='get_name',
        python_callable=get_name

    )
    task3= PythonOperator(
        task_id= 'get_age',
        python_callable = get_age
    )

    [task2, task3] >> task1