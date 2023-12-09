
<h3 align="center">Wine Quality Prediction ML Model</h3>

  <p align="center">
    Wine Quality Prediction with Spark on AWS and Docker.
    <br />
    <a href="https://github.com/NanaBoakye11/Wine-Quality-Prediction-ML-Model"><strong>View Code »</strong></a>
    <br />
    <br />
    <a href="https://github.com/NanaBoakye11/Wine-Quality-Prediction-ML-Model/issues">Report Any Issues Associated</a>
  </p>

## Project Overview
## GOAL

The purpose of this individual assignment is to develop parallel machine learning (ML) applications in Amazon AWS cloud platform. Specifically, you will learn: (1) how to use Apache Spark to train an ML model in parallel on multiple EC2 instances; (2) how to use Spark’s MLlib to develop and use an ML model in the cloud; (3) How to use Docker to create a container for your ML model to simplify model deployment.


## Description 

You have to build a wine quality prediction ML model in Spark over AWS. The model must be trained in parallel using 4 EC2 instances. Then, you need to save and load the model in a Spark application that will perform wine quality prediction; this application will run on one EC2 instance. The assignment was implemented in Python on Ubuntu Linux.


* Input for model training: 2 datasets with you for your ML model.
    * TrainingDataset.csv: you will use this dataset to train the model in parallel on multiple EC2 instances.
    * ValidationDataset.csv: you will use this dataset to validate the model and optimize its
performance (i.e., select the best values for the model parameters).
* Input for prediction testing: TestDataset.csv. We will use this file, which has a similar structure
with the two datasets above, to test the functionality and performance of your prediction
application. Your prediction application should take such a file as input. This file is not shared with
you, but you can use the validation dataset to make sure your application works.
* Output: The output of your application will be a measure of the prediction performance, specifically
the F1 score, which is available in MLlib.
* Model Implementation: You have to develop a Spark application that uses MLlib to train for wine
quality prediction using the training dataset. You will use the validation dataset check the
performance of your trained model and to potentially tune your ML model parameters for best
performance. You should start with a simple linear regression or logistic regression model from
MLlib, but you can try multiple ML models to see which one leads to better performance. For
classification models, you can use 10 classes (the wine scores are from 1 to 10). 
* Docker container: You have to build a Docker container for your prediction application. In this
way, the prediction model can be quickly deployed across many different environments.
* The model training is done in parallel on 4 EC2 instances.
* The prediction with or without Docker is done on a single EC2 instance.



## Running The Application 
## Prequisites

* Amazon AWS account with access to EC2 instances.
* Docker installed on local machine and EC2 instances.
* Python3, Java and Apache Spark installed on Ubuntu Linux.


Click this <a href="https://github.com/NanaBoakye11/Wine-Quality-Prediction-ML-Model/blob/main/HowToGuide.pdf">link </a> for more information.


## Connect

Nana Boakye - [@LinkedIn](https://www.linkedin.com/in/boakye-nana/)
