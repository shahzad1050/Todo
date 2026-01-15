// frontend/src/app/api/[...path]/route.ts
import { NextRequest } from 'next/server';

// This API route acts as a proxy to the Python backend
export async function GET(request: NextRequest, { params }: { params: { path: string[] } }) {
  try {
    const path = params.path.join('/');
    const backendPath = `/api/${path}`;
    const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000';
    const backendEndpoint = `${BACKEND_URL}${backendPath}`;

    // Forward headers from the original request
    const headers: Record<string, string> = {};
    request.headers.forEach((value, key) => {
      headers[key] = value;
    });

    // Remove host header to prevent issues with backend
    delete headers['host'];

    // Make request to the Python backend
    const response = await fetch(backendEndpoint, {
      method: 'GET',
      headers,
    });

    // Copy response headers
    const responseHeaders = new Headers(response.headers);

    // Return the response from the backend
    return new Response(await response.text(), {
      status: response.status,
      headers: responseHeaders,
    });
  } catch (error) {
    console.error('Proxy error:', error);
    return new Response(JSON.stringify({ error: 'Backend service unavailable' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}

export async function POST(request: NextRequest, { params }: { params: { path: string[] } }) {
  try {
    const path = params.path.join('/');
    const backendPath = `/api/${path}`;
    const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000';
    const backendEndpoint = `${BACKEND_URL}${backendPath}`;

    // Get request body
    const body = await request.text();

    // Forward headers from the original request
    const headers: Record<string, string> = {};
    request.headers.forEach((value, key) => {
      headers[key] = value;
    });

    // Remove host header to prevent issues with backend
    delete headers['host'];

    // Make request to the Python backend
    const response = await fetch(backendEndpoint, {
      method: 'POST',
      headers,
      body,
    });

    // Copy response headers
    const responseHeaders = new Headers(response.headers);

    // Return the response from the backend
    return new Response(await response.text(), {
      status: response.status,
      headers: responseHeaders,
    });
  } catch (error) {
    console.error('Proxy error:', error);
    return new Response(JSON.stringify({ error: 'Backend service unavailable' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}

export async function PUT(request: NextRequest, { params }: { params: { path: string[] } }) {
  try {
    const path = params.path.join('/');
    const backendPath = `/api/${path}`;
    const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000';
    const backendEndpoint = `${BACKEND_URL}${backendPath}`;

    // Get request body
    const body = await request.text();

    // Forward headers from the original request
    const headers: Record<string, string> = {};
    request.headers.forEach((value, key) => {
      headers[key] = value;
    });

    // Remove host header to prevent issues with backend
    delete headers['host'];

    // Make request to the Python backend
    const response = await fetch(backendEndpoint, {
      method: 'PUT',
      headers,
      body,
    });

    // Copy response headers
    const responseHeaders = new Headers(response.headers);

    // Return the response from the backend
    return new Response(await response.text(), {
      status: response.status,
      headers: responseHeaders,
    });
  } catch (error) {
    console.error('Proxy error:', error);
    return new Response(JSON.stringify({ error: 'Backend service unavailable' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}

export async function PATCH(request: NextRequest, { params }: { params: { path: string[] } }) {
  try {
    const path = params.path.join('/');
    const backendPath = `/api/${path}`;
    const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000';
    const backendEndpoint = `${BACKEND_URL}${backendPath}`;

    // Get request body
    const body = await request.text();

    // Forward headers from the original request
    const headers: Record<string, string> = {};
    request.headers.forEach((value, key) => {
      headers[key] = value;
    });

    // Remove host header to prevent issues with backend
    delete headers['host'];

    // Make request to the Python backend
    const response = await fetch(backendEndpoint, {
      method: 'PATCH',
      headers,
      body,
    });

    // Copy response headers
    const responseHeaders = new Headers(response.headers);

    // Return the response from the backend
    return new Response(await response.text(), {
      status: response.status,
      headers: responseHeaders,
    });
  } catch (error) {
    console.error('Proxy error:', error);
    return new Response(JSON.stringify({ error: 'Backend service unavailable' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}

export async function DELETE(request: NextRequest, { params }: { params: { path: string[] } }) {
  try {
    const path = params.path.join('/');
    const backendPath = `/api/${path}`;
    const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000';
    const backendEndpoint = `${BACKEND_URL}${backendPath}`;

    // Forward headers from the original request
    const headers: Record<string, string> = {};
    request.headers.forEach((value, key) => {
      headers[key] = value;
    });

    // Remove host header to prevent issues with backend
    delete headers['host'];

    // Make request to the Python backend
    const response = await fetch(backendEndpoint, {
      method: 'DELETE',
      headers,
    });

    // Copy response headers
    const responseHeaders = new Headers(response.headers);

    // Return the response from the backend
    return new Response(await response.text(), {
      status: response.status,
      headers: responseHeaders,
    });
  } catch (error) {
    console.error('Proxy error:', error);
    return new Response(JSON.stringify({ error: 'Backend service unavailable' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}