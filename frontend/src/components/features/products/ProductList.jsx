import { useNavigate } from "react-router-dom";
import { deleteProduct } from "../../../api/product";
import { VscDiffRemoved, VscEdit } from "react-icons/vsc";
import { useState } from "react";
import ModalUpdateProduct from "./ModalUpdateProduct"

const ProductList = ({ products, setProducts }) => {
    const navigate = useNavigate();
    const [selectedProduct, setSelectedProduct] = useState(null);

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
                <div key={product.id} className="border p-3 my-1 flex justify-between items-center" onClick={() => navigate(`/product/${product.id}`)}>
                    <div className="flex flex-row">
                        <h3 className="mr-5 hover:underline">{product.name}</h3>
                        <p className="mr-5">Цена: {product.price} руб.</p>
                        <p>В наличии: {product.stock} шт.</p>
                    </div>
                    <div className="flex items-center">
                        <VscEdit 
                            className="mr-2 cursor-pointer text-blue-500 hover:text-blue-700"
                            onClick={(e) => {
                                e.stopPropagation();
                                setSelectedProduct(product);
                            }}
                        />
                        <VscDiffRemoved 
                            className="cursor-pointer text-red-500 hover:text-red-700"
                            onClick={(e) => {
                                e.stopPropagation();
                                handleDelete(product.id);
                            }}
                        />
                    </div>
                </div>
            ))}
            {selectedProduct && (
                <ModalUpdateProduct 
                    product={selectedProduct} 
                    setProduct={setSelectedProduct} 
                    setProducts={setProducts}
                    onClose={() => setSelectedProduct(null)}
                />
            )}
        </div>
    );
};

export default ProductList;
