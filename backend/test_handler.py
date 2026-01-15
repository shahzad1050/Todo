#!/usr/bin/env python3
"""
Test the API handler to ensure it works properly with Vercel-like requests
"""
import json

try:
    from api_handler import lambda_handler
    print("+ Successfully imported lambda handler")

    # Simulate a simple GET request to the root path
    event = {
        "httpMethod": "GET",
        "path": "/",
        "headers": {},
        "queryStringParameters": None,
        "body": None
    }

    context = {}

    response = lambda_handler(event, context)

    print(f"+ Handler executed successfully")
    print(f"Status Code: {response['statusCode']}")
    print(f"Headers: {list(response['headers'].keys())}")

    body = json.loads(response['body'])
    print(f"Response Body: {body}")

    if response['statusCode'] == 200:
        print("\n+ Test passed! Handler is working correctly.")
    else:
        print(f"\n- Test failed! Expected status 200, got {response['statusCode']}")

except ImportError as e:
    print(f"- Import error: {e}")
except Exception as e:
    print(f"- Error running handler: {e}")