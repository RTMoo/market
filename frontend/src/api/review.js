import { request } from './request';

export const getProductReviews = (product_id) => request("get", `reviews/product/${product_id}/`);
export const createReview = (data) => request("post", "reviews/create/", data);
export const deleteReview = (id) => request("delete", `reviews/delete/${id}/`);
export const updateReview = (id, data) => request("patch", `reviews/update/${id}/`, data);