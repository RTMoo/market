import React, { useEffect, useState } from "react";
import { getProfile, updateProfile } from "../api/profile";
import { getUserProducts } from "../api/product";
import FormInput from "../components/commons/FormInput";
import ProductList from "../components/products/ProductList";

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
    const [userProducts, setUserProducts] = useState([])
    const fetchProfile = async () => {
        try {
            const response = await getProfile();
            if (response.status === 200) {
                const data = response.data
                setProfile(data);
                setFormData({
                    first_name: data.first_name || "",
                    last_name: data.last_name || "",
                    email: data.email,
                    phone_number: data.phone_number || "",
                });
            } else {
                console.log(response.data, response.status);
            }
            
        } catch (error) {
            setError(error.detail || "Ошибка загрузки профиля");
        } finally {
            setLoading(false);
        }
    };

    const fetchUserProducts = async () => {
        try {
            const response = await getUserProducts();
            if(response.status === 200) {
                setUserProducts(response.data)
            } else {
                console.log(response.data, response.status)
            }
        } catch (error) {
            console.log(error)
        }
    }

    useEffect(() => {
        fetchProfile();
        fetchUserProducts();
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
                <div>
                    <h2 className="text-2xl font-semibold text-center mb-4">Профиль</h2>
                    <form onSubmit={handleSubmit} className="space-y-4 mb-5">

                        <div className="flex gap-4">
                            <FormInput label={'Имя'} type={'text'} name={'first_name'} value={formData.first_name} onChange={handleChange} />
                            <FormInput label={'Фамилия'} type={'text'} name={'last_name'} value={formData.last_name} onChange={handleChange} />
                        </div>

                        <div className="flex gap-4">
                            <FormInput label={'Номер'} type={'text'} name={'phone_number'} value={formData.phone_number} onChange={handleChange} />
                            <FormInput label={'Почта'} type={'text'} value={formData.email} disabled={true} />
                        </div>

                        <div className="flex justify-end">
                            <button
                                type="submit"
                                className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition"
                            >
                                Сохранить
                            </button>
                        </div>
                    </form>
                    <h2 className="text-2xl font-semibold text-center mb-4">Ваши продукты</h2>
                    <ProductList products={userProducts} />
                </div>
                <div className="flex flex-col">
                    
                </div>
            </div>
        </div>
    );
};

export default Profile;
