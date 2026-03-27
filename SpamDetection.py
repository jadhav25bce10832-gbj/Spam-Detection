import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv(r"C:\Users\tanan\Downloads\shikha.aiml\spam.csv")

data.drop_duplicates(inplace=True)
data['Category']=data['Category'].replace(['ham','spam'],['Not Spam','Spam'])

mess=data['Message']
cat=data['Category']

(mess_train,mess_test,cat_train,cat_test)= train_test_split(mess, cat , test_size=0.2)

cv=CountVectorizer(stop_words='english')
features=cv.fit_transform(mess_train)

#Creating Model

model=MultinomialNB()
model.fit(features,cat_train)

#Testing my model
features_test=cv.transform(mess_test)
accuracy = model.score(features_test, cat_test)

print(f"\nModel Accuracy: {accuracy*100:.2f}%")

#Predict Data
def predict(message):
    input_message = cv.transform([message]).toarray()
    return model.predict(input_message)[0]


# CLI loop
while True:
    user_input = input("\nEnter a message to be checked(or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    
    if user_input.strip() == "":
        print("Please enter a valid message.")
        continue
    
    result = predict(user_input)
    print(f"Prediction: {result}")
