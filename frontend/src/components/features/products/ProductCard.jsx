import { useNavigate } from "react-router-dom";


const ProductCard = ({ item, isCart=false }) => {
    const navigate = useNavigate()

    return (
        <div className="border rounded-xl p-4 shadow-md bg-white h-60 flex flex-col justify-between overflow-hidden"
            onClick={
                () => {
                    navigate(`/product/${item.id}`)
                }
            }>
            <div>
                <h2 className="text-xl font-bold text-gray-800">
                    {isCart ? item.product_name : item.title}
                </h2>
            </div>
            <div className="">
                <p className="text-lg font-semibold mt-2">
                    Цена: <span className="text-green-500">
                        {isCart ? item.product_price : item.price}₽
                    </span>
                </p>
                <p className="text-sm text-gray-500">
                    {isCart ? "В корзине:" : "Остаток:"}
                    {isCart ? item.quantity : item.stock}</p>
            </div>
        </div>
    );
};

export default ProductCard;
