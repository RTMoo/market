import { useEffect, useState } from "react";
import { getProducts } from "../../../api/product";
import Paginator from "./Paginator";
import ProductCard from "./ProductCard";
import Filter from "./Filter";

const Product = () => {
    const [products, setProducts] = useState([]);
    const [nextPage, setNextPage] = useState(null);
    const [prevPage, setPrevPage] = useState(null);
    const [currentPage, setCurrentPage] = useState(1);
    const [count, setCount] = useState(0);
    const [loading, setLoading] = useState(false);

    const pageSize = 24; // Укажи здесь реальный page_size с бэка
    const totalPages = Math.ceil(count / pageSize);

    const fetchProducts = async (page = 1) => {
        setLoading(true);

        const response = await getProducts({ page });

        if (response.status === 200) {
            setProducts(response.data.results);
            setNextPage(response.data.next ? page + 1 : null);
            setPrevPage(response.data.previous ? page - 1 : null);
            setCurrentPage(page);
            setCount(response.data.count);
        }

        window.scrollTo({ top: 0, behavior: "smooth" });
        setLoading(false);
    };

    useEffect(() => {
        fetchProducts();
    }, []);

    return (
        <div className="p-4 flex">
            <div className="w-full lg:w-[80%]">
                {loading ? (
                    <p>Загрузка товаров...</p>
                ) : (
                    <>
                        <div className="grid gap-6 grid-cols-2 md:grid-cols-3 lg:grid-cols-5">
                            {products.map((item) => (
                                <ProductCard key={item.id} item={item} />
                            ))}
                        </div>

                        <div className="mt-6 flex justify-center">
                            <Paginator
                                next={nextPage}
                                previous={prevPage}
                                current={currentPage}
                                total={totalPages}
                                onPageChange={fetchProducts}
                            />
                        </div>
                    </>
                )}
            </div>

            {/* Фильтр справа */}
            <div className="hidden lg:block lg:w-[20%] sticky top-4 h-fit ml-4">
                <Filter setProducts={setProducts} />
            </div>
        </div>
    );
};

export default Product;
