/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html", 
    "./src/**/*.{js,jsx,ts,tsx}"
  ],

  theme: {
    extend: {
      colors: {
        primary: "#69A634",    
        secondary: "#4ECDC4",  
      },
    },
  },
  plugins: [],
}

