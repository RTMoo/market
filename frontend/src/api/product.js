import { request } from './request'

export const getProducts = (params = {}) => {
    const query = new URLSearchParams();

    // Обработка параметров
    for (const key in params) {
        const value = params[key];
        // Если значение - массив, добавляем каждый элемент как отдельный параметр
        if (Array.isArray(value)) {
            value.forEach(val => {
                if (val) query.append(key, val); // добавляем только ненулевые значения
            });
        } else if (value !== undefined && value !== '') {
            query.append(key, value); // добавляем, если значение не пустое
        }
    }

    // Если query пустой, не добавляем его в URL
    const queryString = query.toString();
    const url = queryString ? `catalogs/products/list/?${queryString}` : 'catalogs/products/list/';

    return request('get', url);
};


export const createProduct = (data) => request('post', 'catalogs/products/create/', data)
export const getUserProducts = () => request('get', 'catalogs/products/seller-list/')
export const getProductInfo = (id) => request('get', `catalogs/products/${id}/get/`)
export const deleteProduct = (id) => request('delete', `catalogs/products/${id}/delete/`)
export const updateProduct = (id, data) => request('patch', `catalogs/products/${id}/update/`, data)

export const getCategories = () => request('get', 'catalogs/categories/list/')