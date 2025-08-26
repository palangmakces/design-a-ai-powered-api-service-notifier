# AI-Powered API Service Notifier Configuration File

# Project Settings
PROJECT_NAME = "AI-Notifier"
PROJECT_DESCRIPTION = "AI-powered API service notifier for real-time event notifications"

# API Settings
API_URL = "https://api.example.com/notifier"
API_TOKEN = "your_api_token_here"
API_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

# AI Model Settings
AI_MODEL_URL = "https://model.example.com/predict"
AI_MODEL_TOKEN = "your_model_token_here"
AI_MODEL_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AI_MODEL_TOKEN}"
}

# Notification Settings
NOTIFICATION_TYPES = ["email", "slack", "sms"]
NOTIFICATION_PROVIDERS = {
    "email": {
        "FROM_EMAIL": "your_email@example.com",
        "SMTP_SERVER": "smtp.example.com",
        "SMTP_PORT": 587,
        "SMTP_USERNAME": "your_smtp_username",
        "SMTP_PASSWORD": "your_smtp_password"
    },
    "slack": {
        "SLACK_WEBHOOK_URL": "https://your_slack_webhook_url.com",
        "SLACK_CHANNEL": "#your_slack_channel"
    },
    "sms": {
        "TWILIO_ACCOUNT_SID": "your_twilio_account_sid",
        "TWILIO_AUTH_TOKEN": "your_twilio_auth_token",
        "TWILIO_PHONE_NUMBER": "+1234567890"
    }
}

# Event Settings
EVENT_TYPES = ["new_user", "payment_received", "system_error"]
EVENT_THRESHOLDS = {
    "new_user": 10,
    "payment_received": 100,
    "system_error": 1
}

# Logging Settings
LOGGING_LEVEL = "DEBUG"
LOGGING_FILE = "notifier.log"