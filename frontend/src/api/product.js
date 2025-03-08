import { request } from './request'

export const getProducts = (page = 1) => request('get', `catalog/product/?page=${page}`)
export const createProduct = (data) => request('post', 'catalog/product/', data)
export const getUserProducts = () => request('get', 'catalog/user-products/')
export const getProductInfo = (id) => request('get', `catalog/product/${id}/`)
export const deleteProduct = (id) => request('delete', `catalog/product/${id}/`)

export const getCategories = () => request('get', 'catalog/category/')
export const getCategoryInfo = (id) => request('get', `catalog/category/${id}/`)