import { request } from "./request";

export const getOrderList = () => request("get", "order/");
export const getOrderInfo = (id) => request("get", `order/${id}/`);
export const createOrder = (data) => request("post", "order/create/", data);