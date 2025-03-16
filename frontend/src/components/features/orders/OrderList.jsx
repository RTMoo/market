import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { getOrderList } from '../../../api/order';
import OrderItemCard from './OrderItemCard';


const OrderList = () => {
    const [orders, setOrders] = useState([]);
    const fetchOrders = async () => {
        try {
            const response = await getOrderList();
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
