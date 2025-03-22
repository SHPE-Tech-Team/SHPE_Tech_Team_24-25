// import { defineConfig } from "vite";
// import react from "@vitejs/plugin-react";
// import path from "path"; 

// export default defineConfig({
//   plugins: [react()],
//   base: "/AI_Loteria_24-25/",
//   build: {
//     outDir: "dist",
//   },
//   resolve: {
//     alias: {
//       "@": path.resolve(__dirname, "./src"),
//     },
//   },
//   server: {
//     watch: {
//       usePolling: true,
//     },
//     open: "/AI_Loteria_24-25/",
//   },
// });



import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig(({ mode }) => {
  const isProduction = mode === "production";

  return {
    plugins: [react()],
    base: isProduction ? "/AI_Loteria_24-25/" : "/",
    build: {
      outDir: "dist",
    },
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },
    server: {
      port: 3000,
      open: true,
      watch: {
        usePolling: true,
      },
    },
  };
});