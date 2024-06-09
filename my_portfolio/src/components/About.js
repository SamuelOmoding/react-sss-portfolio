
const About = () => {
  return (
    <div
      name="about"
      className="w-full h-screen bg-gradient-to-b  from-black
      via-blue to-cyan-800 text-white"
    >
      <div
        className="max-w-screen-lg p-4 mx-auto flex flex-col
    justify-center w-full h-full"
      >
        <div className="pb-8">
          <p
            className="text-4xl font-bold inline border-b-4 
            border-gray-500"
          >
            About
          </p>
        </div>

        <p className="text-xl mt-20">
        I am a web designer and developer with one year of experience in creating 
        visually appealing and functional websites. I have developed expertise in 
        designing responsive navigation bars and am proficient in HTML, CSS, and JavaScript, 
        as well as popular CSS frameworks such as Tailwind and Bootstrap. My skill set enables 
        me to deliver responsive and user-friendly web solutions that meet the demands of modern digital environments.
        </p>
        <br />

      </div>
    </div>
  );
};

export default About