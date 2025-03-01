import axios from "axios";

axios.defaults.withCredentials = true
const API_URL = "http://localhost:8000/api/accounts/";

export const login = async (email, password) => {
  try {
    const response = await axios.post(`${API_URL}login/`, { email, password });
    return response.data;
  } catch (error) {
    throw error.response?.data || { detail: "Ошибка авторизации" };
  }
};

export const register = async (email, password, password2) => {
  try {
    const response = await axios.post(`${API_URL}register/`, { email, password, password2 });
    return response.data;
  } catch (error) {
    throw error.response?.data || { detail: "Ошибка регистрации" };
  }
};

export const logout = async () => {
  try {
    await axios.post(`${API_URL}logout/`);
  } catch (error) {
    console.error("Ошибка выхода:", error.response?.data || "Неизвестная ошибка");
  }
};
