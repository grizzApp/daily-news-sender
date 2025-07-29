Great, Captain! Here's a revised `README.md` in **English**, reflecting that your `tests/` folder is already excluded via `.gitignore`:

---

```markdown
# 🗞️ Daily News Sender

**Daily News Sender** is a simple Python application that automatically fetches the latest news and sends a daily email to a specified recipient. It's perfect for keeping yourself or others updated with the latest headlines.

## 🔧 Features

- Fetches top news articles using NewsAPI
- Cleans and formats article text
- Sends daily emails using SMTP
- Supports scheduled execution (e.g. via PythonAnywhere Tasks)
- Simple modular structure

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/daily-news-sender.git
cd daily-news-sender
````

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv / python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file with the following:

```
NEWS_API_KEY=your_newsapi_key
EMAIL_USER=your_email@example.com
EMAIL_PASSWORD=your_email_password
RECIPIENT=receiver@example.com
NEWS_API_ENDPOINT=newsapi_endpoint
```

### 5. Run the App

```bash
python main.py
```

## 📅 Scheduling (PythonAnywhere Example)

To run daily using PythonAnywhere Tasks, add this command:

```bash
source /home/yourusername/venv/bin/activate && \
cd /home/yourusername/daily-news-sender && \
python main.py >> log.txt 2>&1
```

> Replace `yourusername` with your actual PythonAnywhere username.

## 🛡️ Notes

- Do **not** upload your local `venv/` folder to PythonAnywhere.
- Use `requirements.txt` to install dependencies on the server.
- Logs are appended to `log.txt` for debugging.
- Ensure correct timezone settings when scheduling.

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute.

---
