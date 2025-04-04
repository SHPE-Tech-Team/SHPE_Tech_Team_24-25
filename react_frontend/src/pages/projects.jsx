import React from "react";
import ObjectDetection from "./card_detection/camera.jsx";
import RealtimePrediction from "./card_detection/data_predi.jsx";
import TitleCard from "../components/title_card.jsx";
import { Link } from "react-router-dom";
import "../styles/projects_style.css";
import Footer from "../components/footer.jsx";


function Printvid() {
  return (
    <video width="600" height="500" controls>
      <source
        src={import.meta.env.BASE_URL + "home_media/print.mp4"}
        type="video/mp4"
      />
    </video>
  );
}

function Hero() {
  return (
    <div className="hero">
      <div className="hero-images">
        <div className="hero-image left">
          <img
            src={import.meta.env.BASE_URL + "projects_media/code.jpeg"}
            alt="A close-up photograph of computer code displayed on a monitor, featuring syntax-highlighted text on a dark background."
          ></img>
        </div>
        <div className="hero-image right">
          <img
            src= {import.meta.env.BASE_URL + "projects_media/robot.jpeg"}
            alt= "A close-up of a robotic hand reaching upward against a vibrant blue background, symbolizing futuristic technology and innovation."
          ></img>
        </div>
      </div>
      <div className="hero-text">
        <div className="hero-title">
          <h1>Engineering Open House 2025</h1>
        </div>
        <h2>The Age of Innovation</h2>
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
        <div className="loteria-text full-width-on-mobile">
          <h2>Project 1</h2>
          <h1>AI Loteria</h1>
          <p className="project-description">
            AI Lotería brings a fresh and fun twist to the classic Mexican game of Lotería by mixing in some cool artificial intelligence technology. Using smart computer vision and machine learning, our system can spot and track cards instantly, making the game more interactive and exciting than ever before. It's all about combining tradition with tech to keep cultural favorites alive in a new and modern way. Come play and see how AI is adding extra fun to an old favorite!
          </p>
          <Link to="/loteria">
            <button className="robot-button">Learn more</button>
          </Link>
        </div>
        <div className="loteria-video hide-on-mobile">
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
        <div className="robot-text full-width-on-mobile">
          <h2>Project 2</h2>
          <h1>ASL Robot</h1>
          <p className="project-description">
            The ASL Robot is all about breaking down barriers between the hearing and Deaf communities in a fun and engaging way. Powered by advanced robotics, our robot accurately performs American Sign Language (ASL) gestures. It's a creative and practical way to make communication easier and more inclusive for everyone. Experience firsthand how technology can open up new possibilities, empowering people to connect better in all sorts of situations.
          </p>
          <a href="#loteria">
            <button className="loteria-button">Learn more</button>
          </a>
        </div>
        <div className="robot-video hide-on-mobile">
          <Printvid />
        </div>
      </div>
    </div>
  );
}

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
