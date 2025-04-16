import React, { useEffect, useState } from 'react';
import { IoFilterSharp } from "react-icons/io5";
import { getCategories, getProducts } from '../../../api/product';

const Filter = ({ setProducts }) => {
    const [priceMin, setPriceMin] = useState('');
    const [priceMax, setPriceMax] = useState('');
    const [categories, setCategories] = useState([]);
    const [selectedCategories, setSelectedCategories] = useState([]);

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

    const handleCategoryChange = (e) => {
        const value = e.target.value;
        setSelectedCategories(prev =>
            prev.includes(value)
                ? prev.filter(id => id !== value)
                : [...prev, value]
        );
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const query = {
            price_min: priceMin || undefined,
            price_max: priceMax || undefined,
            category: selectedCategories.length ? selectedCategories : undefined
        };

        try {
            const response = await getProducts(query);
            if (response.status === 200) {
                setProducts(response.data.results);
            }
        } catch (error) {
            console.error("Ошибка при загрузке товаров", error);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="w-full p-4 border rounded-lg shadow-sm bg-white space-y-4">
            <div className="flex items-center space-x-2 text-lg font-semibold">
                <IoFilterSharp />
                <span>Фильтры</span>
            </div>

            <div className="flex space-x-4">
                <input
                    type="number"
                    value={priceMin}
                    onChange={(e) => setPriceMin(e.target.value)}
                    placeholder="Мин. цена"
                    className="w-full border px-2 py-1 rounded"
                    min={0}
                />
                <input
                    type="number"
                    value={priceMax}
                    onChange={(e) => setPriceMax(e.target.value)}
                    placeholder="Макс. цена"
                    className="w-full border px-2 py-1 rounded"
                    min={0}
                />
            </div>

            <div className="space-y-2">
                <div className="text-sm font-medium">Категории</div>
                {categories.map(category => (
                    <label key={category.id} className="flex items-center space-x-2">
                        <input
                            type="checkbox"
                            value={category.id}
                            checked={selectedCategories.includes(String(category.id))}
                            onChange={handleCategoryChange}
                        />
                        <span>{category.name}</span>
                    </label>
                ))}
            </div>

            <button
                type="submit"
                className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
            >
                Применить фильтры
            </button>
        </form>
    );
};

export default Filter;
