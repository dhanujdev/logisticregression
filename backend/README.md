# AI Tutor for Instagram Creators - Backend Service

## 🚀 Overview

AI Tutor is a revolutionary SaaS platform that transforms Instagram engagement into personalized learning experiences. Built for content creators, course builders, and educational influencers, our platform automatically generates customized project materials and tracks learner progress through Instagram interactions.

### 🎯 Key Features

- **Instagram Webhook Integration**: Automatically capture and process likes and comments
- **AI-Powered Project Generation**: LangChain + Google Gemini for intelligent content creation
- **Automated PDF Generation**: Professional course materials delivered instantly
- **Progress Tracking**: Monitor learner engagement through Instagram interactions
- **Scalable Architecture**: Built with FastAPI, Celery, and Supabase

## 🛠 Tech Stack

- **Core Framework**: FastAPI
- **AI/ML**: LangChain + Google Gemini API
- **Task Queue**: Celery with Redis
- **Database**: PostgreSQL via Supabase
- **Documentation**: OpenAPI/Swagger
- **PDF Generation**: WeasyPrint
- **Email Service**: SendGrid
- **Container**: Docker

## 🏗 Architecture

```
┌──────────────┐   Webhooks   ┌───────────────┐    RPC/REST   ┌──────────────┐
│ Instagram    │◀──────────▶│ FastAPI Core  │◀────────────▶│ Next.js UI   │
│ Graph API    │             │ (Business API)│              │ (Creator)     │
└──────────────┘             │  ├─ LangChain  │              └──────────────┘
                             │  │  Agent      │
                             │  ├─ Celery     │ async jobs
                             │  ├─ PDF Engine │
                             │  └─ Email      │
                             └───────────────┘
                                   ▲  ▲
                                   │  │
                           Postgres/Supabase
```

## 📁 Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── instagram.py    # Webhook handlers
│   │       ├── creators.py     # Creator management
│   │       └── projects.py     # Project generation
│   ├── core/
│   │   ├── config.py          # Environment & settings
│   │   └── deps.py            # Dependencies
│   ├── models/
│   │   └── models.py          # Database models
│   └── services/
│       ├── ai_service.py      # LangChain integration
│       ├── pdf_service.py     # PDF generation
│       └── email_service.py   # Email notifications
├── main.py                    # Application entry
└── requirements.txt           # Dependencies
```

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-tutor-instagram.git
   cd ai-tutor-instagram/backend
   ```

2. Set up virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

5. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```

## 🔑 Environment Variables

Required environment variables:
- `INSTAGRAM_APP_ID`: Instagram API credentials
- `INSTAGRAM_APP_SECRET`: Instagram API secret
- `SUPABASE_URL`: Supabase project URL
- `SUPABASE_KEY`: Supabase API key
- `GEMINI_API_KEY`: Google Gemini API key
- `SENDGRID_API_KEY`: SendGrid email service key
- `REDIS_URL`: Redis connection URL

## 📚 API Documentation

API documentation is available at `/docs` when running the server (Swagger UI).

## 🔄 Workflow

1. **Creator Onboarding**
   - Instagram OAuth authentication
   - Profile setup and plan selection

2. **Content Processing**
   - Webhook receives Instagram interactions
   - AI generates personalized projects
   - PDF materials auto-generated

3. **Progress Tracking**
   - Automatic learner progress updates
   - Analytics dashboard for creators

## 💡 Features for Creators

- **Automated Response**: Generate personalized project materials from comments
- **Progress Tracking**: Monitor student engagement through likes and comments
- **Analytics Dashboard**: Track learner progress and engagement metrics
- **Customizable Templates**: Tailor AI responses to your teaching style
- **Scalable Infrastructure**: Handle growing communities effortlessly

## 🛡 Security

- JWT authentication
- Instagram OAuth 2.0
- Rate limiting
- Request validation
- Data encryption

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 