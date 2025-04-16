import { request } from './request'

export const getProducts = (params = {}) => {
    const query = new URLSearchParams();

    for (const key in params) {
        const value = params[key];
        if (Array.isArray(value)) {
            value.forEach(val => query.append(key, val));
        } else if (value !== undefined && value !== '') {
            query.append(key, value);
        }
    }

    return request('get', `catalogs/products/list/?${query.toString()}`);
};

export const createProduct = (data) => request('post', 'catalogs/products/create/', data)
export const getUserProducts = () => request('get', 'catalogs/products/seller-list/')
export const getProductInfo = (id) => request('get', `catalogs/products/${id}/get/`)
export const deleteProduct = (id) => request('delete', `catalogs/products/${id}/delete/`)
export const updateProduct = (id, data) => request('patch', `catalogs/products/${id}/update/`, data)

export const getCategories = () => request('get', 'catalogs/categories/list/')