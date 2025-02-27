import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  Navigate,
} from "react-router-dom";
import MembersPage from "./pages/members_page.js";
import AboutPage from "./pages/about_page.js";
import ContactPage from "./pages/contact_page.js";
import Projects from "./pages/projects.js";
import "./styles/App.css";
import NavBar from "./components/nav.js";

function App() {
  return (
    // <div>
    //   <Router>
    //     <Routes>
    //       <Route path="/" element={<Navigate to="/projects" />} />
    //       <Route path="/projects" element={<Projects />} />
    //       <Route path="/about" element={<AboutPage />} />
    //       <Route path="/members" element={<MembersPage />} />
    //       <Route path="/contact" element={<ContactPage />} />
    //     </Routes>
    //   </Router>
    //   <React.Fragment>
    //     <NavBar />
    //   </React.Fragment>
    // </div>

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
