import { request } from "./request";

export const getOrderList = () => request("get", "order/");
export const getOrder = (id) => request("get", `order/${id}/`);
