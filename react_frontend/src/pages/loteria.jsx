import React from "react";
import "../styles/loteria_style.css";
import Footer from "../components/footer.jsx";
import F1 from "../../../runs/detect/loteria_model7/F1_curve.png";
import ValBatch from "../../../runs/detect/loteria_model7/val_batch0_pred.jpg"
import ConfusionMatrix from "../../../runs/detect/loteria_model7/confusion_matrix.png"
import Results from "../../../runs/detect/loteria_model7/results.png"

export default function Loteria() {
    return (
        <div className="body">
            <div className="title">
                <h2>Project 1</h2>
                <h1>AI Loteria</h1>
            </div>
            <div className="subtitle">
                <h3>AI Lotería brings a fresh and fun twist to the classic Mexican game of Lotería by mixing in some cool artificial intelligence technology. Using smart computer vision and machine learning, our system can spot and track cards instantly, making the game more interactive and exciting than ever before. It's all about combining tradition with tech to keep cultural favorites alive in a new and modern way. Come play and see how AI is adding extra fun to an old favorite!</h3>
            </div>
            
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