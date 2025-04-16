import { createRoot } from 'react-dom/client'
import AppRoutes from './routes';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { ProductsProvider } from './components/contexts/ProductContext';

function App() {
    return (
        <>
            <ToastContainer />
            <AppRoutes />
        </>
    )
}

createRoot(document.getElementById('root')).render(
    <ProductsProvider>
        <App />
    </ProductsProvider>
)
