# dash_github_page

# Dash App GitHub Pages Deployment

This is a ready-to-deploy Plotly Dash application configured for GitHub Pages deployment.

## 📁 Project Structure

```
my-dash-app/
├── app.py                          # Main Dash application
├── requirements.txt                # Python dependencies
├── Procfile                        # Deployment configuration
├── .gitignore                      # Git ignore file
├── .github/
│   └── workflows/
│       └── deploy.yml              # GitHub Actions workflow
└── README.md                       # This file
```

## 🚀 Quick Setup & Deployment

### Step 1: Create GitHub Repository
1. Go to [GitHub](https://github.com/new)
2. Create a **new public repository** named: `my-dash-app`
3. Do NOT initialize with README/gitignore

### Step 2: Local Setup
```bash
# Clone locally (or create new folder)
mkdir my-dash-app
cd my-dash-app

# Initialize git
git init
git branch -M main

# Create virtual environment
python -m venv venv

# Activate venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Add All Files
Copy all the files (app.py, requirements.txt, Procfile, .gitignore, .github/workflows/deploy.yml) into your `my-dash-app` folder.

### Step 4: Test Locally (Optional)
```bash
python app.py
# Visit http://localhost:8050 in your browser
```

### Step 5: Push to GitHub
```bash
git add .
git commit -m "Initial Dash app deployment setup"
git remote add origin https://github.com/YOUR_USERNAME/my-dash-app.git
git push -u origin main
```

### Step 6: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select **main** branch and **/root** folder
4. Click **Save**

### Step 7: Deploy to Render (for hosting)

Since GitHub Pages doesn't support Python/Dash server-side execution, we'll use **Render** (free tier available):

1. Go to [Render.com](https://render.com)
2. Sign up with GitHub
3. Click **New +** → **Web Service**
4. Connect your GitHub repository
5. Fill in the details:
   - **Name**: my-dash-app
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:server`
6. Click **Create Web Service**
7. Once deployed, your app will be live at a URL like: `https://my-dash-app-xxx.onrender.com`

**Optional - Auto-deploy on push:**
1. On Render dashboard, go to your service
2. Click **Settings** → Copy the "Deploy Hook" URL
3. Go to GitHub repo → **Settings** → **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Name: `RENDER_DEPLOY_HOOK`
6. Value: Paste the Deploy Hook URL
7. Now every push to main will auto-deploy!

## 🔧 Customization

Edit `app.py` to:
- Change dashboard title, colors, and layout
- Modify the sample data or add your own CSV
- Add more interactive components and callbacks
- Update the data source

## 📚 Resources

- [Dash Documentation](https://dash.plotly.com/)
- [Plotly Documentation](https://plotly.com/python/)
- [Render Deployment Guide](https://render.com/docs)

## ⚠️ Important Notes

- **GitHub Pages** hosts static content only (cannot run Python)
- **Render, Heroku, Railway, or similar** can host your full Dash app
- Use the **Procfile** to configure how your app runs on these platforms
- Free tier on Render has limitations but is sufficient for demos

## 🎯 Next Steps

1. Customize the dashboard with your own data
2. Deploy to Render for live hosting
3. Share your live URL!

Enjoy! 🚀