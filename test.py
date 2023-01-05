from collections.abc import MutableMapping
from _collections_abc import Mapping
from _collections_abc import MutableMapping
from _collections_abc import Sequence
from pyspark.sql import SparkSession
spark = SparkSession.builder.config("spark.driver.host", "localhost").appName("Practice").master("local[3]").getOrCreate()
spark.sparkContext.setLogLevel('Error')

dept = [("Finance",10),("Marketing",20),("Sales",30),("IT",40)]
deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(data=dept, schema = deptColumns)
deptDF.printSchema()
deptDF.show(truncate=False)

dataCollect = deptDF.collect()

print(dataCollect)

dataCollect2 = deptDF.select("dept_name").collect()
print(dataCollect2)

for row in dataCollect:
    print(row['dept_name'] + "," +str(row['dept_id']))
