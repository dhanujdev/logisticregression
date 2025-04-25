import axios from 'axios';

const apiClient = axios.create({
    // Ensure NEXT_PUBLIC_ prefix for client-side environment variables
    baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1',
    headers: {
        'Content-Type': 'application/json',
        // Add Authorization header if/when authentication is implemented
        // 'Authorization': `Bearer ${token}`
    }
});

export default apiClient; 