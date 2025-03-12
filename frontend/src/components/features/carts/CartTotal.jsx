import React from 'react';
import { clearCart } from '../../../api/cart';


const CartTotal = ({ totalPrice, setCartItems }) => {
    const handleClearCart = async () => {
        try {
            const response = await clearCart();
            if (response.status === 204) {
                setCartItems([])
            }
        } catch (error) {
            console.log(error)
        }
    };

    return (
        <div className="bg-white rounded-md px-4 py-6 h-max shadow-[0_2px_12px_-3px_rgba(61,63,68,0.3)]">
            <ul className="text-slate-900 font-medium space-y-4">
                <li className="flex flex-wrap gap-4 text-sm font-semibold">Итого <span className="ml-auto">{totalPrice}₽</span></li>
            </ul>

            <div className="mt-8 space-y-2">
                <button type="button" className="text-sm px-4 py-2.5 w-full font-semibold tracking-wide bg-slate-800 hover:bg-slate-900 text-white rounded-md">Заказать</button>
                <button type="button" onClick={handleClearCart}
                    className="text-sm px-4 py-2.5 w-full font-semibold tracking-wide bg-transparent hover:bg-slate-100 text-slate-900 border border-slate-300 rounded-md">Очистить корзину</button>
            </div>
        </div>
    );
}

export default CartTotal;
