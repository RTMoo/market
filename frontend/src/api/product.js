import { request } from './request'

export const getProducts = (page = 1) => request('get', `catalog/product/?page=${page}`)
export const createProduct = (data) => request('post', `catalog/product/`, data)

export const getCategories = () => request('get', `catalog/category/`)
