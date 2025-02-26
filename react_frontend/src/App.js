import React,{ useState, useEffect }from "react";
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from "react-router-dom";
import ObjectDetection from './pages/card_detection/camera.js';
import RealtimePrediction from './pages/card_detection/data_predi.js';
import './styles/App.css';
import MembersPage from "./pages/members_page.js";
import AboutPage from "./pages/about_page.js";
import ContactPage from "./pages/contact_page.js";
import MyHand from "./pages/hand_project.js";
import MyAI from "./pages/ai_loteria.js"
import Projects from "./pages/projects.js";



function App() {
  return (   

    <div>
      <Router>
        <Routes>
          <Route path = "/" element = {<Navigate to="/projects"/>} />
          <Route path = "/projects" element = {<Projects/>} />
          <Route path = "/about" element = {<AboutPage/>} />
          <Route path = "/members" element = {<MembersPage/>} />
          <Route path = "/contact" element = {<ContactPage/>} />
        </Routes>
      </Router>

    </div>
  );
}


export default App;