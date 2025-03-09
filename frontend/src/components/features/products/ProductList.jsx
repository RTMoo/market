import { useNavigate } from "react-router-dom";
import { deleteProduct } from "../../../api/product";
import { VscDiffRemoved } from "react-icons/vsc";

const ProductList = ({ products, setProducts }) => {
    const navigate = useNavigate();

    const handleDelete = async (id) => {
        try {
            const response = await deleteProduct(id);
            if (response.status === 204) {
                setProducts(products.filter(product => product.id !== id));
            }
        } catch (error) {
            console.error("Ошибка удаления:", error);
        }
    };

    return (
        <div>
            {products.map((product) => (
                <div key={product.id} className="border p-3 my-1 flex justify-between" onClick={() => navigate(`/product/${product.id}`)}>
                    <div className="flex flex-row">
                        <h3 className="mr-5">{product.title}</h3>
                        <p className="mr-5">Цена: {product.price} руб.</p>
                        <p>В наличии: {product.stock} шт.</p>
                    </div>
                    <VscDiffRemoved onClick={(e) => {
                        e.stopPropagation(); // Чтобы клик не срабатывал на родительский div
                        handleDelete(product.id);
                    }} />
                </div>
            ))}
        </div>
    );
};

export default ProductList;