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
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3051.4105037803615!2d-88.22954292341777!3d40.11085437419841!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880cd73ffb8e733b%3A0x550a408e89cd806!2sEngineering%20Hall%2C%201308%20W%20Green%20St%2C%20Urbana%2C%20IL%2061801!5e0!3m2!1sen!2sus!4v1761509553727!5m2!1sen!2sus" width="600" height="450" allowFullScreen="" loading="lazy" referrerPolicy="no-referrer-when-downgrade"></iframe>
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
          <iframe  title="PSA Instagram" src="https://www.instagram.com/shpe_uiuc/embed" width="400" height="480" frameBorder="0" scrolling="no" allowtransparency="true">…</iframe>

        </div>
      </div>
      <Footer></Footer>
    </div>
  );
}

export default ContactPage;
