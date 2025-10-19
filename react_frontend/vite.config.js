// vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig(() => {
  const isVercel = !!process.env.VERCEL; // Vercel sets this env var
  return {
    plugins: [react()],
    base: isVercel ? "/" : "/SHPE_Tech_Team_24-25/",
    build: { outDir: "dist" },
    resolve: { alias: { "@": path.resolve(__dirname, "./src") } },
  };
});
