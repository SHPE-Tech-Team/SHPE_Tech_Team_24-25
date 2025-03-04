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
import "./styles/App.css";
import NavBar from "./components/nav.jsx";

function App() {
  return (
    <Router>
      <div>
        <NavBar/>
        <Routes>
          <Route path="/" element={<Navigate to="/projects" />} />
          <Route path="/projects" element={<Projects />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/members" element={<MembersPage />} />
          <Route path="/contact" element={<ContactPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
