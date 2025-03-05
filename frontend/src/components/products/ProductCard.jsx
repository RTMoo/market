const ProductCard = ({ product }) => {
    return (
        <div className="border rounded-xl p-4 shadow-md bg-white h-60 flex flex-col justify-between">
            <div>
                <h2 className="text-xl font-bold text-gray-800">{product.title}</h2>
                <p className="text-gray-600">{product.description}</p>
            </div>
            <div className="">
                <p className="text-lg font-semibold mt-2">
                    Цена: <span className="text-green-500">{product.price}₽</span>
                </p>
                <p className="text-sm text-gray-500">Остаток: {product.stock}</p>
            </div>
        </div>
    );
};

export default ProductCard;
