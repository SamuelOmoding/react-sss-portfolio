// import React from 'react'
import js from '../assets/js.png';
import css from '../assets/CSS.png';
import react from '../assets/react.png';
import node from '../assets/nodejs.png';
import html from '../assets/html.png';
import psql from '../assets/psql.png';
import ubuntu from '../assets/ubuntu.png';
import github from '../assets/github.png';

const Experience = () => {

    const techs = [
        {
            id: 1,
            src: js,
            title: 'JAVASCRIPT',
            style: 'shadow-yellow-200'
        },
        {
            id: 2,
            src: css,
            title: 'CSS',
            style: 'shadow-blue-500'

        },
        {
            id: 3,
            src: react,
            title: 'REACT',
            style: 'shadow-blue-300'

        },
        {
            id: 4,
            src: node,
            title: 'NODEJS',
            style: 'shadow-lime-500'

        },
        {
            id: 5,
            src: html,
            title: 'HTML',
            style: 'shadow-orange-700'

        },
        {
            id: 6,
            src: psql,
            title: 'POSTGRESQL',
            style: 'shadow-blue-900'

        },
        {
            id: 7,
            src: ubuntu,
            title: 'UBUNTU',
            style: 'shadow-orange-700'

        },
        {
            id: 8,
            src: github,
            title: 'GITHUB',
            style: 'shadow-black'
        },
    ]
  return (
    <div 
    name='experience' 
    className='bg-gradient-to-b from-black
    to-gray-800 w-full text-white md:h-screen'
    > 
        <div className='max-w-screen-lg mx-auto p-4 flex flex-col 
        justify-center w-full h-full white-black'>
            <div>
            <p className='text-4xl font-bold border-b-4 
            border-gray-500 p-2 inline'>
                Experience
                </p>
            <p className='py-6'>These are the technologies I have worked with</p>
        </div>
        <div className='w-full grid grid-cols-2 sm:grid-cols-3
        gap-8 text-center py-8 px-12 sm:px-0'>

           {techs.map(({id, src, title, style}) => (
                <div 
                key={id}
                className={`shadow-md hover:scale-105 duration-500
                py-2 rounded-lg ${style}`}
                >
                    <img src={src} alt='' className='w-20 mx-auto'/>
                    <p className='mt-4'>{title}</p>
                </div>
            ))
           }
        </div>
    </div>
    </div>
  );
};

export default Experience;