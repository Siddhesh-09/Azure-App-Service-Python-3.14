# 🚀 Azure App Service Deployment with Python (Day 8)

## 📌 Overview
This project demonstrates how to build and deploy a **Python 3.14 web application** on Microsoft Azure using **Azure App Service**, with source code hosted on GitHub.

The application serves a static HTML page (`index.html`) from the root directory and is deployed directly from GitHub using Azure’s built-in deployment integration.

---

## 🛠️ What I Did

- Created an Azure App Service instance  
- Selected **Python 3.14 runtime**  
- Built a Python application serving an HTML file  
- Pushed the code to GitHub  
- Connected GitHub repository to Azure App Service  
- Successfully deployed and ran the application 🎉  

---

## ⚙️ Tech Stack

- Python 3.14  
- Azure App Service  
- GitHub  
- HTML  

---

## 🔗 Deployment Flow


Local Development → GitHub → Azure App Service → Live Web App


---

## 📂 Project Structure


.
├── app.py
├── index.html
├── requirements.txt
└── README.md


---

## 🚀 Application Code

### app.py

```python
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    app.run()
index.html
<!DOCTYPE html>
<html>
<head>
    <title>Azure App Service</title>
</head>
<body>
    <h1>🚀 Hello from Azure App Service</h1>
    <p>Python + HTML deployed successfully!</p>
</body>
</html>
🚀 Steps to Deploy
1. Create Azure App Service

Go to Azure Portal

Search App Services → Create

Configure:

Runtime: Python 3.14

Pricing Tier: Free / Basic

2. Push Code to GitHub
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-link>
git push -u origin main
3. Connect GitHub to Azure

Go to App Service

Open Deployment Center

Select GitHub

Choose repository & branch

Authorize and deploy

🌐 Output

Python web app deployed successfully

HTML page served from root directory

🧠 Key Learnings

Deploying Python apps using Azure App Service

Serving static HTML without templates

GitHub integration with Azure

Understanding PaaS deployment

🔗 Future Improvements

Move HTML to templates for scalability

Add CSS & JS

Implement multiple routes

Add CI/CD pipeline

🙌 Author

Siddhesh Khanorkar
Cloud & DevOps Learner ☁️🚀
