// import React from 'react';
import logo from '../assets/images/redlogo.png';
import { MdOutlineKeyboardArrowRight } from "react-icons/md";
import { Link } from 'react-scroll';

const Home = () => {
  return (
    <div name="home" 
    className='flex h-screen w-full bg-gradient-to-b from-black
    via-black to-gray-800 '
    >
      <div className='max-w-screen-lg mx-auto flex flex-col
      items-center justify-center h-full px-4 md:flex-row'>
        <div className='flex flex-col justify-center h-full'>
          <h2 className='text-4xl sm:text-7xl font-bold
          text-white'>
            I am a Full Stack Developer</h2>
          <p className='text-white'>
            I have 1 year of experience building and developing/designing software.
            Currently, I love to work on web application using technologies like React, 
            Tailwind, and HTML.
          </p>

          <div>
            <Link to="portfolio" 
            smooth duration={500}
            className='text-white w-half px-6 py-3 my-0
            flex items-center rounded-md bg-gradient-to-r
            from-cyan-500 to-blue-500'>
              Portfolio
              <span className='group-hover:rotate-90 duration-300'>
              <MdOutlineKeyboardArrowRight size={25} 
              className='ml-1'/>
              </span>
            </Link>
          </div>
          <img src={logo} alt="my profile" 
          className='rounded-2xl mx-auto w-1/3 md:w-half'
          />
        </div>
      </div>
    </div>
  );
};

export default Home;