'use client'; // Required for useState and event handlers

import { useState } from 'react';
import apiClient from '../lib/apiClient'; // Adjust path if needed

export default function Home() {
  const [postUrl, setPostUrl] = useState('');
  const [commentText, setCommentText] = useState('');
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setIsLoading(true);
    setMessage('');
    setError('');

    if (!postUrl || !commentText || !username) {
        setError('Please fill in Post URL, Comment Text, and Username.');
        setIsLoading(false);
        return;
    }

    try {
      const payload = {
        instagram_post_url: postUrl,
        comment_text: commentText,
        requester_instagram_username: username,
        requester_email: email || null, // Send null if email is empty
        // creator_id will be handled by the backend (using placeholder for now)
      };

      // Use the imported apiClient
      const response = await apiClient.post('/projects/generate-project', payload);

      setMessage(response.data.message || 'Project generation request submitted successfully!');
      // Clear form on success
      setPostUrl('');
      setCommentText('');
      setUsername('');
      setEmail('');

    } catch (err: any) {
      console.error("API Error:", err);
      setError(err.response?.data?.detail || 'An error occurred while submitting the request.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-6 md:p-24 bg-gray-50">
      <div className="w-full max-w-2xl bg-white p-8 rounded-lg shadow-md">
        <h1 className="text-2xl font-bold mb-6 text-center text-gray-800">
          Generate Project from Instagram Comment (MVP)
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="postUrl" className="block text-sm font-medium text-gray-700 mb-1">
              Instagram Post URL <span className="text-red-500">*</span>
            </label>
            <input
              type="url"
              id="postUrl"
              value={postUrl}
              onChange={(e) => setPostUrl(e.target.value)}
              placeholder="https://www.instagram.com/p/C.../"
              required
              className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>

          <div>
            <label htmlFor="commentText" className="block text-sm font-medium text-gray-700 mb-1">
              Comment Text <span className="text-red-500">*</span>
            </label>
            <textarea
              id="commentText"
              rows={3}
              value={commentText}
              onChange={(e) => setCommentText(e.target.value)}
              placeholder='e.g., "Make me a spotify clone"'
              required
              className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            ></textarea>
          </div>

          <div>
            <label htmlFor="username" className="block text-sm font-medium text-gray-700 mb-1">
              Requester's Instagram Username <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="e.g., coding_learner"
              required
              className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>

          <div>
            <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
              Requester's Email (Optional - for delivery)
            </label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="user@example.com"
              className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>

          <button
            type="submit"
            disabled={isLoading}
            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isLoading ? 'Submitting...' : 'Generate Project'}
          </button>
        </form>

        {message && (
          <div className="mt-4 p-3 bg-green-100 border border-green-400 text-green-700 rounded">
            {message}
          </div>
        )}
        {error && (
          <div className="mt-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded">
            {error}
          </div>
        )}
      </div>
    </main>
  );
}
