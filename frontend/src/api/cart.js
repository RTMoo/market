import { request } from './request';


export const getCart = () => request('get', 'cart/');
export const clearCart = () => request('delete', `cart/clear/`);

export const addCartItem = (product_id) => request('post', 'cart/add/', { product_id });
export const updateCartItem = (id, quantity) => request('patch', `cart/update/${id}/`, { quantity });
export const deleteCartItem = (id) => request('delete', `cart/delete/${id}/`);
