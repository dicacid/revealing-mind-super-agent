# Railway Deployment Guide - Revealing Mind AI Super Agent

## 🚀 One-Click Deployment to Railway

This guide will help you deploy your Revealing Mind AI Super Agent to Railway.app in just a few minutes.

## Prerequisites

1. **GitHub Account** - You'll need this to connect Railway
2. **Railway Account** - Sign up at [railway.app](https://railway.app) (free tier available)
3. **Your Project Repository** - The code needs to be in a GitHub repository

## Step 1: Prepare Your Repository

First, make sure all your code is committed and pushed to GitHub:

```bash
# In your project directory
git add .
git commit -m "Ready for Railway deployment"
git push origin main
```

## Step 2: Deploy to Railway

### Option A: Deploy Button (Easiest)

1. Go to your GitHub repository
2. Add this button to your README:
   ```markdown
   [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME)
   ```
3. Click the button and follow the prompts

### Option B: Manual Deployment

1. **Visit Railway**
   - Go to [railway.app](https://railway.app)
   - Click "Start a New Project"

2. **Connect GitHub**
   - Click "Deploy from GitHub repo"
   - Authorize Railway to access your repositories
   - Select your project repository

3. **Automatic Detection**
   - Railway will automatically detect your project configuration
   - It will use the `railway.json` and `Procfile` we created
   - Both files define the start command `python backend/src/main.py` (no
     virtualenv activation needed)

4. **Wait for Build**
   - Railway will build your project (takes 2-3 minutes)
   - You'll see the build logs in real-time

## Step 3: Configure Environment Variables (Optional)

If you need to set environment variables:

1. In Railway dashboard, click on your project
2. Go to "Variables" tab
3. Add any required variables:
   - `FLASK_SECRET_KEY` - A secure random string
   - `NODE_ENV` - Set to "production"

## Step 4: Get Your Live URL

1. Once deployment is complete, Railway will provide a URL
2. It will look like: `https://your-app-name.railway.app`
3. Click the URL to test your deployed application

## Step 5: Connect Custom Domain (Optional)

To use `revealingmind.net`:

1. **In Railway Dashboard:**
   - Go to your project settings
   - Click "Domains"
   - Click "Add Domain"
   - Enter `revealingmind.net`

2. **Update DNS at OrangeHost:**
   - Log into your OrangeHost control panel
   - Go to DNS management
   - Add a CNAME record:
     - Name: `@` (or leave blank for root domain)
     - Value: `your-app-name.railway.app`
   - Add a CNAME record for www:
     - Name: `www`
     - Value: `your-app-name.railway.app`

3. **Wait for Propagation:**
   - DNS changes can take up to 24 hours
   - Usually works within 1-2 hours

## Step 6: Test Your Deployment

1. **Visit Your Site**
   - Go to your Railway URL or custom domain
   - You should see the Revealing Mind AI interface

2. **Test Chat Functionality**
   - Type a message in the chat
   - Verify you get an AI response
   - Check that the interface is responsive on mobile

3. **Check Health Endpoint**
   - Visit `https://your-domain.com/api/health`
   - Should return: `{"status": "healthy", ...}`

## Troubleshooting

### Common Issues and Solutions

**1. Build Fails**
```
Error: No such file or directory
```
**Solution:** Make sure all files are committed and pushed to GitHub

**2. App Crashes on Start**
```
Error: Port already in use
```
**Solution:** Railway automatically assigns ports. Make sure your app uses `process.env.PORT`

**3. Frontend Not Loading**
```
404 Not Found
```
**Solution:** Ensure the frontend build files are in `backend/src/static/`

**4. API Calls Failing**
```
CORS Error
```
**Solution:** Check that Flask-CORS is properly configured in your backend

**5. Custom Domain Not Working**
```
DNS_PROBE_FINISHED_NXDOMAIN
```
**Solution:** 
- Verify DNS records are correct
- Wait for DNS propagation (up to 24 hours)
- Use Railway's provided URL while waiting

### Getting Help

**Railway Support:**
- Railway Discord: [discord.gg/railway](https://discord.gg/railway)
- Railway Docs: [docs.railway.app](https://docs.railway.app)

**Project Support:**
- GitHub Issues: Create an issue in your repository
- Check the logs in Railway dashboard for error details

## Cost Estimation

**Railway Pricing:**
- **Free Tier:** $0/month
  - 500 hours of usage
  - Perfect for testing and small projects
  
- **Pro Plan:** $20/month
  - Unlimited usage
  - Custom domains
  - Priority support

**Domain Costs:**
- Keep your existing domain with OrangeHost
- No additional domain costs

## Monitoring and Maintenance

**Railway Dashboard:**
- Monitor app performance
- View logs and metrics
- Manage deployments
- Scale resources if needed

**Automatic Updates:**
- Connect Railway to your GitHub repository
- Automatic deployments on every push to main branch
- Rollback capability if issues occur

## Security Checklist

Before going live:

- [ ] Change default Flask secret key
- [ ] Set up HTTPS (Railway provides this automatically)
- [ ] Review CORS settings
- [ ] Test all functionality thoroughly
- [ ] Set up monitoring and alerts

## Next Steps

Once deployed successfully:

1. **Share Your URL** - Test with friends and colleagues
2. **Gather Feedback** - Use the Basic Mode to collect user feedback
3. **Plan Phase 1B** - Prepare for AI provider integration
4. **Monitor Usage** - Watch Railway metrics for performance

## Success! 🎉

Your Revealing Mind AI Super Agent is now live and accessible to users worldwide. The delightfully simple Basic Mode interface is ready for non-technical users to enjoy.

**What You've Accomplished:**
- ✅ Professional AI chat interface
- ✅ Responsive design (works on all devices)
- ✅ Production-ready deployment
- ✅ Custom domain capability
- ✅ Scalable architecture for future features

**Ready for Phase 1B:**
- Real AI provider integration
- Enhanced conversation capabilities
- Tool system implementation
- Intermediate and Advanced modes

---

**Need Help?** Create an issue in your GitHub repository or reach out to the development team.

**Celebrating?** Share your success! Your AI agent is now live at `revealingmind.net`

