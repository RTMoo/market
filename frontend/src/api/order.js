import { request } from "./request";


export const getOrderList = () => request("get", "order/buyer/list/");
export const getOrderDetail = (id) => request("get", `order/buyer/get/${id}/`);
export const createOrder = (data) => request("post", "order/buyer/create/", data);
export const updateBuyerOrderStatus = (id, data) => request("patch", `order/buyer/update/${id}/`, data);


export const getSellerOrderList = () => request("get", `order/seller/list/`);
export const getSellerOrderDetail = (id) => request("get", `order/seller/get/${id}/`);
export const updateSellerOrderStatus = (id, data) => request("patch", `order/seller/update/${id}/`, data);
