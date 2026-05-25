## Deploy to Vercel

Vercel supports Flask via the Python runtime.

```bash
# 1. Install Vercel CLI
npm i -g vercel

# 2. Login
vercel login

# 3. Deploy (from the portfolio/ folder)
vercel --prod
```

The included `vercel.json` handles routing automatically.

> **Note:** Vercel's free tier may cold-start slowly. For always-on performance, use Render or PythonAnywhere instead.

---

## Deploy to Render (recommended for Flask)

1. Push this folder to a GitHub repo.
2. Go to [render.com](https://render.com) → New → Web Service.
3. Connect your repo.
4. Set:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
   - **Environment:** Python 3
5. Click Deploy. Done.

---

## Deploy to PythonAnywhere

1. Upload the project folder via the Files tab.
2. Create a new Web App → Flask → Python 3.x.
3. Set the source directory and WSGI file to point at `app.py`.
4. Reload the app.


