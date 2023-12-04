# Start from a base image with Java
FROM openjdk:11-jdk

# Install Python 3 and Pip
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Apache Spark
ENV SPARK_VERSION=3.1.2
ENV HADOOP_VERSION=3.2
ENV SPARK_HOME=/usr/local/spark
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py \
    && python3 get-pip.py \
    && pip install pyspark 

# Add Spark to PATH

export SPARK_HOME=/home/ubuntu/spark-3.5.0-bin-hadoop3

ENV PATH=$PATH:$SPARK_HOME/bin

# Copy the current directory contents into the container at /usr/src/app
COPY . .

RUN pip install numpy

# Run wine_quality_prediction.py when the container launches
CMD ["python3", "wine_quality_prediction.py"]
