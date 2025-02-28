import secureApi from "./secureApi";
import { refreshToken, logout } from "./authService";
import { useNavigate } from "react-router-dom";

export const requestWithAuth = async (url, method = "GET", data = null) => {
  const navigate = useNavigate();

  try {
    const response = await secureApi({ url, method, data });
    return response.data;
  } catch (error) {
    if (error.response?.status === 401) {
      try {
        await refreshToken();
        
        // Повторяем запрос
        const retryResponse = await secureApi({ url, method, data });
        return retryResponse.data;
      } catch (refreshError) {
        await logout();
        navigate("/login");
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
};
