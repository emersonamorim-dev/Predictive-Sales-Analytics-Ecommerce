# Predictive Sales Analytics for E-commerce 🛍️📈

Codificação em Python para uma solução de Análise Preditiva para Vendas de E-commerce. Ele utiliza Apache Airflow para orquestração, Apache Spark para processamento de dados e uma aplicação web para visualização.

### Docker 🐳

Docker é utilizado para containerizar cada componente da solução, garantindo isolamento, reprodutibilidade e escalabilidade. Cada serviço, seja ele Airflow, Spark ou a aplicação web, é encapsulado em um container Docker, facilitando o deployment, scaling e a manutenção.

### Kubernetes ☸️

Kubernetes é usado para orquestrar os containers Docker em um ambiente de produção. Ele gerencia o ciclo de vida dos containers, auto-healing, auto-scaling e distribuição de carga. Com o Spark no Kubernetes, é possível escalar dinamicamente os workers de acordo com a demanda.

### PostgreSQL 🐘

PostgreSQL é o banco de dados escolhido para armazenar metadados do Airflow e, potencialmente, dados de vendas para análise. É um sistema de gerenciamento de banco de dados relacional robusto, extensível e SQL-compliant.


## Pré-requisitos 📋

- Docker e Docker Compose
- Apache Airflow
- Apache Spark
- Python 3.x

## Instalação 🚀

1. **Clone o repositório**:
   ```b
   git clone https://github.com/your-github-username/Predictive-Sales-Analytics-Ecommerce.git
   cd Predictive-Sales-Analytics-Ecommerce
   ```

2. **Construa as imagens Docker**:
   ```
   docker-compose build
   ```

3. **Instale as dependências Python** (se estiver executando localmente sem Docker):
   ```
   pip install -r requirements.txt
   ```

## Executando a Aplicação 🖥️

1. **Inicie os serviços com Docker Compose**:
   ```
   docker-compose up
   ```

2. Acesse a aplicação web em \`http://localhost:8050\` e o Airflow em \`http://localhost:8081\`.

## Inicie a aplicação de forma local com os seguintes comandos:

 - Instalar o Apache Airflow
```
pip install apache-airflow
```

## Inicializar o banco de dados do Airflow
``` 
airflow db init
```

## Criar um usuário admin para acessar a interface web do Airflow
```
airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname Admin \
    --role Admin \
    --email admin@example.com
```
    
## Iniciar o webserver do Airflow
```
airflow webserver -p 8080
```

## Em um novo terminal, iniciar o scheduler do Airflow
airflow scheduler

## Instalar Apache Spark
```
pip install pyspark
```


4. PostgreSQL
- Para instalar o PostgreSQL localmente:

```
sudo apt-get update
```
```
sudo apt-get install postgresql postgresql-contrib
```

- Após a instalação, você pode iniciar o serviço PostgreSQL:
```
sudo service postgresql start
```

- Crie um banco de dados chamado sales_data:
```
sudo -u postgres createdb sales_data
```

## Para executar a aplicação web:
Instale as dependências necessárias (assumindo que você tenha um requirements.txt):
```
pip install -r requirements.txt
```

## Execute a aplicação:
```
python main.py
```


## Tecnologias Utilizadas 🛠️

- ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) - Linguagem de programação principal.
- ![Spark](https://img.shields.io/badge/-Spark-E25A1C?style=flat-square&logo=apache-spark&logoColor=white) - Para processamento de dados.
- ![Airflow](https://img.shields.io/badge/-Airflow-017CEE?style=flat-square&logo=apache-airflow&logoColor=white) - Para orquestração de tarefas.
- ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white) - Para containerização.


###Sequence Diagram
                    
```seq
Emerson->Brazil: Says Hello 
Note right of Brazil: Brazil thinks\nabout it 
Brazil-->Emerson: How are you? 
Emerson->>Emerson: I am good thanks!
```

echo "README.md Autor:"

Emerson Amorim
