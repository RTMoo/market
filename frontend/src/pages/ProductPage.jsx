import { useState, useEffect } from 'react';
import { getProductInfo, getCategoryInfo } from '../api/product';
import { useParams } from 'react-router-dom';

const ProductPage = () => {
    const { id } = useParams();
    const [product, setProduct] = useState(null);

    useEffect(() => {
        const fetchProductInfo = async () => {
            try {
                const response = await getProductInfo(id);
                if (response.status === 200) {
                    const data = response.data;
                    const category = await getCategoryInfo(data.category);
                    data.category = category.status === 200 ? category.data.name : "Не указано";
                    setProduct(data);
                }
            } catch (error) {
                console.log(error);
            }
        };
        fetchProductInfo();
    }, [id]);

    if (!product) return <div className="text-center py-10">Загрузка...</div>;

    return (
        <section className="p-6">
            <div className="grid md:grid-cols-2 gap-10">
                <div className="w-full aspect-[4/3] overflow-hidden shadow-xl">
                    <img 
                    src={product.image ? product.image : "../../assets/img/image-not-available.png"}
                    alt={product.title} 
                    className="w-full h-full object-cover"/>
                </div>                
                <div>
                    <p className="text-indigo-600 mb-2">Категория: {product.category}</p>
                    <h2 className="text-3xl font-bold mb-2">{product.title}</h2>
                    <h6 className="text-2xl font-semibold mb-4">${product.price}</h6>
                    <p className="text-gray-500 mb-4">{product.description}</p>
                    <button className="w-full py-3 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700">Купить</button>
                </div>
            </div>
        </section>
    );
};

export default ProductPage;