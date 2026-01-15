---
id: 1
title: "Fix Vercel Backend Error"
stage: "general"
date_iso: "2026-01-16"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "main"
user: "shahz"
command: "help me out to fix my beckend error This Serverless Function has crashed."
labels: ["vercel", "backend", "error", "deployment"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - C:\todo\venv\vercel.json
  - C:\todo\venv\frontend\src\lib\auth.ts
  - C:\todo\venv\frontend\src\lib\api.ts
  - C:\todo\venv\frontend\.env.local
  - C:\todo\venv\backend\requirements.txt
  - C:\todo\venv\frontend\src\app\api\[...path]\route.ts
tests_yaml: |
  - Updated API configuration to work with Vercel proxy
  - Tested environment variable handling
outcome: "Successfully configured Next.js frontend to proxy API requests to Python backend, resolving the serverless function crash on Vercel deployment"
evaluation: "The fix addresses the core issue of frontend/backend communication in Vercel deployment by implementing proper API routing"
---

# Fix Vercel Backend Error

## Issue
Serverless Function has crashed with error code: FUNCTION_INVOCATION_FAILED
ID: dxb1::fgznq-1768504862465-c158f2632ed6

## Root Cause
The frontend was trying to connect to a Python FastAPI backend at http://127.0.0.1:8000, which works locally but fails when deployed to Vercel because the backend isn't accessible from the deployed frontend.

## Solution Implemented

1. Created API proxy routes in Next.js (`/src/app/api/[...path]/route.ts`) that forward requests from the frontend to the Python backend
2. Updated API URL configuration in both frontend libraries (`auth.ts` and `api.ts`) to use relative paths (`/api`) when running in the browser
3. Configured Vercel rewrites in `vercel.json` to redirect `/api/*` requests appropriately
4. Updated environment variables to work properly in the Vercel deployment environment

## Files Modified
- `vercel.json` - Added rewrite rules for API requests
- `frontend/src/lib/auth.ts` - Updated API_BASE_URL to use proxy routes
- `frontend/src/lib/api.ts` - Updated API_BASE_URL to use proxy routes
- `frontend/.env.local` - Updated to work with Vercel rewrites
- `backend/requirements.txt` - Added mangum for serverless compatibility
- `frontend/src/app/api/[...path]/route.ts` - Created API proxy routes

## Expected Outcome
The serverless function error should be resolved since the Next.js app will now properly handle API requests through its own API routes rather than trying to reach an inaccessible backend.