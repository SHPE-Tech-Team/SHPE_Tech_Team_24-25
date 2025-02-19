import React,{ useState, useEffect }from "react";
import ObjectDetection from './camera';
import RealtimePrediction from './data_predi';
import myImage from "./loteria.png";
import myVid from "./print.mp4";



function MyComponent() {
  return <img src={myImage} alt = "3D Printing" width = '900' height = '500' />;
}

function Myvideo() {
  return (
  <video width = "750" height = "500" controls>
    <source src={myVid} type = "video/mp4"/>
  </video>
  );
}

function App() {
  return (
      <div style = {{textAlign: 'center'}}>
        <h1>SHPE TECH TEAM - AI Loteria</h1>

        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '20px' }}>
          <MyComponent />
          <Myvideo />
      </div>

      
      <ObjectDetection />
      <RealtimePrediction /> 
    </div>
  );
}


export default App;