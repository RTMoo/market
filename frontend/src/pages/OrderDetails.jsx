import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getOrderInfo } from '../api/order';

const OrderDetails = () => {
    const { id } = useParams();
    const [order, setOrder] = useState([]);

    const fetchOrder = async () => {
        try {
            const response = await getOrderInfo(id);
            if (response.status === 200) {
                setOrder(response.data);
            } else {
                console.log(response.data, response.status);
            }
        } catch (error) {
            console.error(error);
        }
    }

    useEffect(() => {
        fetchOrder();
    }, [id]);
    console.log(order)

    return (
        <div className="bg-white p-6 rounded-2xl max-w-8xl mx-auto">
            <h2 className="text-xl font-bold text-gray-900 mb-4">Заказ #{order.id}</h2>

            <div className="mb-4">
                <span className={`px-3 py-1 rounded text-sm font-medium 
                    ${order.status === 'pending' ? 'bg-yellow-100 text-yellow-700' : ''}
                    ${order.status === 'shipped' ? 'bg-blue-100 text-blue-700' : ''}
                    ${order.status === 'delivered' ? 'bg-green-100 text-green-700' : ''}
                `}>
                    {order.status}
                </span>
            </div>

            <div className="space-y-4 mb-6">
                {order.items && order.items.length > 0 ? (
                    order.items.map((item) => (
                        <div key={item.id} className="flex justify-between items-center border-b pb-3">
                            <div className="flex items-center gap-4">
                                {item.image && (
                                    <img
                                        src={item.image}
                                        alt={item.name}
                                        className="w-16 h-16 object-cover rounded-lg"
                                    />
                                )}
                                <div>
                                    <h3 className="text-lg font-medium text-gray-900">{item.product_name}</h3>
                                    <p className="text-sm text-gray-500">
                                        {item.quantity} шт. × {item.product_price} ₸
                                    </p>
                                </div>
                            </div>
                            <p className="text-lg font-semibold text-gray-900">
                                {item.quantity * item.product_price} ₸
                            </p>
                        </div>
                    ))
                ) : (
                    <p className="text-gray-500">Заказ пуст или данные загружаются...</p>
                )}
            </div>


            <div className="text-right">
                <p className="text-lg font-semibold text-gray-900">Итого: {order.total_price} ₸</p>
            </div>

            <div className="mt-6 bg-gray-100 p-4 rounded-lg">
                <p className="text-sm text-gray-700">Адрес доставки: <span className="font-medium text-gray-900">{order.to_address}</span></p>
                <p className="text-sm text-gray-700">Телефон: <span className="font-medium text-gray-900">{order.phone_number}</span></p>
            </div>

            <div className="mt-6 flex justify-end gap-4">
                <button className="px-4 py-2 bg-blue-600 text-white rounded-lg shadow">Повторить заказ</button>
                {order.status === 'pending' && (
                    <button className="px-4 py-2 bg-red-500 text-white rounded-lg shadow">Отменить заказ</button>
                )}
            </div>
        </div>
    );
}

export default OrderDetails;
