from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'sourabh',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)  # Retry every two minutes if task execution fails
}

with DAG(
    dag_id="dag_with_postgres_v555",
    default_args=default_args,
    start_date=datetime(2024, 10, 10),
    schedule_interval='0 0 * * *',  # Daily at midnight
) as dag:
    task1 = PostgresOperator(
        task_id='create_postgres_table',
        postgres_conn_id='postgres_localhost',  # Replace with actual connection ID
        sql="""
            CREATE TABLE IF NOT EXISTS dag_runs (
                dt DATE,
                dag_id CHARACTER VARYING,
                PRIMARY KEY (dt, dag_id)
            );
        """  # SQL query to create the table
    )
    task2 = PostgresOperator(
        task_id='insert_data_postgres_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            INSERT INTO dag_runs (dt, dag_id) 
            VALUES ('{{ ds }}', '{{ dag.dag_id }}') 
            ON CONFLICT (dt, dag_id) DO NOTHING;

        """  
    )
    task3 = PostgresOperator(
        task_id='delete_data_postgres_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            INSERT INTO dag_runs (dt, dag_id) VALUES ('{{ ds }}', '{{ dag.dag_id }}');
        """  
    )
    task1 >> task3 >> task2
