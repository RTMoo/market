import { useEffect, useState } from "react";
import { getProducts } from "../../../api/product";
import Paginator from "./Paginator";
import ProductCard from "./ProductCard";

const Product = () => {
    const [products, setProducts] = useState([]);
    const [nextPage, setNextPage] = useState(null);
    const [prevPage, setPrevPage] = useState(null);
    const [currentPage, setCurrentPage] = useState(1);
    const [loading, setLoading] = useState(false);

    const fetchProducts = async (page = 1) => {
        setLoading(true);

        const response = await getProducts(page);

        if (response.status === 200) {
            setProducts(response.data.results);
            setNextPage(response.data.next ? page + 1 : null);
            setPrevPage(response.data.previous ? page - 1 : null);
            setCurrentPage(page);
        }
        window.scrollTo({ top: 0, behavior: "smooth" });

        setLoading(false);
    };

    useEffect(() => {
        fetchProducts();
    }, []);

    return (
        <div className="p-4">
            {loading ? (
                <p>Загрузка товаров...</p>
            ) : (
                <>
                    {/* Сетка для карточек товаров */}
                    <div className="grid gap-6 grid-cols-2 sm:grid-cols-3 md:grid-cols-[repeat(auto-fit,minmax(200px,300px))]">
                        {products.map((item) => (
                            <ProductCard key={item.id} item={item}/>
                        ))}
                    </div>


                    {/* Пагинация */}
                    <div className="mt-6 flex justify-center">
                        <Paginator next={nextPage} previous={prevPage} onPageChange={fetchProducts} />
                    </div>

                    <p className="text-center mt-2">Страница: {currentPage}</p>
                </>
            )}
        </div>
    );
};

export default Product;
