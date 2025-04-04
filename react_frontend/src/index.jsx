import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import reportWebVitals from "./reportWebVitals.jsx";

try {
  // Process redirect from 404.html using the new spa-path key
  const spaPath = sessionStorage.getItem('spa-path');
  
  if (spaPath) {
    console.log("Restoring SPA path:", spaPath);
    sessionStorage.removeItem('spa-path');
    
    try {
      // For GitHub Pages, we need to reconstruct the full path
      const isGitHubPages = window.location.hostname.includes('github.io');
      const repoName = 'AI_Loteria_24-25';
      
      // For GitHub Pages, prefix with repo name
      const fullPath = isGitHubPages 
        ? `/${repoName}/${spaPath}` 
        : `/${spaPath}`;
      
      // Apply the path to the current location
      window.history.replaceState(null, '', fullPath);
    } catch (e) {
      console.error("Failed to restore path:", e);
    }
  }
  
  // Process any legacy redirectPath (for backward compatibility)
  const redirectPath = sessionStorage.getItem('redirectPath');
  if (redirectPath) {
    console.log("Legacy redirect path found:", redirectPath);
    sessionStorage.removeItem('redirectPath');
    
    if (!redirectPath.match(/^https?:\/\//)) {
      try {
        window.history.replaceState(null, null, redirectPath);
      } catch (e) {
        console.error("History API error with legacy path:", e);
      }
    }
  }

  const rootElement = document.getElementById("root");
  if (!rootElement) {
    throw new Error("Root element not found");
  }

  const root = ReactDOM.createRoot(rootElement);
  root.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );

  reportWebVitals();
} catch (error) {
  console.error("Application initialization failed:", error);
  document.body.innerHTML = `<div style="color: red; padding: 20px;">
    <h1>Initialization Error</h1>
    <pre>${error.message}</pre>
    <pre>${error.stack}</pre>
  </div>`;
}
