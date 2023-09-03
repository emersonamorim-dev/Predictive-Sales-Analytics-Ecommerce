from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'you',
    'start_date': datetime(2023, 9, 2),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('ecommerce_dag', default_args=default_args, schedule_interval='@daily', catchup=False)

# Tarefa para preparar os dados
prepare_data_task = BashOperator(
    task_id='prepare_data',
    bash_command='echo "Preparing data..."',
    dag=dag
)

spark_submit_cmd = """
spark-submit --master k8s://https://<KUBERNETES_API_ADDRESS>:<PORT> \
  --deploy-mode cluster \
  --name e-commerce-analytics \
  --class com.yourcompany.YourMainClass \
  /path/to/your/spark/job.jar
"""

# Tarefa para executar o job Spark
spark_task = BashOperator(
    task_id='spark_job',
    bash_command=spark_submit_cmd,
    dag=dag
)

# Tarefa para notificar o fim da execução
notify_task = BashOperator(
    task_id='notify_completion',
    bash_command='echo "Job completed!"',
    dag=dag
)

# Definindo a ordem das tarefas
prepare_data_task >> spark_task >> notify_task
