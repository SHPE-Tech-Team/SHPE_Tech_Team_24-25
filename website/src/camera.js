import React, { useEffect, useRef } from 'react';


const ObjectDetection = () => {
  const videoRef = useRef(null);
  useEffect(() => {
    const load_video =  () => {
      if (videoRef.current) {
        videoRef.current.src = 'http://localhost:5000/predict';


        videoRef.current.onerror = () => {
          console.error("Error loading video feed. Check the backend stream.");
          setTimeout(load_video, 5000);
        };
      }
    }
    load_video();
  }, []);

  return (
    <div>
      <h2>Object Detection</h2>
      <img
        ref={videoRef}
        alt="Video feed"
        width="50%" 
        height="auto" 
      />
    </div>
  );
};

export default ObjectDetection;
