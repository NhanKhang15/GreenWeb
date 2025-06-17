// src/components/header/Navbar.jsx
import React from 'react'
import { Link } from 'react-router-dom'

const Navbar = () => {
  const menuItems = ['Portfolio', 'About', 'Contact', 'Sign Up', 'Login']

  return (
    <header className="relative min-h-[740px] text-center
      [background-image:linear-gradient(#00000091,_#222),url('https://cdn.prod.website-files.com/67e2c5bcd8d91826d120509e/67e2c5bcd8d91826d120512c_fe4a5cbf.jpg')]
      [background-position:0_0,_38%] [background-repeat:repeat,_no-repeat]
      [background-size:auto,_cover]
    ">
      <nav className="pt-[28px] z-[1000] bg-transparent relative">
        <div className="max-w-[940px] mx-auto flex items-center">
          <Link to="/" className="p-[15px] text-white text-[26px] leading-[30px] font-[Lato,sans-serif] no-underline">
            VERSUS
          </Link>
          <div className="ml-auto flex">
            {menuItems.map((name, idx) => {
              let toPath = '/'
              if (name === 'Portfolio') toPath = '/'
              else if (name === 'Sign Up') toPath = '/signup'
              else if (name === 'Login')   toPath = '/login'
              else toPath = `/${name.toLowerCase()}`

              return (
                <Link
                  key={idx}
                  to={toPath}
                  className={`
                    inline-block p-[20px] text-[14px] leading-[17px]
                    font-[Lato,sans-serif] uppercase tracking-[1px]
                    ${name === 'Portfolio' ? 'text-[#69A634]' : 'text-[#c9c8c8] hover:text-white'}
                    transition-colors duration-200
                  `}
                >
                  {name}
                </Link>
              )
            })}
          </div>
        </div>
      </nav>

      {/* Hero */}
      <div className="max-w-[940px] mx-auto mt-[140px] px-[10%]">
        <h1 className="text-[48px] font-light leading-[59px] text-white mb-[39px]">
          We build beautiful web and mobile apps.
        </h1>
        <Link
          to="/signup"
          className="inline-block text-[#69A634] uppercase bg-transparent
                     border border-[#69A634] rounded-[3px]
                     px-[40px] py-0 text-[18px] font-light leading-[50px]
                     transition-all duration-200 hover:text-white hover:border-white"
        >
          Get a quote
        </Link>
      </div>
    </header>
  )
}

export default Navbar
