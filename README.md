
---

### **Groq Chat App 🧠💬**  

A lightweight AI-powered chatbot built with **Streamlit, LangChain, and Groq API**. This application enables real-time conversations using powerful LLMs like** Llama-3.3-70B-Versatile** and **Mixtral-8x7b-32768**, with **adjustable memory length for better contextual continuity**. Users can customize how many past interactions the chatbot remembers, improving conversational flow.

## **🚀 Features**  
✔️ **Real-Time AI Conversations** – Interact with state-of-the-art LLMs via the Groq API.  
✔️ **Conversational Memory** – Maintains chat history for contextual awareness.  
✔️ **Dynamic Model Selection** – Switch between multiple language models.  
✔️ **Customizable UI** – Optimized with colors, themes, and emojis.  
✔️ **Easy Setup** – Minimal dependencies, runs locally with a few commands.  

---

## **📌 Prerequisites**  

Ensure you have the following installed before proceeding:  
- **Python 3.7+**  
- **pip (Python Package Manager)**  
- **Groq API Key** (Sign up at [Groq Console](https://console.groq.com/keys) to get your API Key)  
- **Git** (Optional, but recommended)  

---

## **🔧 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/groq-chat-app.git
cd groq-chat-app
```
*(Replace `your-username` with your GitHub username if needed.)*  

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**  
Create a `.env` file in the root directory and add your Groq API key:  
```bash
GROQ_API_KEY="your_groq_api_key_here"
```
*(Replace `"your_groq_api_key_here"` with your actual API key.)*  

### **4️⃣ Run the Application**  
```bash
streamlit run app.py
```
This will launch the chatbot interface in your browser.  

---

## **🛠 Troubleshooting**  

🔹 **Issue: `ModuleNotFoundError: No module named 'streamlit'`**  
✔️ Run: `pip install streamlit` and retry.  

🔹 **Issue: API Key Error (`Invalid API Key`)**  
✔️ Ensure you have added the correct **GROQ_API_KEY** in the `.env` file.  

🔹 **Issue: App Not Launching**  
✔️ Check if **Python 3.7+** is installed by running `python --version`.  
✔️ Restart the terminal and try `streamlit run app.py` again.  

---

## **📸 Screenshots**  
![image](https://github.com/user-attachments/assets/086b1b35-35b0-4a68-8b81-06bf9bd8bf17)
![image](https://github.com/user-attachments/assets/f9ae3171-f96b-4ba0-b21a-18803592483d)
![image](https://github.com/user-attachments/assets/119a8dbe-70ca-430f-b8c4-93c08fc96b32)



---

## **📌 Next Steps & Future Enhancements**  
🔹 **Deploy on Cloud** (Vercel, AWS, or Streamlit Cloud)  
🔹 **Add More AI Models** for broader LLM choices  
🔹 **Improve UI with Theming & Customization**  

---

## **📜 License**  
This project is licensed under the **MIT License** – feel free to use and modify it!  

---

## **🌟 Connect & Contribute**  
If you find this project useful, feel free to **⭐ star** the repo and **contribute**! Pull requests are welcome.  

---
