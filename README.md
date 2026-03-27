# Spam Detector – AI & ML Project

**By:** Jadhav Gauri Bhausaheb


---

## Introduction
Spam messages are unwanted or unsolicited messages received via email, SMS, or online platforms. They waste time, reduce productivity, and may contain harmful links or malware. This project develops a **Spam Detection System** using **AI and ML techniques**, which automatically identifies messages as Spam or Not Spam. It uses text preprocessing, feature extraction, and the **Naive Bayes classification algorithm** to detect spam accurately, improving communication safety and saving time.

---

## Problem Statement
Users receive a large number of messages daily, and many are spam. Manually filtering these messages is inefficient and time-consuming. The Spam Detection System uses **AI and ML** to automatically detect and classify messages, reducing human effort, minimizing exposure to malicious content, and improving productivity.

---

## Relevance to AI and ML

### Artificial Intelligence (AI)
- **Intelligent Automation:** Automatically identifies and filters spam messages.  
- **Decision Making:** Determines whether a message is Spam or Not Spam based on its content.  
- **Pattern Recognition:** Learns common spam patterns or keywords to make predictions.

### Machine Learning (ML)
- **Supervised Learning:** Model is trained on labeled data (Spam or Not Spam).  
- **Classification Problem:** Messages are categorized as Spam or Not Spam.  
- **Feature Extraction:** Converts text into numerical vectors using **CountVectorizer**.  
- **Naive Bayes Algorithm:** **Multinomial Naive Bayes** classifies messages based on word frequency.  
- **Model Evaluation:** Accuracy, precision, recall, and F1-score measure performance.  

---

## Tools and Technologies
- **Python:** Programming language for AI/ML implementation.  
- **pandas:** Load, clean, and manipulate datasets.  
- **scikit-learn:** ML algorithms and model evaluation.  
  - CountVectorizer  
  - Multinomial Naive Bayes  
  - train_test_split  
- **NLTK:** Text preprocessing, removing stop words.    
- **Dataset:** SMS Spam Collection Dataset (labeled SMS messages as spam or ham).

---

## Approach 
1. Load and clean the dataset.  
2. Preprocess messages: lowercase, remove special characters, stop words.  
3. Convert messages to numerical vectors using **CountVectorizer**.  
4. Split data: 80% training, 20% testing.  
5. Train **Multinomial Naive Bayes** classifier.  
6. Test the model on unseen messages and evaluate performance.  

---
## Setting Up

### Step 1: Clone the GitHub Repository

* Copy the repository URL from GitHub and clone it:

```bash
git clone <your-repo-link>
cd <your-repo-folder>
```

### Step 2: Set Up Python Environment

* Ensure Python 3.8+ is installed.

### Step 3: Install Required Libraries

```bash
pip install pandas scikit-learn
```

### Step 4: Add the Dataset

* Ensure `spam.csv` is in the project folder.

### Step 5: Run the Command-Line Program

```bash
python SpamDetection.py
```

### Step 6: Use the Program

* Enter a message when prompted
* The program will display:

  * **Spam**
  * **Not Spam**
* Type `exit` to close the program




## Challenges Faced
- Cleaning dataset and removing duplicates.  
- Handling very short messages with insufficient information.  
- Converting the ML model into a real-time interactive application.  
- Choosing appropriate preprocessing and feature extraction steps for better accuracy.

---

## Results
- Accuracy: **98.64%** on test dataset.  
- Successfully classified both test data
- Confusion matrix confirmed correct classification of spam and non-spam messages.  
- Real-time interface allows easy message validation.

---

## Conclusion
The Spam Detection System efficiently classifies messages as Spam or Not Spam, saving time and reducing exposure to harmful content. It demonstrates practical use of **AI and ML** concepts, including supervised learning, classification, and Naive Bayes. This system can be extended to detect spam emails, social media messages, or phishing attacks.

