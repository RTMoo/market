import { request } from "./request";

export const getProfile = () => request("get", "profiles/me/")
export const updateProfile = (data) => request("patch", "profiles/me/", data)
