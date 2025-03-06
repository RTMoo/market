import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import Home from './pages/Home';
import Layout from './components/layouts/Layout';
import Profile from './pages/Profile';
import CreateProductPage from './pages/CreateProductPage';

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
                <Route path='/create-product' element={
                    <Layout>
                        <CreateProductPage />
                    </Layout>
                } />
            </Routes>
        </Router>
    );
}

export default AppRoutes;