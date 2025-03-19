import React from "react";
import Footer from "../components/footer.jsx";
import CardDeckPrediction from "./card_detection/card_deck_prediction.jsx";
import TitleCard from "../components/title_card.jsx";
import "../styles/about_style.css";

function AboutPage() {
  const ValuesContainers = ({ title, description }) => {
    return (
      <div className="about-values-container">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    );
  };

  return (
    <div>
      <TitleCard
        title="About Us"
        description="Learn more about the Society of Hispanic Professional Engineers Tech Team at the University of Illinois at Urbana-Champaign."
      />

      <div className="about-mission">
        <h2>Our Mission</h2>
        <p>
          The Society of Hispanic Professional Engineers is a technical
          organization with a mission to empower the Hispanic community to
          realize its fullest potential and to impact the world through STEM
          awareness, access, support, and development.
        </p>
        <p>
          SHPE's Technical Team is dedicated to providing members with valuable
          technical experience while developing real-world engineering
          solutions. Our team works on various projects that allow members to
          apply classroom knowledge to practical challenges.
        </p>
        <p>
          We strive to create an inclusive environment where Hispanic engineers
          can grow professionally, develop leadership skills, and build a strong
          network of peers and mentors in the engineering field.
        </p>
      </div>
      <div className="about-history">
        <h2>Our History</h2>
        <p>
          The SHPE Tech Team at the University of Illinois at Urbana-Champaign
          was established to provide Hispanic engineering students with hands-on
          technical experience outside the classroom. What began as a small
          group of passionate students has grown into a vibrant community of
          engineers working on innovative projects.
        </p>
        <p>
          Over the years, our team has participated in numerous engineering
          competitions, hosted workshops, and developed projects that have made
          a positive impact on our campus and community. Our alumni have gone on
          to successful careers in various engineering fields, carrying forward
          the values and skills they developed as part of SHPE.
        </p>
        <p>
          Today, we continue to build on this legacy by embracing new
          technologies and tackling challenging engineering problems while
          fostering a supportive community for Hispanic engineers at UIUC.
        </p>
      </div>
      <div className="about-values">
        <h2>Our Values</h2>
        <div className="values-row">
          <ValuesContainers
            title="Exellence"
            description="We strive for excellence in all our technical projects and professional  endeavors, pushing the boundaries of what's possible through innovation  and dedication."
          />
          <ValuesContainers
            title="Collaboration"
            description="We believe in the power of teamwork and collaboration, bringing together diverse perspectives to solve complex engineering challenges."
          />
          <ValuesContainers
            title="Community"
            description="We are committed to building a supportive community that empowers  Hispanic engineers to achieve their full potential and make meaningful  contributions to society."
          />
        </div>
      </div>

      <Footer></Footer>
    </div>
  );
}

export default AboutPage;
