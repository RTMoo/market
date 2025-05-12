import { request } from "./request";

export const login = (email, password) => request("post", "accounts/login/", { email, password });
export const register = (email, password) => request("post", "accounts/register/", { email, password });
export const logout = () => request("post", "accounts/logout/");
export const confirmCode = (data) => request("post", "accounts/confirm_code/", data);