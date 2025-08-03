# 💰 AI Agent for Digital Financial Literacy (Problem Statement No.7)

An AI-powered multilingual assistant built using **IBM Cloud Lite**, **IBM Watson Discovery**, and **IBM Granite** (Watsonx), designed to educate users on digital financial tools like **UPI**, **interest rates**, **personal finance**, **digital scams**, and more.

---

## ✅ Features

* 🔍 **RAG (Retrieval-Augmented Generation)** using Watson Discovery
* 💬 **Granite LLM (IBM Watsonx)** for accurate and contextual responses
* 🌐 **Multilingual Support** using Google Translate
* 🔐 Built with **Flask API** and `.env` secure credentials
* 🔄 Answers questions like:

  * “How do I send money using UPI?”
  * “What is a safe interest rate?”
  * “How to identify a fake banking app?”

---

## 🏗️ Project Structure

```
ai-digital-financial-agent/
├── app.py                 # Flask backend for the AI chatbot
├── retriever.py           # Retrieves financial context using Watson Discovery
├── translator.py          # Language translation for multilingual support
├── prompt_template.txt    # Template for Granite LLM prompt
├── .env                   # Environment variables (keys & IDs)
├── requirements.txt       # All required dependencies
└── README.md              # You're here!
```

---

## 🛠️ Technologies Used

| Technology           | Role                          |
| -------------------- | ----------------------------- |
| IBM Watsonx Granite  | Large Language Model (LLM)    |
| IBM Watson Discovery | Knowledge retrieval (RAG)     |
| Flask                | API framework                 |
| Googletrans          | Translate user input/output   |
| Python dotenv        | Secure environment management |

---

## 🔑 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-digital-financial-agent.git
cd ai-digital-financial-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` file

```env
IBM_API_KEY=your_ibm_cloud_api_key
DISCOVERY_URL=https://api.us-south.discovery.watson.cloud.ibm.com
DISCOVERY_PROJECT_ID=your_discovery_project_id
```

### 4. Run the Flask app

```bash
python app.py
```

---

## 🔄 Sample Request (POST `/ask`)

```json
{
  "question": "यूपीआई से पैसे कैसे भेजें?",
  "language": "hi"
}
```

### Sample Response

```json
{
  "question": "यूपीआई से पैसे कैसे भेजें?",
  "answer": "आप UPI ऐप जैसे Google Pay, PhonePe या BHIM का उपयोग करके मोबाइल नंबर या UPI ID के माध्यम से पैसे भेज सकते हैं।",
  "language": "hi"
}
```

---

## ⚠️ Notes

* Ensure you have uploaded **valid financial documents** (like RBI FAQs, NPCI docs) to your **Watson Discovery project**.
* Granite LLM access requires an **IBM Cloud project with Watsonx enabled**.
* This app is intended for **educational and awareness** purposes only.

---

## 📚 Use Cases

* Digital Financial Literacy in rural areas
* Banking fraud awareness
* Student & youth financial onboarding
* Multilingual chatbot on financial apps

---

## 👥 Contributors

* **Kalyan Nagu** (Developer)
* IBM Cloud Lite APIs
* Open-source AI community

