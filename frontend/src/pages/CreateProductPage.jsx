import { useState, useEffect } from 'react';
import FormInput from '../components/commons/FormInput';
import { createProduct, getCategories } from '../api/product';
import { useNavigate } from 'react-router-dom';

const CreateProductPage = () => {
    const navigate = useNavigate();
    const [categories, setCategories] = useState([]);
    const [formData, setFormData] = useState({
        title: "",
        description: "",
        category: "",
        price: "",
        stock: "",
    });

    // Получение списка категорий
    const fetchCategories = async () => {
        try {
            const response = await getCategories();
            if (response.status === 200) {
                setCategories(response.data);
            } else {
                console.error("Ошибка при получении категорий:", response.data);
            }
        } catch (error) {
            console.error("Ошибка сети:", error);
        }
    };

    useEffect(() => {
        fetchCategories();
    }, []);

    // Обработчик изменений в форме
    const handleChange = (e) => {
        const { name, value, type } = e.target;
        setFormData({
            ...formData,
            [name]: name === "category" ? Number(value) || "" : type === "number" ? Number(value) || "" : value,
        });
    };

    // Обработчик отправки формы
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            console.log(formData)
            const response = await createProduct(formData);
            if (response.status === 201) {
                navigate('/profile');
            } else {
                console.log(response.data);
            }
        } catch (error) {
            console.error("Ошибка создания продукта:", error);
        }
    };

    return (
        <div className='px-6 mt-10'>
            <h2 className='text-2xl font-semibold text-center mb-4'>Создать продукт</h2>
            <form onSubmit={handleSubmit}>
                <FormInput label="Заголовок" name="title" value={formData.title} onChange={handleChange} type="text" />
                <FormInput label="Описание" name="description" value={formData.description} onChange={handleChange} isTextArea />

                {/* Поле выбора категории */}
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
                            <option key={cat.id} value={cat.id}>
                                {cat.name}
                            </option>
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
    );
};

export default CreateProductPage;
