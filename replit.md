# SecureCrop - AI-Powered Agriculture Platform

## Overview
SecureCrop is a full-stack web application that provides farmers with AI-driven soil analysis, weather forecasts, and personalized crop recommendations.

## Project Structure
- **backend/**: Django REST API with PostgreSQL database
  - `accounts/`: User authentication and management
  - `soil/`: Soil input data handling
  - `recommendations/`: ML-based crop recommendations
  - `weather/`: Weather data integration
  - `ml_engine/`: Machine learning prediction engine
  - `cyber_layer/`: Cybersecurity checks and anomaly detection
  - `logs/`: Security logging
  - `contact/`: Contact inquiry handling
  - `feedback/`: User feedback system
  - `notifications/`: Alert and notification system
  - `market_linkage/`: Market information

- **frontend/**: React + TypeScript application built with Vite
  - `src/pages/`: Main application pages
  - `src/components/`: Reusable UI components
  - `src/services/`: API service functions
  - `src/contexts/`: React context providers

## Tech Stack
- **Backend**: Django 4.2, Django REST Framework, PostgreSQL
- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS
- **ML**: scikit-learn, pandas, SHAP for explainable AI

## Running the Application
- Frontend runs on port 5000 (with Vite dev server)
- Backend runs on port 8000 (Django development server)
- API endpoints are proxied from `/api/*` to the backend

## Database
Using Replit's built-in PostgreSQL database. Environment variables:
- `DATABASE_URL`: Full connection string
- `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, `PGDATABASE`: Individual connection parameters

## Environment Variables
- `DEBUG`: Set to 'True' for development mode
- `REPLIT`: Set to '1' to enable Replit-specific configurations
- `OPENWEATHER_API_KEY`: For weather data integration (optional)
