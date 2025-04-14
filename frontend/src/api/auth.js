import { request } from "./request";

export const login = (email, password) => request("post", "accounts/login/", { email, password });
export const register = (email, password, password2) => request("post", "accounts/register/", { email, password, password2 });
export const logout = () => request("post", "accounts/logout/");
export const confirmCode = (data) => request("post", "accounts/confirm_code/", data);