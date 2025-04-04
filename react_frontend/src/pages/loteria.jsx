import React from "react";
import "../styles/loteria_style.css";
import Footer from "../components/footer.jsx";
import F1 from "../../../runs/detect/loteria_model7/F1_curve.png";
import ValBatch from "../../../runs/detect/loteria_model7/val_batch0_pred.jpg"
import ConfusionMatrix from "../../../runs/detect/loteria_model7/confusion_matrix.png"
import Results from "../../../runs/detect/loteria_model7/results.png"
import TitleCard from "../components/title_card.jsx";

export default function Loteria() {
    return (
        <div className="body">
            <TitleCard
                title="AI Loteria"
                description="Experience our innovative robotic hand that brings American Sign Language (ASL) to life through mechanical engineering. This project combines precision robotics with accessibility, creating a bridge between technology and sign language communication."
            />
            
            <div className="model-results">
                <h2>Model Detection Results</h2>
                <p>Our AI model has been trained to recognize Loteria cards with high accuracy. Below are some examples of the model's performance.</p>
                
                <div className="results-gallery">
                    <div className="result-item">
                        <img src={ValBatch} alt="Validation Batch Predictions" />
                        <p>Model predictions on validation images. The AI accurately identifies multiple Loteria cards even when they overlap or are partially visible.</p>
                    </div>
                    
                    <div className="result-item">
                        <img src={ConfusionMatrix} alt="Confusion Matrix" />
                        <p>Confusion matrix showing the model's classification accuracy across different card types. The strong diagonal pattern indicates excellent performance.</p>
                    </div>
                    
                    <div className="result-item">
                        <img src={F1} alt="F1 Score Curve" />
                        <p>F1 confidence curve demonstrating the balance between precision and recall. Our model achieves high F1 scores across different confidence thresholds.</p>
                    </div>
                </div>
                
                <div className="performance-metrics">
                    <h2>Model Performance</h2>
                    <div className="metrics-container">
                        <div className="metric-item">
                            <img src={Results} alt="Training Results" />
                            <p>Training results over time showing improvements in both detection accuracy and loss reduction throughout the training process.</p>
                        </div>
                    </div>
                </div>
                
                <p className="model-conclusion">The AI Loteria model demonstrates robust performance in recognizing cards across various lighting conditions, angles, and partial occlusions, making it ideal for an interactive experience.</p>
            </div>
            < Footer />
        </div>
    );
}