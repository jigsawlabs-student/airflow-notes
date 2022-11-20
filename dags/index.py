from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

def select_states():
    rds_hook = PostgresHook('rds')
    vals = rds_hook.get_records("select * from states")
    return vals



# dag
#  task_1 , task_2
pull_data = DAG(dag_id = 'pull_data', 
                          start_date = datetime.now() - timedelta(days = 1))


hello_task = PythonOperator(task_id='select_states', 
                            dag = pull_data,
                            python_callable = select_states)

