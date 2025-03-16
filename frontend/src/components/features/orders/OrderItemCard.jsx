import React from 'react';


const OrderItemCard = ({ order }) => {
    return (
        <div className="bg-white p-6 rounded-2xl shadow-[0_2px_12px_-3px_rgba(61,63,68,0.3)] mb-4 flex flex-col sm:flex-row justify-between items-center">
            <div className="flex flex-col sm:flex-row items-center gap-4">
                <div className="flex flex-col">
                    <h3 className="text-lg font-semibold text-gray-900">Заказ #{order.id}</h3>
                    <p className="text-sm text-gray-500">Дата: {new Date(order.created_at).toLocaleDateString()}</p>
                    <p className="text-sm text-gray-500">Статус: 
                        <span className={`ml-2 px-2 py-1 rounded text-xs font-medium 
                            ${order.status === 'pending' ? 'bg-yellow-100 text-yellow-700' : ''}
                            ${order.status === 'shipped' ? 'bg-blue-100 text-blue-700' : ''}
                            ${order.status === 'delivered' ? 'bg-green-100 text-green-700' : ''}
                        `}>
                            {order.status}
                        </span>
                    </p>
                </div>
            </div>
            <div className="flex flex-col items-end">
                <p className="text-sm text-gray-500">Получатель: <span className="font-medium text-gray-900">{order.full_name}</span></p>
                <p className="text-sm text-gray-500">Телефон: <span className="font-medium text-gray-900">{order.phone_number}</span></p>
                <p className="text-sm text-gray-500">Адрес: <span className="font-medium text-gray-900">{order.to_address}</span></p>
                <p className="text-lg font-semibold text-gray-900 mt-2">{order.total_price} ₸</p>
            </div>
        </div>
    );
}

export default OrderItemCard;




