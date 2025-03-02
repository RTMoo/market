import { request } from "./request";

export const getProfile = () => request("get", "profile/me/")
export const updateProfile = (data) => request("patch", "profile/me/", data)
