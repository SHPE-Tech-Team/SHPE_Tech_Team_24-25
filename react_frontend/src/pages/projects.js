import React from "react";
import ObjectDetection from "./card_detection/camera.js";
import RealtimePrediction from "./card_detection/data_predi.js";
import { Link } from "react-router-dom";
import "../styles/App.css";

function Printvid() {
  return (
    <video width="600" height="500" controls>
      <source src={"/home_media/print.mp4"} type="video/mp4" />
    </video>
  );
}

function Navbar() {
  return (
    <nav className="navbar">
      <ul className="nav-links">
        <li>
          <link to="/"> Home </link>
        </li>
        <li>
          <a href="#">Members</a>
        </li>
        <li>
          <a href="#"> sheehs </a>
        </li>
        <li>
          <a href="#">Contact</a>
        </li>
        <li>
          <a href="#">Hand Project</a>
        </li>
        <li>
          <a href="#">AI Loteria</a>
        </li>
      </ul>
    </nav>
  );
}

// Jorge to organize it better and make it prettier
/// Do figma concept before programming  !!!!!!!!!!!!

function Hero() {
  return (
    <div className="hero">
      <div className="hero-images">
        <div className="hero-image left">
          <img src="https://images.pexels.com/photos/546819/pexels-photo-546819.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="A close-up photograph of computer code displayed on a monitor, featuring syntax-highlighted text on a dark background."></img>
        </div>
        <div className="hero-image right">
          <img src="https://images.pexels.com/photos/8386363/pexels-photo-8386363.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="A close-up of a robotic hand reaching upward against a vibrant blue background, symbolizing futuristic technology and innovation."></img>
        </div>
      </div>
      <div className="hero-text">
        <h1>Engineering Open House 2025</h1>
        <h2>The Age of Innovation</h2>
        {/* To-Do: Add 2 buttons to explore each project  */}
        <div className="hero-buttons">
          <a href="#loteria"><button className="loteria-button">AI Loteria</button></a>
          <a href="#robot"><button className="robot-button">ASL Robot</button></a>
        </div>
      </div>
    </div>
  )
}

function ProjectLoteria() {
  return (
    <div className="loteria" id="loteria">
      <div className="loteria-background">
        <div className="loteria-text">
          <h2>Project 1</h2>
          <h1>AI Loteria</h1>
          <p>Lorem ipsum odor amet, consectetuer adipiscing elit. Euismod massa donec taciti tristique accumsan nulla phasellus risus. Augue rhoncus a taciti pretium dignissim interdum. Consectetur sollicitudin parturient etiam tempor mauris congue. Suspendisse suspendisse posuere venenatis semper; est mi. Massa luctus at dis velit facilisis pharetra leo. Quis elit erat magnis commodo vulputate potenti.
          </p>
        </div>
        <div className="loteria-video">
          <ObjectDetection />
        </div>
      </div>
    </div>
  )
}

function ProjectRobot() {
  return (
    <div className="robot" id="robot">
      <div className="robot-background">
        <div className="robot-text">
          <h2>Project 2</h2>
          <h1>ASL Robot</h1>
          <p>Lorem ipsum odor amet, consectetuer adipiscing elit. Euismod massa donec taciti tristique accumsan nulla phasellus risus. Augue rhoncus a taciti pretium dignissim interdum. Consectetur sollicitudin parturient etiam tempor mauris congue. Suspendisse suspendisse posuere venenatis semper; est mi. Massa luctus at dis velit facilisis pharetra leo. Quis elit erat magnis commodo vulputate potenti.
          </p>
        </div>
        <div className="robot-video">
          <Printvid />
        </div>
      </div>
    </div>
  )
}

function Team() {
  return (
    <div className="team">
      <div className="team-background">
        <div className="team-text">
          <h1>Meet the Team</h1>
          <h2>Software</h2>
          <div className="members">
            <p>Jorge Becerra</p>
            <p>John Doe</p>
            <p>Jane Doe</p>
          </div>
          <h2>Hardware</h2>
          <div className="members">
            <p>Jorge Becerra</p>
            <p>John Doe</p>
            <p>Jane Doe</p>
          </div>
        </div>
      </div>
    </div>
  )
}

function About() {
  return (
    <div className="about">
      <div className="about-background">
        <div className="about-text">
          <h1>About</h1>
        </div>
      </div>
    </div>
  )
}

function Contact() {
  return (
    <div className="contact">
      <div className="contact-background">
        <div className="contact-text">
          <h1>Contact</h1>
        </div>
      </div>
    </div>
  )
}

function Footer() {
  return (
    <div className="footer">
      <div className="footer-background">
        <div className="footer-nav">
          <Link to="/projects">Projects</Link>
          <Link to="/about">About</Link>
          <Link to="/members">Members</Link>
          <Link to="/contact">Contact</Link>
        </div>
        <div className="social-links">
          <a rel="noreferrer" href="https://www.instagram.com/shpe_uiuc/?hl=en" target="_blank"><img src="https://img.icons8.com/win10/512/FFFFFF/instagram-new.png" alt="Instagram Logo in white"></img></a>
          <a rel="noreferrer" href="https://github.com/SHPE-Tech-Team/AI_Loteria_24-25" target="_blank"><img src="https://img.icons8.com/ios11/512/FFFFFF/github.png" alt="Github Logo in white"></img></a>
          <a rel="noreferrer" href="https://www.linkedin.com/groups/13627278/" target="_blank"><img src="https://img.icons8.com/?size=100&id=44914&format=png&color=FFFFFF" alt="LinkedIn Logo in white"></img></a>
        </div>
      </div>
    </div>
  )
}

function Projects() {
  return (
    <div>
      <div style={{ textAlign: "center" }}>
        <Hero />
        <ProjectLoteria />
        <ProjectRobot />
        <Team />
        <About />
        <Contact />
        <Footer />
      </div>
    </div>
  );
}

export default Projects;
