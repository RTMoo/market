import { request } from "./request";

export const getOrderList = () => request("get", "order/list/");
export const getOrderDetail = (id) => request("get", `order/get/${id}/`);
export const createOrder = (data) => request("post", "order/create/", data);
export const getOrderItemDetail = (id) => request("get", `order/item/get/${id}/`);

export const getSellerOrderItemList = () => request("get", `order/seller/item/list/${id}/`);
export const updateSellerOrderItem = (id) => request("patch", `order/seller/item/update/${id}/`);
