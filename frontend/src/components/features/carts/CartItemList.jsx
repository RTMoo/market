import CartItemCard from "./CartItemCard";

const CartItemList = ({ cartItems }) => {
    console.log(cartItems)
    return (
        <>
            {cartItems.map((item) => (
                <CartItemCard key={item.id} item={item} />
            ))}
        </>
    );
};

export default CartItemList