// eslint-env node
import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import path from 'path'

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd())

  return {
    plugins: [react(), tailwindcss()],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, './src'),
      },
    },
    server: {
      host: true,
      allowedHosts: [
        'localhost',
        '127.0.0.1'
      ],
      proxy: env.VITE_BACKEND_URL
        ? {
            '/api': {
              target: env.VITE_BACKEND_URL,
              changeOrigin: true,
            },
          }
        : undefined,
    },
  }
})
