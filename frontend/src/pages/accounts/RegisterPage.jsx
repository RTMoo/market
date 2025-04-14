import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'
import { register } from '../../api/auth';

const RegisterPage = () => {
    const navigate = useNavigate()
    let [email, setEmail] = useState('')
    let [password, setPassword] = useState('')
    let [password2, setPassword2] = useState('')

    const handleRegister = async (e) => {
        e.preventDefault();
        try {
            const response = await register(email, password, password2);
            if (response.status === 201) {
                localStorage.setItem("confirmEmail", email)
                navigate('/confirm_code');
            };
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <div className="w-full min-h-screen flex items-center justify-center bg-gray-100">
            <form className="bg-white p-8 rounded-2xl shadow-md w-96 space-y-4">
                <h2 className="text-xl font-bold text-center">Регистрация</h2>

                <div>
                    <label htmlFor="email" className="block text-gray-600 text-sm font-medium">Email</label>
                    <input
                        type="text"
                        id="email"
                        className="mt-1 w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none"
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>

                <div>
                    <label htmlFor="password" className="block text-gray-600 text-sm font-medium">Пароль</label>
                    <input
                        type="password"
                        id="password"
                        className="mt-1 w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none"
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>

                <div>
                    <label htmlFor="password2" className="block text-gray-600 text-sm font-medium">Повторите пароль</label>
                    <input
                        type="password"
                        id="password2"
                        className="mt-1 w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none"
                        onChange={(e) => setPassword2(e.target.value)}
                    />
                </div>

                <button
                    type="submit"
                    className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition duration-200"
                    onClick={handleRegister}
                >
                    Регистрация
                </button>
            </form>
        </div>

    );
}

export default RegisterPage;
