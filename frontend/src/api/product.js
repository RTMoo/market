import { request } from './request'

export const getProducts = (page = 1) => request('get', `catalog/product/?page=${page}`)