# GreenWeb - E-commerce Website

A modern e-commerce website built with React frontend and Python Flask backend.

## Project Structure

```
Website/
├── Backend_GreenWeb/          # Python Flask Backend
│   ├── api/
│   │   ├── auth/             # Authentication APIs
│   │   └── hashPassword/     # Password hashing utilities
│   ├── database_Connection/  # Database connection
│   ├── app.py               # Main Flask application
│   └── requirements.txt     # Python dependencies
├── Database/                # SQL database files
├── GreenWeb_Frontend/       # React Frontend
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── assets/         # Images and static files
│   │   └── App.jsx         # Main React component
│   ├── package.json        # Node.js dependencies
│   └── vite.config.js      # Vite configuration
└── README.md               # This file
```

## Features

- **Frontend (React + Vite + Tailwind CSS)**
  - Modern responsive UI
  - Product listing and details
  - User authentication (login/signup)
  - Shopping cart functionality
  - Dark/Light mode toggle

- **Backend (Python Flask)**
  - RESTful API endpoints
  - User authentication and authorization
  - Password hashing and security
  - Database integration

## Getting Started

### Prerequisites

- Node.js (for frontend)
- Python 3.x (for backend)
- Git

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd GreenWeb_Frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd Backend_GreenWeb
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

## Technologies Used

- **Frontend:**
  - React.js
  - Vite
  - Tailwind CSS
  - JavaScript (ES6+)

- **Backend:**
  - Python
  - Flask
  - SQLAlchemy (if using ORM)

- **Database:**
  - SQL (see Database/SQLQuery1.sql)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License. 