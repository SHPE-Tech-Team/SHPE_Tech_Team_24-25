import React, { useState } from "react";

function MyComponent() {
  const [isToggled, setIsToggled] = useState(false);

  const handleToggle = () => {
    setIsToggled(!isToggled);
  };

  return (
    <div>
      <button onClick={handleToggle}>{isToggled ? "ON" : "OFF"}</button>
      {isToggled && (
        <div>
          <p>This content is visible when the toggle is ON.</p>
        </div>
      )}
    </div>
  );
}

export default MyComponent;
