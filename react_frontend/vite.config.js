import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  base: "/AI_Loteria_24-25/",
  server: {
    watch: {
      usePolling: true,
    },
  },
});
