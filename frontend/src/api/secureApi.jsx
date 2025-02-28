import axios from "axios";

const API_URL = "http://localhost:8000/api/";

const secureApi = axios.create({
  baseURL: API_URL,
  withCredentials: true,
});

// Перехватчик ответов (авто-обновление токена при 401)
secureApi.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      console.error("Ошибка 401: требуется обновление токена.");
      return Promise.reject(error);
    }
    return Promise.reject(error);
  }
);

export default secureApi;
