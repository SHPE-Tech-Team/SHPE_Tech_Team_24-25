import React from "react";
import Footer from "../components/footer.js"

function ContactPage() {
    return (
      <div className="contact">
        <div className="contact-background">
          <div className="contact-container">
            <h1>Contact Info</h1>
            
            <div className="contact-details">
                {/* Email Section */}
                <div className="contact-section">
                    <h2>Email</h2>
                    <p>
                        For general inquiries, email:
                        <a href="mailto:shpe.uiuc.president@gmail.com">shpe.uiuc.president@gmail.com</a>
                    </p>
                </div>
                {/* Location Section*/}
                <div className="contact-section">
                    <h2>Location</h2>
                    <p>Engineering Hall 103A</p>
                    <p>1308 W Green St.</p>
                    <p>Urbana, IL 61801</p>
                </div>

                {/* Social Media Section*/}
                <div className="contact-section">
                    <h2>Follow Us</h2>
                    <p>
                        Join our <a href="https:/www.facebook.com/groups/SHPE.UIUC">Facebook Group</a>!
                    </p>
                </div>
            </div>
          </div>
        </div>
        <Footer></Footer>
      </div>
    )
  }

export default ContactPage;
