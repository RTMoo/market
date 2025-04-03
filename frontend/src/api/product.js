import { request } from './request'

export const getProducts = (page = 1) => request('get', `catalog/products/list/?page=${page}`)
export const createProduct = (data) => request('post', 'catalog/products/create/', data)
export const getUserProducts = () => request('get', 'catalog/products/seller-list/')
export const getProductInfo = (id) => request('get', `catalog/products/${id}/get/`)
export const deleteProduct = (id) => request('delete', `catalog/products/${id}/delete/`)
export const updateProduct = (id, data) => request('patch', `catalog/products/${id}/update/`, data)

export const getCategories = () => request('get', 'catalog/categories/list/')