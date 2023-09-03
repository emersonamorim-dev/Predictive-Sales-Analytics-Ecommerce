from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("e-commerce-analytics").getOrCreate()

def process_data():
    data = spark.read.csv("/data/raw/sales_data.csv")
    # Transformações, limpeza, enriquecimento etc.
    data.write.parquet("/data/processed/sales_data.parquet")

if __name__ == "__main__":
    process_data()
