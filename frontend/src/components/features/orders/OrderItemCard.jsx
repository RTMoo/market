import React from 'react';


const OrderItemCard = ({ item }) => {

    return (
        <div className="flex bg-white px-4 py-6 rounded-md shadow-[0_2px_12px_-3px_rgba(61,63,68,0.3)] mb-4 justify-between">
            <h3 className="text-sm sm:text-base font-semibold text-slate-900">{item.product_name} {item.quantity} штук.</h3>
            <div className="">
                <div className="text-lg">
                    Итого
                </div>
                <h3 className="text-sm sm:text-base font-semibold text-slate-900 mt-auto">{item.product_price * item.quantity}₽</h3>
            </div>
        </div>

    );
}

export default OrderItemCard;

