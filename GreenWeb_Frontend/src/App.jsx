// App.jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Navbar   from './components/navbar/Navbar'
import Login    from './components/popup/login'
import SignUp   from './components/popup/sign_up'
import Hero     from './components/hero/Hero'
import ListProd from './components/listProduct/listProduct'
import Clip     from './components/clip/Clips'
import Footer   from './components/footer/Footer'
import Product from './components/after/Product'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Chỉ hiển thị form */}
        <Route path="/login"  element={<Login />} />
        <Route path="/signup" element={<SignUp />} />

        {/* Route riêng cho Product */}
        <Route path="/product" element={<Product />} />

        {/* Homepage với full layout */}
        <Route path="/" element={
          <>
            <Navbar />
            <Hero />
            <ListProd />
            <Clip />
            <Footer />
          </>
        }/>
      </Routes>
    </BrowserRouter>
  )
}
