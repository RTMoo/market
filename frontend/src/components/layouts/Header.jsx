import React, { useEffect, useState, useRef } from "react";
import { VscThreeBars, VscAccount } from "react-icons/vsc";
import { logout } from "../../api/auth";
import { useNavigate } from "react-router-dom";

const Header = ({ toggleSidebar }) => {
    const navigate = useNavigate();
    const [userEmail, setUserEmail] = useState(null);
    const [menuOpen, setMenuOpen] = useState(false);
    const menuRef = useRef(null);

    useEffect(() => {
        setUserEmail(localStorage.getItem("email"));
    }, []);

    const handleLogout = async () => {
        try {
            await logout();
            localStorage.removeItem("email");
            setUserEmail(null);
            navigate("/");
        } catch (error) {
            console.log(error);
        }
    };

    // Закрываем меню при клике вне него
    useEffect(() => {
        const handleClickOutside = (event) => {
            if (menuRef.current && !menuRef.current.contains(event.target)) {
                setMenuOpen(false);
            }
        };
        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    }, []);

    return (
        <header className="sticky top-0 left-0 w-full h-16 bg-white shadow-md px-6 z-50">
            <div className="flex justify-between items-center h-full">
                <div className="flex flex-row items-center">
                    <button className="p-2 rounded-md hover:bg-gray-200 transition" onClick={toggleSidebar}>
                        <VscThreeBars size={30} />
                    </button>
                    <h1 className="text-2xl font-bold p-2">
                        <a href="/">eMarket</a>
                    </h1>
                </div>

                <nav className="relative">
                    {userEmail ? (
                        <div className="relative flex items-center">
                            <button onClick={() => setMenuOpen(!menuOpen)} className="p-2 rounded-full hover:bg-gray-200 transition">
                                <VscAccount size={30} />
                            </button>

                            {menuOpen && (
                                <div ref={menuRef} className="absolute right-0 top-14 w-36 bg-white shadow-lg rounded-lg py-2 z-50">
                                    <button
                                        onClick={() => navigate("/profile")}
                                        className="block w-full text-left px-4 py-2 hover:bg-gray-100"
                                    >
                                        Профиль
                                    </button>
                                    <button
                                        onClick={handleLogout}
                                        className="block w-full text-left px-4 py-2 text-red-500 hover:bg-gray-100"
                                    >
                                        Выйти
                                    </button>
                                </div>
                            )}
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
