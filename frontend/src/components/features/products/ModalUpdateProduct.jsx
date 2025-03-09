import React, { useState, useEffect } from "react";
import FormInput from "../../commons/FormInput";
import { updateProduct, getCategories } from "../../../api/product";
import { useNavigate } from 'react-router-dom';


const ModalUpdateProduct = ({ product, onClose }) => {
    const navigate = useNavigate();
    const [categories, setCategories] = useState([]);
    const [formData, setFormData] = useState({ ...product });

    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const response = await getCategories();
                if (response.status === 200) {
                    setCategories(response.data);
                }
            } catch (error) {
                console.error("Ошибка при загрузке категорий", error);
            }
        };
        fetchCategories();
    }, []);

    const handleChange = (e) => {
        const { name, value, type } = e.target;
        setFormData({
            ...formData,
            [name]: name === "category" ? Number(value) || "" : type === "number" ? Number(value) || "" : value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await updateProduct(product.id, formData);
            if (response.status === 200) {
                navigate(0)
            } else {
                console.log("Ошибка при обновлении продукта", response.data);
            }
        } catch (error) {
            console.error("Ошибка обновления продукта", error);
        }
    };

    return (
        <div className="fixed inset-0 flex items-center justify-center bg-[#00000060] z-50" onClick={onClose}>
            <div className="bg-white p-6 rounded-lg shadow-lg w-120 relative" onClick={(e) => e.stopPropagation()}>
                <button className="absolute top-2 right-2 text-gray-500 hover:text-gray-700" onClick={onClose}>✖</button>
                <h2 className="text-2xl font-semibold text-center mb-4">Редактировать продукт</h2>
                <form onSubmit={handleSubmit}>
                    <FormInput label="Заголовок" name="title" value={formData.title} onChange={handleChange} type="text" />
                    <FormInput label="Описание" name="description" value={formData.description} onChange={handleChange} isTextArea />
                    <div className="w-full">
                        <label className="block text-gray-600">Категория</label>
                        <select
                            name="category"
                            value={formData.category}
                            onChange={handleChange}
                            className="w-full p-2 border border-gray-300 rounded-lg focus:ring-blue-500"
                        >
                            <option value="">Выберите категорию</option>
                            {categories.map((cat) => (
                                <option key={cat.id} value={cat.id}>{cat.name}</option>
                            ))}
                        </select>
                    </div>
                    <FormInput label="Цена" name="price" value={formData.price} onChange={handleChange} type="number" />
                    <FormInput label="В наличии" name="stock" value={formData.stock} onChange={handleChange} type="number" />
                    <div className="flex justify-end mt-4">
                        <button type="submit" className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition">
                            Сохранить
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default ModalUpdateProduct;
