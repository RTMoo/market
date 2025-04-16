import { getCategories, getProducts } from "../../api/product";
import { useProducts } from "../contexts/ProductContext";
import { useEffect, useState } from "react";

const Sidebar = ({ isOpen, toggleSidebar }) => {
    const [categories, setCategories] = useState([])
    const { setProducts } = useProducts()

    const fetchCategories = async () => {
        try {
            const response = await getCategories();
            if (response.status === 200) {
                setCategories(response.data); // предполагаем, что response.data - это массив категорий
            }
        } catch (error) {
            console.error("Ошибка при загрузке категорий", error);
        }
    };

    const handleCategoryClick = async (id) => {
        const response = await getProducts({ category: id });
        if (response.status === 200) {
            setProducts(response.data.results);
            toggleSidebar()
        }
    };

    useEffect(() => {
        if (isOpen) {
            document.body.classList.add("overflow-hidden");
        } else {
            document.body.classList.remove("overflow-hidden");
        }

        fetchCategories();

        return () => {
            document.body.classList.remove("overflow-hidden");
        };
    }, [isOpen]);

    return (
        <>
            {/* Затемнение фона */}
            <div
                className={`fixed inset-0 bg-[#00000020] z-40 transition-opacity ${isOpen ? "opacity-100" : "opacity-0 pointer-events-none"}`}
                onClick={toggleSidebar}
            />

            {/* Сайдбар */}
            <aside
                className={`fixed left-0 top-20 w-64 h-screen bg-white shadow-lg transition-transform duration-300 z-99 ${isOpen ? "translate-x-0" : "-translate-x-full"}`}
            >
                <ul className="p-4 overflow-y-auto h-full">
                    {categories.length > 0 ? (
                        categories.map((category) => (
                            <li key={category.id} className="p-2 hover:bg-gray-200 hover: rounded-xl text-lg hover:cursor-pointer" onClick={
                                () => handleCategoryClick(category.id)
                            }>
                                {category.name} {/* Здесь используйте поля объекта, например, category.name */}
                            </li>
                        ))
                    ) : (
                        <li className="p-2">Загружается...</li>
                    )}
                </ul>
            </aside>
        </>
    );
};

export default Sidebar;
