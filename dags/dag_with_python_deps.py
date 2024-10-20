from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'sourabh',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)  # Retry every two minutes if task execution fails
}

def get_numpy():
    import numpy as np
    print(f"get_numpy version {np.__version__}")

with DAG(
    dag_id="python_deps_v01",
    default_args=default_args,
    start_date=datetime(2024, 10, 10),
    schedule_interval='0 0 * * *',  # Daily at midnight
) as dag:
    task1 = PythonOperator(
        task_id='python_deps',
        python_callable=get_numpy,  # The function to be called
    )
  
    task1
