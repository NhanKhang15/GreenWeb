import React from 'react'

const youtube = () => {
  return (
    <div className="relative w-full pt-[50%] overflow-hidden bg-[#222]">
      <h3 className="absolute top-[17%] left-1/2 -translate-x-1/2 text-white text-center mb-8 text-3xl font-light">
        The advertise video
      </h3>
      <iframe
        className="absolute top-1/2 left-1/2 w-1/2 h-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none border-0"
        src="https://www.youtube-nocookie.com/embed/JOiGpref=en?rel=0&controls=0&autoplay=1&mute=1&loop=1&playlist=JOiGEI9pQBs&cc_load_policy=0&cc_lang_pref=en"
        allow="autoplay; encrypted-media"
        allowFullScreen
      />
    </div>
  )
}

export default youtube