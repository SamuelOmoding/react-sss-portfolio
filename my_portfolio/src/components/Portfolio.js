// import React from 'react'
import uzuri from '../assets/uzuri_ltd.png';
import markdown from '../assets/markdowntopdf.png';
import vendors from '../assets/vendors.png';
import navbar from '../assets/navbar.png';
import nyumbani from '../assets/nyumbani.png';
import bookstore from '../assets/bookstore.png';

const Portfolio = () => {

    const portfolio = [
        {
            id: 1,
            src: uzuri,
            href: 'https://uzuri-ltd-dashboard-sp64.vercel.app/'     
        },
        {
            id: 2,
            src: markdown,
            href: 'https://app.screencastify.com/v2/manage/videos/520TTgqjkyooEonGUQk3',
        },
        {
            id: 3,
            src: vendors,
            href: 'https://vendor-sweets.onrender.com',
        },
        {
            id: 4,
            src: navbar,
            href: 'https://book-store-project-phi.vercel.app',
        },
        {
            id: 5,
            src: nyumbani,
            href: 'https://nyumbani-app-im96.vercel.app'
        }, 
        {
            id: 6,
            src: bookstore,
            href: 'https://book-store-project-phi.vercel.app'
        },
    ]

  return (
    <div name='portfolio' className='bg-gradient-to-b  from-black
    via-blue to-cyan-900 w-full text-white md:h-screen'
    > 
    <div className='max-w-screen-lg p-4 mx-auto flex flex-col
    justify-center w-full h-full'>
            <div className='pb-8'>
                <p className='text-4xl font-bold inline border-b-0
                border-gray-500'>
                  Portfolio</p>
                <p className='py-6'>Check out some of my work right here</p>
            </div>
    <div className='grid sm:grid-cols-2 md:grid-cols-3 gap-8
    px-12 sm:px-0'>
    {
    portfolio.map(({id, src, href}) => (
            <div key={id}
            className='shadow-md shadow-gray-600 rounded-lg'>
            <img 
            src={src} 
            alt='' 
            className='rounded-md duration-200 hover:scale-105'
            />
            <a 
            href={href} 
            className='flex justify-between items-center font-signature text-white'
            >
            <div className='flex items-center justify-center'>
                <button 
                    className='w-1/2 px-6 m-4 duration-200 hover:scale-105'
                >
                    Demo
                </button>
            </div>
            </a>

                {/* <button className='w-1/2 px-6 m-4 duration-200 
                hover:scale-105'>
                    Code
                    </button> */}
            </div>
        ))}
        </div>

        </div>
    </div>
  )
};

export default Portfolio;