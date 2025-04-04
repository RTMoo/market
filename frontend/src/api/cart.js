import { request } from './request';


export const getCart = () => request('get', 'carts/');
export const clearCart = () => request('delete', `carts/clear/`);

export const addCartItem = (product_id) => request('post', 'carts/add/', { product_id });
export const updateCartItem = (id, quantity) => request('patch', `carts/update/${id}/`, { quantity });
export const deleteCartItem = (id) => request('delete', `carts/delete/${id}/`);
