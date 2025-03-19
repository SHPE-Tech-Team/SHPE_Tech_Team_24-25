import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  Navigate,
} from "react-router-dom";
import MembersPage from "./pages/members_page.jsx";
import AboutPage from "./pages/about_page.jsx";
import ContactPage from "./pages/contact_page.jsx";
import Projects from "./pages/projects.jsx";
import Home from "./pages/home.jsx";
import AI_loteria from "./pages/ai_loteria.jsx";
import NavBar from "./components/nav.jsx";


import "./styles/App.css";


function App() {
  return (
    <Router>
      <div className="App">
        <NavBar />
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/projects" element={<Projects />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/members" element={<MembersPage />} />
          <Route path="/contact" element={<ContactPage />} />
          <Route path="/teddy" element={<AI_loteria />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
