import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Change to the current directory to ensure imports work properly
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from main import app
from mangum import Mangum

# Create the Mangum handler to convert FastAPI app to AWS Lambda/Vercel function
handler = Mangum(app, lifespan="off")


def lambda_handler(event, context):
    """Wrapper for Vercel serverless functions"""
    return handler(event, context)