# 🤖 Revealing Mind AI - Super Agent

A modern AI agent system with three interface modes: Basic (simple), Intermediate (business), and Advanced (power users).

## 🚀 One-Click Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/revealing-mind-ai)

## ✨ Features

- **Basic Mode**: Delightfully simple chat interface for everyone
- **OpenAI Integration**: Real GPT-powered conversations
- **Responsive Design**: Works on desktop and mobile
- **Railway Ready**: One-click deployment

## 🔧 Setup

### 1. Deploy to Railway
1. Click the "Deploy on Railway" button above
2. Connect your GitHub account
3. Wait for automatic deployment

### 2. Add OpenAI API Key
1. Get API key from [platform.openai.com](https://platform.openai.com)
2. In Railway dashboard: Variables → Add `OPENAI_API_KEY`
3. Paste your key and save

### 3. Connect Custom Domain (Optional)
1. In Railway: Settings → Domains
2. Add your domain (e.g., `revealingmind.net`)
3. Update DNS settings

## 🎯 What's Included

### Phase 1A (Current)
- ✅ Basic Mode with real AI responses
- ✅ Feature flag system for future modes
- ✅ Professional UI/UX
- ✅ Mobile responsive design
- ✅ Railway deployment ready

### Coming Soon
- **Phase 1B**: Enhanced AI with memory
- **Phase 2**: Intermediate Mode for businesses
- **Phase 3**: Advanced Mode for developers

## 🏗️ Architecture

- **Frontend**: React + Vite + Tailwind CSS
- **Backend**: Flask + OpenAI API
- **Deployment**: Railway.app
- **Database**: In-memory (PostgreSQL ready)

## 📱 Mobile Friendly

Designed mobile-first with responsive interface that works perfectly on:
- iPhone/iPad
- Android devices  
- Desktop browsers
- Tablets

## 🔒 Security

- API keys stored securely in Railway environment
- CORS properly configured
- No sensitive data in code
- Production-ready security headers

## ⚙️ Environment Variables

- `OPENAI_API_KEY` - Required for AI features
- `SECRET_KEY` - Flask session secret (set in backend)
- `VITE_BACKEND_URL` - URL of the backend server during development

## 📞 Support

- **Issues**: Use GitHub Issues
- **Deployment Help**: Check `DEPLOYMENT.md`

This project is released under the [MIT License](../LICENSE).

---

**Built with ❤️ by Manus AI**  
Ready for `revealingmind.net`

