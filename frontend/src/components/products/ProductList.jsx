import { useNavigate } from "react-router-dom";

const ProductList = ({ products }) => {
    const navigate = useNavigate()

    return (
        <div>
            {products.map((product) => (
                <div key={product.id} className="border p-3 my-1" onClick={
                    () => {
                        navigate(`/product/${product.id}`)
                    }
                }>
                    <h3>{product.title}</h3>
                    <p>Цена: {product.price} руб.</p>
                    <p>В наличии: {product.stock} шт.</p>
                </div>
            ))}
        </div>
    );
};

export default ProductList;