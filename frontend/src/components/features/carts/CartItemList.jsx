import CartItemCard from "./CartItemCard";

const CartItemList = ({ cartItems, setCartItems }) => {

    return (
        <>
            {cartItems.map((item) => (
                <CartItemCard key={item.id} item={item} setCartItems={setCartItems} />
            ))}
        </>
    );
};

export default CartItemList