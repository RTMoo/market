import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/accounts/LoginPage';
import RegisterPage from './pages/accounts/RegisterPage';
import Home from './pages/Home';
import Layout from './components/layouts/Layout';
import Profile from './pages/profiles/Profile';
import ProductPage from './pages/products/ProductPage';
import CartsPage from './pages/carts/CartsPage';
import OrdersPage from './pages/orders/OrdersPage';
import OrderDetails from './pages/orders/OrderDetails';
import ConfirmCode from './pages/accounts/ConfirmCode';

function AppRoutes() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path='/login' element={<LoginPage />} />
                <Route path='/register' element={<RegisterPage />} />
                <Route path='/confirm_code' element={<ConfirmCode />} />
                <Route path='/profile' element={
                    <Layout>
                        <Profile />
                    </Layout>
                } />
                <Route path='/product/:id' element={
                    <Layout>
                        <ProductPage />
                    </Layout>
                } />
                <Route path='/cart' element={
                    <Layout>
                        <CartsPage />
                    </Layout>
                } />
                <Route path='/order' element={
                    <Layout>
                        <OrdersPage />
                    </Layout>
                } />
                <Route path='/order/:id' element={ 
                    <Layout>
                        <OrderDetails />
                    </Layout>   
                } />
            </Routes>
        </Router>
    );
}

export default AppRoutes;