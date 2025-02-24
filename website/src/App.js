import React,{ useState, useEffect }from "react";
import ObjectDetection from './camera';
import RealtimePrediction from './data_predi';
import myImage from "./loteria.png";
import myVid from "./print.mp4";
import './App.css';
import MyMembers from "./members.js";
import MyAbout from "./about.js";
import MyContact from "./contact.js";
import MyHand from "./hand_project.js";
import MyAI from "./ai_loteria.js"


function Myvideo() {
  return (
  <video width = "750" height = "500" controls>
    <source src={myVid} type = "video/mp4"/>
  </video>
  );
}

function Navbar() {
  return (
  <nav className="navbar">
    <ul className="nav-links">
      <li><a href="#">Home</a></li>
      <li><a href="#">Members</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
      <li><a href="#">Hand Project</a></li>
      <li><a href="#">AI Loteria</a></li>

    </ul>
</nav>
);
}


function App() {
  return (   
     <div>
     <Navbar></Navbar>
       <div style = {{textAlign: 'center'}}>
        
         <h1>Engineering Open House 2025</h1>
         <h3><em>The Age of Innovation</em></h3>

         <h4>Project 1</h4>
         <h2>AI Loteria</h2>
         <div className="video-container">
           <ObjectDetection />
           {/* <RealtimePrediction />  */}
         </div>
         <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '20px' }}>
          
           <Myvideo />

           <h3>Made by SHPE UIUC Tech Team</h3>
         </div>      
     </div>
     </div>
    
  );
}


export default App;