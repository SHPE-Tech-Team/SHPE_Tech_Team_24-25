import React from "react";
import Footer from "../components/footer.jsx"
import TitleCard from "../components/title_card.jsx";

function ContactPage() {
    return (
      <div >
        <TitleCard
          title="Contact Us"
          description="Get in touch with the Society of Hispanic Professional Engineers Tech Team at the University of Illinois at Urbana-Champaign. We're happy to answer any questions you may have."
        />
        <Footer></Footer>
      </div>
    )
  }

export default ContactPage;
