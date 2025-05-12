import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [react(), tailwindcss()],
  base: '/', // Обязательно для корректной работы маршрутов в Nginx
  build: {
    outDir: 'dist', // Стандартная папка, совпадает с Dockerfile
    emptyOutDir: true
  }
})
