"""Start local Spark and check a small DataFrame operation."""
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.master('local[1]')
    .appName('flight-delay-ci-smoke')
    .config('spark.ui.enabled', 'false')
    .config('spark.sql.shuffle.partitions', '1')
    .config('spark.driver.host', '127.0.0.1')
    .getOrCreate()
)
try:
    rows = [(1, 0), (2, 1), (3, 1)]
    frame = spark.createDataFrame(rows, ['flight_id', 'delayed'])
    delayed_count = frame.filter(frame.delayed == 1).count()
    assert delayed_count == 2
    print('Local Spark DataFrame smoke check passed.')
finally:
    spark.stop()
