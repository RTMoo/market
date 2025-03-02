import React, { useEffect, useState } from "react";
import { getProfile, updateProfile } from "../api/profile";

const Profile = () => {
    const [profile, setProfile] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [isUpdated, setIsUpdated] = useState(false);
    const [formData, setFormData] = useState({
        first_name: "",
        last_name: "",
        email: "",
        phone_number: "",
    });

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const data = await getProfile();
                setProfile(data);
                setFormData({
                    first_name: data.first_name || "",
                    last_name: data.last_name || "",
                    email: data.email,
                    phone_number: data.phone_number || "",
                });
            } catch (error) {
                setError(error.detail || "Ошибка загрузки профиля");
            } finally {
                setLoading(false);
            }
        };

        fetchProfile();
    }, []);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null); // Очистка ошибки перед запросом

        const { email, ...updatedData } = formData;

        try {
            const updatedProfile = await updateProfile(updatedData);
            setProfile(updatedProfile);
            setIsUpdated(true);

            // Скрытие сообщения через 3 секунды
            setTimeout(() => setIsUpdated(false), 3000);
        } catch (error) {
            setError(error.detail || "Ошибка обновления профиля");
        }
    };

    if (loading) return <div className="text-center text-lg mt-10">Загрузка...</div>;
    if (error) return <div className="text-center text-red-500 mt-10">Ошибка: {error}</div>;

    return (
        <div className="flex flex-col w-full relative">
            {/* Уведомление об обновлении */}
            {isUpdated && (
                <div className="absolute top-5 left-1/2 -translate-x-1/2 bg-green-500 text-white px-4 py-2 rounded-lg shadow-md">
                    Профиль обновлен!
                </div>
            )}

            <div className="w-full bg-white p-6 mt-10 border-gray-200">
                <h2 className="text-2xl font-semibold text-center mb-4">Профиль</h2>
                <form onSubmit={handleSubmit} className="space-y-4">
                    {/* Имя и фамилия */}
                    <div className="flex gap-4">
                        <div className="w-1/2">
                            <label className="block text-gray-600">Имя</label>
                            <input
                                type="text"
                                name="first_name"
                                value={formData.first_name}
                                onChange={handleChange}
                                className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div className="w-1/2">
                            <label className="block text-gray-600">Фамилия</label>
                            <input
                                type="text"
                                name="last_name"
                                value={formData.last_name}
                                onChange={handleChange}
                                className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                    </div>

                    {/* Телефон и Email */}
                    <div className="flex gap-4">
                        <div className="w-1/2">
                            <label className="block text-gray-600">Номер телефона</label>
                            <input
                                type="text"
                                name="phone_number" // Исправлено
                                value={formData.phone_number}
                                onChange={handleChange}
                                className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div className="w-1/2">
                            <label className="block text-gray-600">Email</label>
                            <input
                                type="email"
                                name="email"
                                value={formData.email}
                                disabled
                                className="w-full p-2 border border-gray-300 rounded-lg bg-gray-100 text-gray-500"
                            />
                        </div>
                    </div>

                    {/* Кнопка */}
                    <div className="flex justify-end">
                        <button
                            type="submit"
                            className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition"
                        >
                            Сохранить
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default Profile;
