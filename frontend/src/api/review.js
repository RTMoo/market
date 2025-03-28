import { request } from './request';

export const getProductReviews = (product_id) => request("get", `review/product/${product_id}/`);
export const createReview = (data) => request("post", "review/create/", data);
export const deleteReview = (id) => request("delete", `review/delete/${id}/`);
export const updateReview = (id, data) => request("patch", `review/update/${id}/`, data);