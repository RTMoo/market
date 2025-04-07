import { useState } from 'react';
import { updateCartItem, deleteCartItem } from "../../../api/cart";
import { IoIosRemoveCircleOutline, IoIosAddCircleOutline, IoMdTrash } from "react-icons/io";
import { FaRegHeart } from "react-icons/fa6";
import { toast } from "react-toastify";


const CartItemCard = ({ item, setCartItems }) => {
    const [quantity, setQuantity] = useState(item.quantity)

    const handleUpdateCart = async (quantity) => {
        try {
            const response = await updateCartItem(item.id, quantity);
            if (response.status === 200) {
                setQuantity(quantity)
            }
        } catch (error) {
            toast.error(error.detail)
        }
        
    }

    const handleDeleteCart = async () => {
        const response = await deleteCartItem(item.id);
        if (response.status === 204) {
            setCartItems((prevItems) => prevItems.filter((i) => i.id !== item.id));
        }
    }

    return (
        <div className="flex gap-4 bg-white px-4 py-6 rounded-md shadow-[0_2px_12px_-3px_rgba(61,63,68,0.3)]">
            <div className="flex gap-4">
                <div className="w-28 h-28 max-sm:w-24 max-sm:h-24 shrink-0">
                    <img
                        src={item.image ? item.image : "../../assets/img/image-not-available.png"}
                        alt={item.product_name}
                        className="w-full h-full object-contain" />
                </div>

                <div className="flex flex-col gap-4">
                    <div>
                        <h3 className="text-sm sm:text-base font-semibold text-slate-900">{item.product_name}</h3>
                    </div>

                    <div className="mt-auto flex items-center gap-3">
                        <IoIosRemoveCircleOutline size={30} className='hover:text-gray-500'
                            onClick={() => handleUpdateCart(quantity - 1)}
                        />
                        <span className="font-semibold text-sm leading-[18px]">{quantity}</span>
                        <IoIosAddCircleOutline size={30} className='hover:text-gray-500'
                            onClick={() => handleUpdateCart(quantity + 1)}
                        />
                    </div>
                </div>
            </div>
            <div className="ml-auto flex flex-col">
                <div className="flex items-start gap-4 justify-end">
                    <FaRegHeart size={20} className="cursor-pointer fill-slate-400 hover:fill-pink-600 inline-block" />
                    <IoMdTrash size={20} className="cursor-pointer fill-slate-400 hover:fill-pink-600 inline-block"
                        onClick={handleDeleteCart} />
                </div>
                <h3 className="text-sm sm:text-base font-semibold text-slate-900 mt-auto">{item.product_price}₽</h3>
            </div>
        </div>
    );
}

export default CartItemCard;
