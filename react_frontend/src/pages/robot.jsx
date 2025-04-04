import React from "react";
import "../styles/robot_style.css";
import Footer from "../components/footer.jsx";

export default function Robot() {
    return (
        <div className="body">
            <div className="title">
                <h2>Project 2</h2>
                <h1>ASL Robot</h1>
            </div>
            <div className="subtitle">
                <h3>The ASL Robot is all about breaking down barriers between the hearing and Deaf communities in a fun and engaging way. Powered by advanced robotics, our robot accurately performs American Sign Language (ASL) gestures. It's a creative and practical way to make communication easier and more inclusive for everyone. Experience firsthand how technology can open up new possibilities, empowering people to connect better in all sorts of situations.</h3>
            </div>
            <div className="gallery">
                <h2>Project Gallery</h2>
                <div className="mosaic-gallery">
                    <div className="gallery-item wide">
                        <img src="/robot_media/robot1.jpg" alt="Robot Overview" />
                        <p className="caption">Full view of our ASL Robot in action</p>
                    </div>
                    <div className="gallery-item">
                        <img src="./../public/home_media/hand_close_up.jpeg" alt="Hand Close-up" />
                        <p className="caption">Detailed view of robotic hand joints</p>
                    </div>
                    <div className="gallery-item tall">
                        <img src="../../public/home_media/team_testing.jpg" alt="Testing Session" />
                        <p className="caption">Testing session at Electrical and Computer Engineering Building (ECEB)</p>
                    </div>
                    <div className="gallery-item wide tall">
                        <img src="../../public/home_media/tech_team_group_picture.jpg" alt="Team" />
                        <p className="caption">Our dedicated team of developers and engineers</p>
                    </div>
                    <div className="gallery-item">
                        <img src="../../public/home_media/project_development.jpeg" alt="Development" />
                        <p className="caption">Development process</p>
                    </div>
                    <div className="gallery-item wide">
                        <img src="../../public/home_media/team_brainstorming.jpeg" alt="Team during a brainstorming session" />
                        <p className="caption">Team brainstorming session</p>
                    </div>
                </div>
            </div>
            <Footer/>
        </div>
    )
}
