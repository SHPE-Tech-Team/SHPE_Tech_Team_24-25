import React from "react";
import ObjectDetection from "./card_detection/camera.js";
import RealtimePrediction from "./card_detection/data_predi.js";
import "../styles/App.css";

function Printvid() {
  return (
    <video width="750" height="500" controls>
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

function Projects() {
  return (
    <div>
      <div style={{ textAlign: "center" }}>
        <h1 style={{ color: "red" }}>Jorge this is your page to do</h1>
        <h1 style={{ color: "red" }}>
          Do figma concept before programming !!!!!!!!!!!!
        </h1>
        <h1>Engineering Open House 2025</h1>
        <h3>
          <em>The Age of Innovation</em>
        </h3>

        <h4>Project 1</h4>
        <h2>AI Loteria</h2>
        <div className="video-container">
          <ObjectDetection />
          {/* <RealtimePrediction />  */}
        </div>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: "20px",
          }}
        >
          <Printvid />

          <h3>Made by SHPE UIUC Tech Team</h3>
        </div>
      </div>
    </div>
  );
}

export default Projects;
