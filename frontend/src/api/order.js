import { request } from "./request";

export const getOrderList = () => request("get", "order/list/");
export const getOrderDetail = (id) => request("get", `order/get/${id}/`);
export const createOrder = (data) => request("post", "order/create/", data);
export const getOrderItemDetail = (id) => request("get", `order/item/get/${id}/`);

export const getSellerOrderList = () => request("get", `order/seller/list/${id}/`);
export const updateSellerOrderItem = (id) => request("patch", `order/seller/item/update/${id}/`);
