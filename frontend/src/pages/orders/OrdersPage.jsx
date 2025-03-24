import React from 'react';
import OrderList from '../../components/features/orders/OrderList';

const OrdersPage = () => {
    return (
        <div className="mx-4">
            <h1 className="text-2xl text-slate-900 text-center my-8">Ваши заказы</h1>
            <OrderList />
        </div>
    );
}

export default OrdersPage;
