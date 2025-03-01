import React, { useEffect, useState } from "react";
import { VscThreeBars } from "react-icons/vsc";
import { logout } from "../../api/auth";
import { useNavigate } from "react-router-dom";

const Header = ({ toggleSidebar }) => {
    const navigate = useNavigate()
    const [userEmail, setUserEmail] = useState(null);

    useEffect(() => {
        setUserEmail(localStorage.getItem('email'))
    }, []);

    const handleLogout = async () => {
        try {
            await logout()
            localStorage.removeItem('email')
            setUserEmail(null)
            navigate('/')
        } catch (error) {
            console.log(error)
        }
    };

    return (
        <header className="sticky top-0 left-0 w-full h-16 bg-white shadow-md px-6 z-100">
            <div className="flex justify-between items-center h-full">
                <div className="flex flex-row items-center">
                    <button className="p-2 rounded-md hover:bg-gray-200 transition" onClick={toggleSidebar}>
                        <VscThreeBars size={30} />
                    </button>
                    <h1 className="text-2xl font-bold p-2">
                        <a href="/">
                            eMarket
                        </a>
                    </h1>
                </div>

                <nav className="">
                    {userEmail ? (
                        <div className="flex items-center gap-4">
                            <span className="text-gray-700">{userEmail}</span>
                            <button 
                                onClick={handleLogout} 
                                className="bg-red-500 text-white px-4 py-1 rounded-lg hover:bg-red-600 transition"
                            >
                                Выйти
                            </button>
                        </div>
                    ) : (
                        <>
                            <a href="/login" className="hover:underline hover:text-[#00000090]">Login</a>
                            <span> / </span>
                            <a href="/register" className="hover:underline hover:text-[#00000090]">Register</a>
                        </>
                    )}
                </nav>
            </div>
        </header>
    );
};

export default Header;
