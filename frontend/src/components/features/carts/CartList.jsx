import { useEffect, useState } from 'react';
import { getCart } from '../../../api/cart';
import ProductCard from '../products/ProductCard';

const CartList = () => {
    const [cartItems, setCartItems] = useState([]);
    
    const fetchGetCart = async () => {
        try {
            const response = await getCart();
            if (response.status === 200) {
                setCartItems(response.data.items);
                console.log(response.data.items)
            }
        } catch (error) {
            console.log(error);
        }
    };

    useEffect(() => {
        fetchGetCart();
    }, []);

    return (
        <div className="">
            <h2 className="text-2xl font-bold mb-4">Корзина</h2>
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                {cartItems.length > 0 ? (
                    cartItems.map((item) => (
                        <ProductCard key={item.id} item={item} isCart={true}/>
                    ))
                ) : (
                    <p>Корзина пуста</p>
                )}
            </div>
        </div>
    );
};

export default CartList