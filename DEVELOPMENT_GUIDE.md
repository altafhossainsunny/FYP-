# SecureCrop - Complete Local Development Setup

## Prerequisites
- Anaconda installed
- Git installed

## Quick Start Guide

### 1. Backend Setup (Already Done ✅)
The backend is already running at http://127.0.0.1:8000/

### 2. Frontend Setup

#### Option A: Using conda environment (Recommended)
```bash
# Activate the environment
conda activate fyp

# Navigate to frontend directory
cd c:\Users\Public\Fyp\SecureCrop\frontend

# Install dependencies (using the node.js we installed)
C:\Anaconda3\envs\fyp\node.exe -e "console.log('Node.js working')"
# If above works, install npm packages:
C:\Anaconda3\envs\fyp\npm.cmd install
```

#### Option B: Using system Node.js (if you have it)
```bash
# Navigate to frontend directory  
cd c:\Users\Public\Fyp\SecureCrop\frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

#### Option C: Install Node.js globally
1. Download Node.js from https://nodejs.org/
2. Install it
3. Open new terminal and run:
```bash
cd c:\Users\Public\Fyp\SecureCrop\frontend
npm install
npm run dev
```

### 3. Running Both Services

#### Terminal 1 - Backend (Already Running)
```bash
conda activate fyp
cd c:\Users\Public\Fyp\SecureCrop\backend
python manage.py runserver
```
- Backend API: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/ (admin/admin123)

#### Terminal 2 - Frontend
```bash
cd c:\Users\Public\Fyp\SecureCrop\frontend
npm run dev
```
- Frontend App: http://localhost:3000/

### 4. Application Features

Once both are running, you can access:

**Public Pages:**
- Landing Page: http://localhost:3000/
- Services: http://localhost:3000/services
- About Us: http://localhost:3000/about
- Contact: http://localhost:3000/contact
- Login: http://localhost:3000/login
- Register: http://localhost:3000/register

**User Dashboard (after login):**
- Dashboard: http://localhost:3000/user/dashboard
- Soil Input: http://localhost:3000/user/soil-input
- Weather: http://localhost:3000/user/weather
- Market Linkage: http://localhost:3000/user/market-linkage
- History: http://localhost:3000/user/history
- Feedback: http://localhost:3000/user/feedback
- Profile: http://localhost:3000/user/profile

**Admin Panel (admin users only):**
- Admin Dashboard: http://localhost:3000/admin/dashboard
- User Management: http://localhost:3000/admin/users
- Soil Input Management: http://localhost:3000/admin/soil-inputs
- Cyber Logs: http://localhost:3000/admin/cyber-logs
- Admin Logs: http://localhost:3000/admin/admin-logs
- Weather Alerts: http://localhost:3000/admin/weather-alerts
- Contact Inquiries: http://localhost:3000/admin/contact-inquiries

### 5. API Endpoints (Backend)
- API Root: http://127.0.0.1:8000/
- Authentication: http://127.0.0.1:8000/api/auth/
- Soil Inputs: http://127.0.0.1:8000/api/soil-inputs/
- Recommendations: http://127.0.0.1:8000/api/recommendations/
- Weather: http://127.0.0.1:8000/api/weather/
- And more...

## Environment Configuration

### Backend Environment Variables (.env)
Located at: `backend/.env`
```
SECRET_KEY=your-secret-key-here-change-in-production-123456789abcdef
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,securecrop.onrender.com
# Add your API keys for full functionality
OPENWEATHER_API_KEY=your-key-here
```

### Frontend Proxy Configuration
The frontend is configured to proxy API calls to Django backend via vite.config.ts:
- Frontend requests to `/api/*` → Backend `http://localhost:8000/api/*`

## Troubleshooting

1. **Backend Issues:**
   - Ensure conda environment `fyp` is activated
   - Check if migrations ran: `python manage.py migrate`
   - Check if superuser exists: admin/admin123

2. **Frontend Issues:**
   - Ensure Node.js is installed and accessible
   - Try clearing npm cache: `npm cache clean --force`
   - Delete node_modules and reinstall: `rm -rf node_modules && npm install`

3. **CORS Issues:**
   - Backend is configured to allow localhost:3000
   - Check browser console for specific errors

## Technology Stack

### Backend (Django REST API)
- Django 4.2.7
- Django REST Framework
- JWT Authentication
- PostgreSQL/SQLite
- Machine Learning (scikit-learn, pandas)
- Cybersecurity features
- WhatsApp integration (Infobip)
- Email notifications

### Frontend (React with Vite)
- React 18
- TypeScript
- Tailwind CSS
- React Router
- Axios for API calls
- Leaflet for maps
- i18n for internationalization

## Database
- Development: SQLite (automatic)
- Production: PostgreSQL (Render.com)

Current database includes:
- User management with profiles
- Soil input data
- ML recommendations
- Weather data
- Market linkage information
- Cybersecurity logs
- Contact inquiries
- Feedback system