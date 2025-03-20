import React from "react";
import Footer from "../components/footer.jsx";
import TitleCard from "../components/title_card.jsx";
import "../styles/contact_page_style.css";

function ContactPage() {
  return (
    <div>
      <TitleCard
        title="Contact Us"
        description="Get in touch with the Society of Hispanic Professional Engineers Tech Team at the University of Illinois at Urbana-Champaign. We're happy to answer any questions you may have."
      />

      <div className="contact-section">
        <h2>Get in Touch</h2>
        <div className="contact-container">
          <h3>Our Location</h3>
          <p>1308 W Green St Urbana, IL 61801 United States</p>
        </div>

        <div className="contact-container">
          <h3>Email Us</h3>
          <p>shpe-uiuc@illinois.edu</p>
          <p>techteam@shpe-uiuc.org</p>
        </div>

        <div className="contact-container">
          <h3>Follow Us</h3>
          <p>@shpe_uiuc_tech</p>
        </div>
      </div>
      <Footer></Footer>
    </div>
  );
}

export default ContactPage;
