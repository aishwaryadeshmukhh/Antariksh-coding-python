import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#importing data set frm file
data = pd.read_csv('sales.csv')

#preparing the features for charting here
X = data[['followers', 'engagement']]
y = data['sales']
#data set is in binary otherwise would have to convert to binarty

#split data into training and testing models with 20% used for testing and 80% used for training
X__train, X__test, y__train, y__test = train_test_split(X, y, test_size=0.3, random_state=19)
#random_state signifies proper division of training and testing models any integer will work

#creating a logistic regression model
model = LogisticRegression()

#training the model
model.fit(X__train, y__train)

#predicting
y__pred = model.predict(X__test)

#finding accuracy
accuracy = accuracy_score(y__test, y__pred)
print("accuracy:", accuracy)
