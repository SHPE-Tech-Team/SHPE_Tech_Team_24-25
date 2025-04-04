import React from "react";
import "../styles/robot_style.css";
import Footer from "../components/footer.jsx";
import TitleCard from "../components/title_card.jsx";

export default function Robot() {
    return (
        <div className="body">
            <TitleCard
                title="ASL Robotic Arm"
                description="Experience our innovative robotic hand that brings American Sign Language (ASL) to life through mechanical engineering. This project combines precision robotics with accessibility, creating a bridge between technology and sign language communication."
            />
            <div className="gallery">
                <h2>Project Gallery</h2>
                <div className="mosaic-gallery">
                    <div className="gallery-item wide">
                        <img src="/home_media/robotic_arm_side.jpg" alt="Robot Overview" />
                        <p className="caption">Full view of our ASL robot hand</p>
                    </div>
                    <div className="gallery-item">
                        <img src="/home_media/hand_close_up.jpeg" alt="Hand Close-up" />
                        <p className="caption">Detailed view of robotic hand joints</p>
                    </div>
                    <div className="gallery-item tall">
                        <img src="/home_media/team_testing.jpg" alt="Testing Session" />
                        <p className="caption">Testing session at Electrical and Computer Engineering Building (ECEB)</p>
                    </div>
                    <div className="gallery-item wide tall">
                        <img src="/home_media/tech_team_group_picture.jpg" alt="Team" />
                        <p className="caption">Our dedicated team of developers and engineers</p>
                    </div>
                    <div className="gallery-item">
                        <img src="/home_media/project_development.jpeg" alt="Development" />
                        <p className="caption">Development process</p>
                    </div>
                    <div className="gallery-item wide">
                        <img src="/home_media/team_brainstorming.jpeg" alt="Team during a brainstorming session" />
                        <p className="caption">Team brainstorming session</p>
                    </div>
                </div>
            </div>
            <Footer/>
        </div>
    )
}
