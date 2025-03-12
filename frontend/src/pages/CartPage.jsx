import { useState, useEffect } from 'react';
import { getCart } from '../api/cart';
import CartItemList from '../components/features/carts/CartItemList';

const CartPage = () => {
    const [cartItems, setCartItems] = useState([]);

    const fetchGetCart = async () => {
        try {
            const response = await getCart();
            if (response.status === 200) {
                setCartItems(response.data.items);
            }
        } catch (error) {
            console.log(error);
        }
    };

    useEffect(() => {
        fetchGetCart();
    }, []);

    return (
        <div className="max-w-5xl max-md:max-w-xl mx-auto mt-4">
            <h1 className="text-2xl font-bold text-slate-900">Your Cart</h1>
            <div className="grid md:grid-cols-3 gap-10 mt-8">
                <div className="md:col-span-2 space-y-4">
                    <CartItemList cartItems={cartItems} />
                </div>

                <div className="bg-white rounded-md px-4 py-6 h-max shadow-[0_2px_12px_-3px_rgba(61,63,68,0.3)]">
                    <ul className="text-slate-900 font-medium space-y-4">
                        <li className="flex flex-wrap gap-4 text-sm">Subtotal <span className="ml-auto font-semibold">$200.00</span></li>
                        <li className="flex flex-wrap gap-4 text-sm">Shipping <span className="ml-auto font-semibold">$2.00</span></li>
                        <li className="flex flex-wrap gap-4 text-sm">Tax <span className="ml-auto font-semibold">$4.00</span></li>
                        <hr className="border-slate-300" />
                        <li className="flex flex-wrap gap-4 text-sm font-semibold">Total <span className="ml-auto">$206.00</span></li>
                    </ul>

                    <div className="mt-8 space-y-2">
                        <button type="button" className="text-sm px-4 py-2.5 w-full font-semibold tracking-wide bg-slate-800 hover:bg-slate-900 text-white rounded-md">Buy Now</button>
                        <button type="button" className="text-sm px-4 py-2.5 w-full font-semibold tracking-wide bg-transparent hover:bg-slate-100 text-slate-900 border border-slate-300 rounded-md">Continue Shopping  </button>
                    </div>

                    <div className="mt-4 flex flex-wrap justify-center gap-4">
                        <img src='https://readymadeui.com/images/master.webp' alt="card1" className="w-10 object-contain" />
                        <img src='https://readymadeui.com/images/visa.webp' alt="card2" className="w-10 object-contain" />
                        <img src='https://readymadeui.com/images/american-express.webp' alt="card3" className="w-10 object-contain" />
                    </div>
                </div>
            </div>
        </div>
    );
}

export default CartPage;
