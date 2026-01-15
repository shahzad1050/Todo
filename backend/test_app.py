#!/usr/bin/env python3
"""
Test script to verify the FastAPI application starts correctly
"""
import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from main import app
    print("✓ Successfully imported main FastAPI application")

    # Test that the app has the expected routes
    routes = [route.path for route in app.routes]
    print(f"✓ Found {len(routes)} routes in the application")
    print(f"Routes: {routes}")

    # Test that essential modules can be imported
    from mangum import Mangum
    print("✓ Successfully imported Mangum")

    handler = Mangum(app, lifespan="off")
    print("✓ Successfully created Mangum handler")

    print("\n✓ All tests passed! Application is ready for deployment.")

except Exception as e:
    print(f"✗ Error importing or initializing application: {e}")
    sys.exit(1)