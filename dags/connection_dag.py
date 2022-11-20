from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

def say_hello():
    return 'hello world'

hello_dag = DAG(dag_id = 'hello_dag', 
                          start_date = datetime.now() - timedelta(days = 1))


get_states = PythonOperator(task_id='say_hello', 
                            dag = hello_dag,
                            python_callable = say_hello)