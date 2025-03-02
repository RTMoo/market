import axios from "axios";

axios.defaults.withCredentials = true;
const API_URL = "http://localhost:8000/api/";

const api = axios.create({
  baseURL: API_URL,
  withCredentials: true,
});

// Вспомогательная функция для запросов
export const request = async (method, url, data = {}) => {
  try {
    const response = await api({ method, url, data });
    return response.data;
  } catch (error) {
    throw error.response?.data || { detail: "Ошибка запроса" };
  }
};

// Автообновление токена при 401
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401 && !error.config._retry) {
      error.config._retry = true;
      try {
        await request("post", "accounts/refresh/");
        return api(error.config);
      } catch (refreshError) {
        console.error("Ошибка обновления токена:", refreshError);
      }
    }
    return Promise.reject(error);
  }
);