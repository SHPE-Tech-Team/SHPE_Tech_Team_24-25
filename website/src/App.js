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
      <div style = {{textAlign: 'center', backgroundColor: '#041E42', color: 'white', minHeight: '100vh', padding: '20px'}}>
        <h1 style = {{fontSize: '50px'}}>SHPE TECH TEAM - AI Loteria</h1>

        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '20px' }}>
          <MyComponent />
          <h1>This project brings a new approach to the popular Latin American game Lotería. With using Python libraries that utilize convolutional neural networks and deep learning, Lotería can become fully automized.</h1>
          <Myvideo />
      </div>

      <ObjectDetection />
      <RealtimePrediction /> 
    </div>
  );
}


export default App;