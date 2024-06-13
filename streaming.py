from pyspark.sql import SparkSession

# Define AWS credentials
aws_access_key_id = "AKIA6OUZI3VF52W3O4"   #
aws_secret_access_key = "xuM77R4KMw++9RhT6+bXwJ94aOe4JvTcQRK2GyeX2J"

# Configure Spark session
spark = SparkSession.builder \
    .appName("Read JSON from S3") \
    .config("spark.hadoop.fs.s3a.access.key", aws_access_key_id) \
    .config("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key) \
    .getOrCreate()

# S3 path where JSON files are located
input_path = "s3a://my-json-input-bucket1/"

# Read JSON files into a DataFrame
df = spark.read.json(input_path)

# Show schema and sample data
df.printSchema()
df.show()

# Stop Spark session
spark.stop()
