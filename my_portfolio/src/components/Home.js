import { useState, useEffect } from "react";
import pic from '../assets/images/IMG_27701.jpg';
import { MdOutlineKeyboardArrowRight } from "react-icons/md";
import { Link } from 'react-scroll';
import 'animate.css';

const Home = () => {
  const [loopNum, setLoopNum] = useState(0);
  const [isDeleting, setIsDeleting] = useState(false);
  const [text, setText] = useState('');
  const [delta, setDelta] = useState(300 - Math.random() * 100);
  const toRotate = ["Frontend Web Developer", "Web Designer", "Graphic Designer"];
  const period = 2000;

  useEffect(() => {
    let ticker = setInterval(() => {
      tick();
    }, delta);

    return () => { clearInterval(ticker); };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [text, delta]);

  const tick = () => {
    let i = loopNum % toRotate.length;
    let fullText = toRotate[i];
    let updatedText = isDeleting ? fullText.substring(0, text.length - 1) : fullText.substring(0, text.length + 1);

    setText(updatedText);

    if (isDeleting) {
      setDelta(prevDelta => prevDelta / 2);
    }

    if (!isDeleting && updatedText === fullText) {
      setIsDeleting(true);
      setDelta(period);
    } else if (isDeleting && updatedText === '') {
      setIsDeleting(false);
      setLoopNum(loopNum + 1);
      setDelta(500);
    }
  }

  return (
    <div name="home"
      className='flex h-screen w-full bg-gradient-to-b from-black via-blue to-cyan-800 '
    >
      <div className='max-w-screen-lg mx-auto flex flex-col items-center justify-center h-full px-4 md:flex-row'>
        <div className='flex flex-col justify-center h-full'>
          <h2 className="text-4xl sm:text-7xl font-bold
           text-white">{`Hi! I'm Samuel, a`} <span className="text-4xl sm:text-7xl font-bold) txt-rotate" data-rotate='["Frontend Web Developer", "Web Designer", "Graphic Designer"]'><span className="wrap">{text}</span></span></h2>
          <p className='text-white w-half px-4 py-3 my-1 flex items-center rounded-md bg-gradient-to-r'>
            I have 1 year of experience building and developing/designing software.
            Currently, I love to work on web application using technologies like React,
            Tailwind, and HTML.
          </p>

          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div>
              <Link to="portfolio"
                smooth duration={500}
                className='text-white w-half px-4 py-3 my-1 flex items-center rounded-md bg-gradient-to-r from-cyan-500 to-blue-500'>
                Portfolio
                <span className='group-hover:rotate-90 duration-300'>
                  <MdOutlineKeyboardArrowRight size={25} className='ml-1' />
                </span>
              </Link>
            </div>
            <img src={pic} alt="my profile" className='rounded-2xl w-1/3 md:w-half' />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
