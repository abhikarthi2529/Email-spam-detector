📧 Email Spam Detector
A simple machine learning web app built with Flask that classifies emails as spam or not spam.

I used a dataset from Kaggle, which contains two columns:

The first column includes email text

The second column indicates whether the email is spam (1) or not spam (0)

🧹 Data Preprocessing
Cleaned the email text by:

Lowercasing all letters

Removing punctuation and special characters

Converted the cleaned text into a TF-IDF matrix using TfidfVectorizer

🧠 Model
Used the TF-IDF matrix as input features

Used the spam/not spam labels as target values

Trained a Logistic Regression model to predict whether an email is spam or not
