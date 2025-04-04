import { request } from './request'

export const getProducts = (page = 1) => request('get', `catalogs/products/list/?page=${page}`)
export const createProduct = (data) => request('post', 'catalogs/products/create/', data)
export const getUserProducts = () => request('get', 'catalogs/products/seller-list/')
export const getProductInfo = (id) => request('get', `catalogs/products/${id}/get/`)
export const deleteProduct = (id) => request('delete', `catalogs/products/${id}/delete/`)
export const updateProduct = (id, data) => request('patch', `catalogs/products/${id}/update/`, data)

export const getCategories = () => request('get', 'catalogs/categories/list/')