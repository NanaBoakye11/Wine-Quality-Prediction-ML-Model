from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import VectorAssembler

# Initialize Spark session
spark = SparkSession.builder.appName("Wine Quality Prediction").getOrCreate()

def clean_column_names(df):
    return df.toDF(*(c.replace(' ', '').replace('"', '') for c in df.columns))

# Load training data
training_data = spark.read.csv("TrainingDataset.csv", header=True, inferSchema=True)
training_data = clean_column_names(training_data)

# VectorAssembler to combine feature columns
feature_cols = training_data.columns[:-1]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
training_data = assembler.transform(training_data).select("features", """quality""")

# Define Logistic Regression model
lr = LogisticRegression(featuresCol='features', labelCol='quality')

# Train the model
lr_model = lr.fit(training_data)

# Load validation data
validation_data = spark.read.csv("ValidationDataset.csv", header=True, inferSchema=True)
validation_data = clean_column_names(validation_data)
validation_data = assembler.transform(validation_data).select("features", """quality""")

# Make predictions
predictions = lr_model.transform(validation_data)

# Evaluate the model
evaluator = MulticlassClassificationEvaluator(labelCol='quality', predictionCol='prediction', metricName='f1')
f1_score = evaluator.evaluate(predictions)
print(f"F1 Score: {f1_score}")

# Save the model
lr_model.save("/home/ubuntu/winePrediction/testData")

# Stop the Spark session
spark.stop()
