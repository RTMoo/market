import axios from "axios";

axios.defaults.withCredentials = true;
const API_URL = "http://localhost:8000/api/accounts/";

// Авторизация (получение access и refresh токенов)
export const login = async (email, password) => {
  try {
    const response = await axios.post(`${API_URL}login/`, { email, password });
    return response.data;
  } catch (error) {
    throw error.response?.data || { detail: "Ошибка авторизации" };
  }
};

// Регистрация 
export const register = async (email, password, password2) => {
  try {
    const response = await axios.post(`${API_URL}register/`, { email, password, password2 });
    return response.data;
  } catch (error) {
    throw error.response?.data || { detail: "Ошибка авторизации" };
  }
};


// Выход (удаление refresh-токена)
export const logout = async () => {
  try {
    const response = await axios.post(`${API_URL}logout/`);
    return response.data;
  } catch (error) {
    throw error.response?.data || { detail: "Ошибка выхода" };
  }
};

// Обновление access-токена
export const refreshToken = async () => {
  try {
    const response = await axios.post(`${API_URL}refresh/`);
    return response.data;
  } catch (error) {
    throw error.response?.data || { detail: "Ошибка обновления токена" };
  }
};
