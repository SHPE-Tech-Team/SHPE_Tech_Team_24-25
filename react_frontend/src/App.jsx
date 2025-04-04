import React, { useState, useEffect } from "react";
import {
  HashRouter,
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
import Loteria from "./pages/loteria.jsx";
import Robot from "./pages/robot.jsx"
import NavBar from "./components/nav.jsx";
import Vex from "./pages/vex.jsx";
import "./styles/App.css";

function App() {
  // Using HashRouter instead of BrowserRouter solves the page refresh issues
  // HashRouter uses URL hashes which don't trigger server requests on refresh
  return (
    <HashRouter>
      <div className="App">
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/projects" element={<Projects />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/members" element={<MembersPage />} />
          <Route path="/contact" element={<ContactPage />} />
          <Route path="/loteria" element={<Loteria />} />
          <Route path="/robot" element={<Robot />} />
          <Route path="/vex" element={<Vex />} />
        </Routes>
      </div>
    </HashRouter>
  );
}

export default App;
