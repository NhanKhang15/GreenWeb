import React from 'react';

const List = () => (
  <div className="pt-12 pb-12 bg-[#222]">
    <div className="max-w-4xl mx-auto ">
      <h3 className="text-white text-center tracking-normal normal-case mb-8 text-3xl font-light">
        Latest Work
      </h3>
      <div className="w-dyn-list">
        <div className="w-dyn-items -ml-2.5 -mr-2.5 flex flex-wrap " role="list">
          {[
            { href: '/projects/music-player', src: '', srcSet: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205177_zip-code-800-p-800x.jpeg 800w', alt: '' },
            { href: '/projects/console-app',   src: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205173_thum.png', srcSet: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205173_thum-p-500x.png 500w', alt: '' },
            { href: '/projects/infographic',   src: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205178_cthulu_van_v2.jpg', srcSet: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205178_cthulu_van_v2-p-800x.jpeg 800w', alt: '' },
            { href: '/projects/sports-car-app', src: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205171_fan.png', srcSet: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205171_fan-p-800x.png 800w', alt: '' },
            { href: '/projects/music-app',      src: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205175_human.jpg', srcSet: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205175_human-p-800x.jpeg 800w', alt: '' },
            { href: '/projects/photo-app-icon', src: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205174_dribbble.png', srcSet: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205174_dribbble-p-800x.png 800w', alt: '' },
            { href: '/projects/news-feed',     src: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205172_sans_titre_-_17-01.png', srcSet: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205172_sans_titre_-_17-01-p-500x.png 500w', alt: '' },
            { href: '/projects/photo-app',      src: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205176_astrav1.jpg', srcSet: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d1205176_astrav1-p-800x.jpeg 800w', alt: '' },
            { href: '/projects/flat-design',   src: 'https://cdn.prod.website-files.com/67e2c5bcd8d91826d1205148/67e2c5bcd8d91826d120515c_neighborhood.jpg', alt: '' },
          ].map((item, idx) => (
            <div key={idx} className="w-dyn-item w-1/3 pl-2.5 pr-2.5 mb-5">
              <a className="max-w-full inline-block" href={item.href}>
                <img
                  className="rounded-sm"
                  src={item.src}
                  srcSet={item.srcSet}
                  sizes="(max-width: 767px) 96vw, (max-width: 991px) 30vw, 300px"
                  alt={item.alt}
                />
              </a>
            </div>
          ))}
        </div>
      </div>
    </div>
  </div>
);

export default List;
