import React from "react";
import ObjectDetection from "./card_detection/camera.jsx";
import RealtimePrediction from "./card_detection/data_predi.jsx";
import TitleCard from "../components/title_card.jsx";
import { Link } from "react-router-dom";
import "../styles/App.css";
import Footer from "../components/footer.jsx";

function Printvid() {
  return (
    <video width="600" height="500" controls>
      <source
        src={"/AI_Loteria_24-25/home_media/print.mp4"}
        type="video/mp4"
      />
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
          <img
            src="https://images.pexels.com/photos/546819/pexels-photo-546819.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
            alt="A close-up photograph of computer code displayed on a monitor, featuring syntax-highlighted text on a dark background."
          ></img>
        </div>
        <div className="hero-image right">
          <img
            src="https://images.pexels.com/photos/8386363/pexels-photo-8386363.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
            alt="A close-up of a robotic hand reaching upward against a vibrant blue background, symbolizing futuristic technology and innovation."
          ></img>
        </div>
      </div>
      <div className="hero-text">
        <h1>Engineering Open House 2025</h1>
        <h2>The Age of Innovation</h2>
        {/* To-Do: Add 2 buttons to explore each project  */}
        <div className="hero-buttons">
          <a href="#loteria">
            <button className="loteria-button">AI Loteria</button>
          </a>
          <a href="#robot">
            <button className="robot-button">ASL Robot</button>
          </a>
        </div>
      </div>
    </div>
  );
}

function ProjectLoteria() {
  return (
    <div className="loteria" id="loteria">
      <div className="loteria-background">
        <div className="loteria-text">
          <h2>Project 1</h2>
          <h1>AI Loteria</h1>
          <p>
            Lorem ipsum odor amet, consectetuer adipiscing elit. Euismod massa
            donec taciti tristique accumsan nulla phasellus risus. Augue rhoncus
            a taciti pretium dignissim interdum. Consectetur sollicitudin
            parturient etiam tempor mauris congue. Suspendisse suspendisse
            posuere venenatis semper; est mi. Massa luctus at dis velit
            facilisis pharetra leo. Quis elit erat magnis commodo vulputate
            potenti.
          </p>
        </div>
        <div className="loteria-video">
          <ObjectDetection />
        </div>
      </div>
    </div>
  );
}

function ProjectRobot() {
  return (
    <div className="robot" id="robot">
      <div className="robot-background">
        <div className="robot-text">
          <h2>Project 2</h2>
          <h1>ASL Robot</h1>
          <p>
            Lorem ipsum odor amet, consectetuer adipiscing elit. Euismod massa
            donec taciti tristique accumsan nulla phasellus risus. Augue rhoncus
            a taciti pretium dignissim interdum. Consectetur sollicitudin
            parturient etiam tempor mauris congue. Suspendisse suspendisse
            posuere venenatis semper; est mi. Massa luctus at dis velit
            facilisis pharetra leo. Quis elit erat magnis commodo vulputate
            potenti.
          </p>
        </div>
        <div className="robot-video">
          <Printvid />
        </div>
      </div>
    </div>
  );
}

// EDIT: Added Software Team Names
function Team() {
  return (
    <div className="team">
      <div className="team-background">
        <div className="team-text">
          <h1>Meet the Team</h1>
          <h2>Software</h2>
          <div className="members">
            <p>Jorge Becerra</p>
            <p>Daniel Quillo</p>
            <p>Kevin "LaFlame" Cruz</p>
            <p>Antonio Tapia</p>
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
  );
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
  );
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
  );
}

//EDIT: Removed Team, About, and Contact pages from main page
function Projects() {
  return (
    <div>
      <TitleCard
        title={"Projects"}
        description={
          "Explore the innovative engineering projects developed by the SHPE Tech Team, showcasing our technical skills and commitment to excellence."
        }
      />
      <div style={{ textAlign: "center" }}>
        <Hero />
        <ProjectLoteria />
        <ProjectRobot />
        <Footer></Footer>
      </div>
    </div>
  );
}

export default Projects;
