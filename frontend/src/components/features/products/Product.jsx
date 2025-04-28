import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";  // для управления URL
import { getProducts } from "../../../api/product";
import Paginator from "./Paginator";
import ProductCard from "./ProductCard";
import Filter from "./Filter";

const Product = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(false);
    const [count, setCount] = useState(0);
    const pageSize = 24;
    const location = useLocation();
    const navigate = useNavigate();

    // Получаем текущую страницу из query параметров
    const currentPage = parseInt(new URLSearchParams(location.search).get("page") || "1");
    const totalPages = Math.ceil(count / pageSize);

    const next = currentPage < totalPages ? currentPage + 1 : null;
    const previous = currentPage > 1 ? currentPage - 1 : null;

    // Запрос товаров с пагинацией
    const fetchProducts = async (page = 1, filters = {}) => {
        setLoading(true);

        // Формируем параметры запроса на основе URL и фильтров
        const queryParams = new URLSearchParams(location.search);
        queryParams.set("page", page);

        // Добавляем фильтры в параметры запроса
        Object.keys(filters).forEach((key) => {
            queryParams.set(key, filters[key]);
        });

        // Запрашиваем данные с пагинацией
        const queryObject = Object.fromEntries(queryParams);
        const response = await getProducts(queryObject);

        if (response.status === 200) {
            setProducts(response.data.results);
            setCount(response.data.count);
        }

        setLoading(false);
        window.scrollTo({ top: 0, behavior: "smooth" });
    };

    // Обработчик изменения страницы
    const handlePageChange = (page) => {
        const queryParams = new URLSearchParams(location.search);
        queryParams.set("page", page);

        // Навигация по измененному URL
        navigate({
            pathname: location.pathname,
            search: queryParams.toString()  // передаем параметры фильтров и номер страницы
        });
    };

    // Обработчик изменения фильтров
    const handleFilterChange = (newFilters) => {
        const queryParams = new URLSearchParams(location.search);
        queryParams.set("page", 1);  // сбрасываем страницу на 1
    
        // Обновляем фильтры в URL, только если они имеют значение
        Object.keys(newFilters).forEach((key) => {
            if (newFilters[key] !== undefined && newFilters[key] !== null && newFilters[key] !== "") {
                queryParams.set(key, newFilters[key]);
            } else {
                queryParams.delete(key);  // удаляем фильтры, если они не заданы
            }
        });
    
        // Навигация с обновленными фильтрами и сброшенной страницей
        navigate({
            pathname: location.pathname,
            search: queryParams.toString()  // передаем фильтры и сбрасываем страницу на 1
        });
    
        // Перезапрос товаров с новыми фильтрами
        fetchProducts(1, newFilters);
    };
    

    useEffect(() => {
        fetchProducts(currentPage, new URLSearchParams(location.search));
    }, [location.search]); // Запрос данных при изменении параметров в URL

    return (
        <div className="p-4 flex">
            <div className="w-full lg:w-[80%]">
                {loading ? (
                    <p>Загрузка товаров...</p>
                ) : products.length === 0 ? (
                    <p>Товары не найдены</p>
                ) : (
                    <>
                        <div className="grid gap-6 grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
                            {products.map((item) => (
                                <ProductCard key={item.id} item={item} />
                            ))}
                        </div>

                        <div className="mt-6 flex justify-center">
                            <Paginator
                                next={next}
                                previous={previous}
                                current={currentPage}
                                total={totalPages}
                                onPageChange={handlePageChange}
                            />
                        </div>
                    </>
                )}
            </div>

            <div className="hidden lg:block lg:w-[20%] sticky top-4 h-fit ml-4">
                <Filter setProducts={setProducts} onFilterChange={handleFilterChange} />
            </div>
        </div>
    );
};

export default Product;
