import { createRoot } from 'react-dom/client'
import AppRoutes from './routes';

function App() {
  return (
      <div className="app">
          <AppRoutes />
      </div>
  )
}

createRoot(document.getElementById('root')).render(
  <App />
)
