from main import app
from mangum import Mangum

# Create the Mangum handler to convert FastAPI app to Vercel serverless function
handler = Mangum(app, lifespan="off")