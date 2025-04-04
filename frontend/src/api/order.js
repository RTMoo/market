import { request } from "./request";


export const getOrderList = () => request("get", "orders/buyer/list/");
export const getOrderDetail = (id) => request("get", `orders/buyer/get/${id}/`);
export const createOrder = (data) => request("post", "orders/buyer/create/", data);
export const updateBuyerOrderStatus = (id, data) => request("patch", `orders/buyer/update/${id}/`, data);


export const getSellerOrderList = () => request("get", `orders/seller/list/`);
export const getSellerOrderDetail = (id) => request("get", `orders/seller/get/${id}/`);
export const updateSellerOrderStatus = (id, data) => request("patch", `orders/seller/update/${id}/`, data);
