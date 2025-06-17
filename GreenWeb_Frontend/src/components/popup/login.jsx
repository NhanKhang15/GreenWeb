import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import backgroundImage from "../../assets/background/login_background.jpg";

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [msg, setMsg] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMsg('');
    setLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();

      if (data.success) {
        // Lưu thông tin user vào localStorage
        localStorage.setItem('user', JSON.stringify(data.user));
        setMsg('Đăng nhập thành công!');
        // Chuyển hướng sau 1 giây để người dùng thấy thông báo thành công
        setTimeout(() => {
          navigate('/Banner');
        }, 1000);
      } else {
        setMsg(data.message || 'Đăng nhập thất bại');
      }
    } catch (err) {
      setMsg('Lỗi kết nối server. Vui lòng thử lại sau.');
      console.error('Login error:', err);
    } finally {
      setLoading(false);
    }
  };
  
  return (
    <div
      className="min-h-screen flex items-center justify-center bg-cover bg-center bg-fixed bg-no-repeat"
      style={{
        backgroundImage: `url(${backgroundImage})`,
        minHeight: '100vh',
        width: '100%',
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
      }}
    >
      <Link 
        to="/"
        className="absolute top-6 left-6 px-4 py-2 bg-white bg-opacity-30 backdrop-blur-md rounded-full text-gray-800 hover:bg-opacity-40 transition-all duration-300 flex items-center gap-2"
      >
        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path fillRule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clipRule="evenodd" />
        </svg>
        Back
      </Link>
      
      <div className="bg-white bg-opacity-30 backdrop-blur-md rounded-2xl p-8 w-full max-w-sm">
        <h2 className="text-[1.8rem] font-semibold text-center mb-6 text-gray-800">Login</h2>
        {msg && (
          <div className={`p-3 mb-4 rounded text-center ${
            msg.includes('thành công') 
              ? 'bg-green-100 text-green-700 border border-green-400' 
              : 'bg-red-100 text-red-700 border border-red-400'
          }`}>
            {msg}
          </div>
        )}
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="username" className="sr-only">
              Username
            </label>
            <input
              id="username"
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Username"
              className="w-full bg-transparent border-b-2 border-gray-300 placeholder-gray-500 text-gray-800 py-2 focus:outline-none focus:border-gray-500"
              disabled={loading}
            />
          </div>
          <div>
            <label htmlFor="password" className="sr-only">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Password"
              className="w-full bg-transparent border-b-2 border-gray-300 placeholder-gray-500 text-gray-800 py-2 focus:outline-none focus:border-gray-500"
              disabled={loading}
            />
          </div>
          <div className="flex items-center justify-between mt-4 text-gray-800">
            <label className="inline-flex items-center">
              <input type="checkbox" className="form-checkbox h-4 w-4 text-blue-600" />
              <span className="ml-2 text-sm">Remember me</span>
            </label>
            <Link to="/forgot-password" className="text-sm hover:underline">
              Forgot Password?
            </Link>
          </div>
          <button
            type="submit"
            disabled={loading}
            className={`w-full mt-6 py-2 rounded-full bg-blue-600 hover:bg-blue-700 text-white font-medium text-2xl transition-all duration-300 ${
              loading ? 'opacity-50 cursor-not-allowed' : ''
            }`}
          >
            {loading ? 'Đang đăng nhập...' : 'Login'}
          </button>
          <div className="mt-4 text-center space-y-2">
            <p className="text-gray-800">Welcome back to our website</p>
            <p className="text-sm text-gray-600">
              Don't have an account?{" "}
              <Link to="/signup" className="text-blue-600 hover:underline">
                Sign up
              </Link>
            </p>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
