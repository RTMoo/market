import { useState, useEffect } from 'react';
import { getCart } from '../api/cart';
import CartItemList from '../components/features/carts/CartItemList';
import CreateOrderForm from '../components/features/orders/CreateOrderForm';

const CartsPage = () => {
    const [cartItems, setCartItems] = useState([]);
    const [totalPrice, setTotalPrice] = useState([]);

    const fetchGetCart = async () => {
        try {
            const response = await getCart();
            if (response.status === 200) {
                setCartItems(response.data.items);
                setTotalPrice(response.data.total_price)
            }
        } catch (error) {
            console.log(error);
        }
    };

    useEffect(() => {
        fetchGetCart();
    }, []);

    return (
        <div className="max-w-8xl max-md:max-w-xl mx-auto mt-4 p-5">
            <h1 className="text-2xl text-slate-900 text-center">Корзина</h1>
            <div className="grid md:grid-cols-3 gap-10 mt-8">
                <div className="sm:col-span-1 md:col-span-2 space-y-4">
                    <CartItemList cartItems={cartItems} setCartItems={setCartItems} />
                </div>
                <CreateOrderForm totalPrice={totalPrice}/>
            </div>
        </div>
    );
}

export default CartsPage;
