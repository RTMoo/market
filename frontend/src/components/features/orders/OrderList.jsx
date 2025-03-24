import { useEffect, useState } from 'react';
import { getOrderList, getSellerOrderList } from '../../../api/order';
import OrderItemCard from './OrderItemCard';


const OrderList = () => {
    const [orders, setOrders] = useState([]);
    const fetchOrders = async () => {
        try {
            const role = localStorage.getItem('role');
            const response = await (role === 'S' ? getSellerOrderList() : getOrderList());
            if (response.status === 200) {
                setOrders(response.data);
            } else {
                console.log(response.data, response.status);
            }
        } catch (error) {
            console.error(error);
        }
    }

    useEffect(() => {
        fetchOrders();
    }, []);

    return (
        <div>
            {orders.map((order) => (
                <OrderItemCard key={order.id} order={order} />
            ))}
        </div>
    );

}

export default OrderList;
