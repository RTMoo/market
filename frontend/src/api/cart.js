import { request } from './request';


export const getCart = () => request('get', 'cart/');
export const addCart = (product_id) => request('post', 'cart/add/', { product_id });
export const updateCart = (id, quantity) => request('patch', `cart/update/${id}/`, { quantity });
export const deleteCart = (id) => request('delete', `cart/delete/${id}/`);
