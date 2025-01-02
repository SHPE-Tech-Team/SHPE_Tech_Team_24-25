import React, { useEffect, useRef } from 'react';


const ObjectDetection = () => {
  const videoRef = useRef(null);
  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.src = 'http://localhost:5000/predict';
    }
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
