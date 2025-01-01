import React,{ useState, useEffect, use }from "react";


function App() {
  const [data, setData] = useState([{}]);
  useEffect(() => {
    fetch("/predict")
      .then((res) => res.json())
      .then((data) => {setData(data)
      console.log(data)
      });
  }, []);
  return (
    <div>
      <h1>Hello, World!</h1>
    </div>
  );
}

export default App;