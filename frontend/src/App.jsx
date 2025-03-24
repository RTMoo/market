import { createRoot } from 'react-dom/client'
import AppRoutes from './routes';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
    return (
        <>
            <ToastContainer />
            <AppRoutes />
        </>
    )
}

createRoot(document.getElementById('root')).render(
    <App />
)
