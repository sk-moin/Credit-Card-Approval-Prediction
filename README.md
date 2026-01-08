# Credit Card Approval Prediction


A Flask web app that predicts credit card approval status using a machine learning model trained on real demographic and credit history data.

The project includes a full ML workflow — data preprocessing, model training, serialization with pickle, and deployment readiness — and it’s built for real-world usage and deployment on platforms such as AWS Elastic Beanstalk.

## 🧠 Table of Contents

* 🔍 Overview

* 📁 Dataset

* 🛠 Features

* 🧪 Model Training

* ⚙️ Flask Web App

* 🧩 Deployment



## 🔍 Overview


This project trains a Random Forest classifier to predict whether a credit card application should be approved or declined based on demographic and financial data. The trained model is saved with preprocessing steps in a pipeline and used in a Flask web application for real-time user input.


## 📁 Dataset

The model uses two datasets:

application_record.csv — demographic profile of applicants

credit_record.csv — historical credit repayment behavior


## 🛠 Features Used

### Numerical features:

    AMT_INCOME_TOTAL
    
    CNT_CHILDREN
    
    CNT_FAM_MEMBERS
    
    AGE_YEARS
    
    YEARS_EMPLOYED


### Categorical features:

    CODE_GENDER
    
    FLAG_OWN_CAR
    
    FLAG_OWN_REALTY
    
    NAME_INCOME_TYPE
    
    NAME_EDUCATION_TYPE
    
    NAME_FAMILY_STATUS
    
    NAME_HOUSING_TYPE


## 🧪 Model Training

The model training was done in Jupyter Notebook using:

ColumnTransformer for preprocessing

StandardScaler for numeric features

OneHotEncoder for categorical features

RandomForestClassifier for classification

The pipeline was fitted on training data and then saved with pickle:

pickle.dump(final_pipeline, open("credit_card_approval_pipeline.pkl", "wb"))

This ensures preprocessing and prediction are bundled together.


## ⚙️ Flask Web Application

The application provides a user interface where users can enter:

Personal demographics (age, car ownership, realty)

Income details

Family and education information

It returns a prediction (APPROVED / DECLINED) based on the trained model.

<img width="490" height="802" alt="Screenshot 2026-01-08 194706" src="https://github.com/user-attachments/assets/b1250bc8-48a4-4c42-bd99-a0f2a0ee92cd" />


## 🚀 Deployment

This app can be deployed on AWS Elastic Beanstalk, Heroku, or similar platforms.


    <img width="905" height="400" alt="image" src="https://github.com/user-attachments/assets/8c54ea07-3feb-40a9-8d00-c67fd6eefc8c" />


## 🧩 How to Run Locally

    <img width="757" height="719" alt="Screenshot 2026-01-09 003327" src="https://github.com/user-attachments/assets/70e76258-c7b1-49d3-8b97-4b86b133acb8" />
