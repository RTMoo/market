import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import Home from './pages/Home';
import Layout from './components/layouts/Layout';
import Profile from './pages/Profile';
import ProductPage from './pages/ProductPage';
import CartsPage from './pages/CartsPage';
import OrdersPage from './pages/OrdersPage';

function AppRoutes() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path='/login' element={<LoginPage />} />
                <Route path='/register' element={<RegisterPage />} />
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
            </Routes>
        </Router>
    );
}

export default AppRoutes;