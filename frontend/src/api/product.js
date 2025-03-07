import { request } from './request'

export const getProducts = (page = 1) => request('get', `catalog/product/?page=${page}`)
export const createProduct = (data) => request('post', 'catalog/product/', data)
export const getUserProducts = () => request('get', 'catalog/user-products/')
export const getCategories = () => request('get', 'catalog/category/')
