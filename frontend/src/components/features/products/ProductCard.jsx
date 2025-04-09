import { useNavigate } from "react-router-dom";


const ProductCard = ({ item }) => {
    const navigate = useNavigate()

    return (
        <div className="border rounded-xl p-4 shadow-md bg-white h-60 flex flex-col justify-between overflow-hidden hover:cursor-pointer"
            onClick={
                () => {
                    navigate(`/product/${item.id}`)
                }
            }>
            <div>
                <span className="text-xl font-bold text-gray-800 hover:underline">
                    {item.name}
                </span>
            </div>
            <div className="">
                <p className="text-lg font-semibold mt-2">
                    Цена: <span className="text-green-500">
                        {item.price}₽
                    </span>
                </p>
                <p className="text-lg font-semibold mt-2">
                    Категория: <span className="text-blue-300">
                        {item.category_name}
                    </span>
                </p>
                <p className="text-sm text-gray-500">
                    Остаток:
                    {item.stock}
                </p>
            </div>
        </div>
    );
};

export default ProductCard;
