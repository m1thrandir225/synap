import type { AxiosInstance } from "axios";
import axios, { AxiosError } from "axios";
import { useAuthStore } from "~/stores/auth.store";
import type { ApiRequestOptions, MultipartRequestOptions } from "~/types/api";

import config from "~/util/config";
import { buildFormData } from "~/util/form";

const createApiInstance = (): AxiosInstance => {
  const api = axios.create({
    baseURL: config.apiUrl,
    headers: {
      "Content-Type": "application/json",
    },
  });

  /**
   * Request Interceptor
   * Used for adding JWT token if the request is protected
   */
  api.interceptors.request.use((config) => {
    const authStore = useAuthStore.getState();

    const accessToken = authStore.accessToken;

    const isProtected = config.headers?.protected !== false;

    if (!isProtected && accessToken) {
      config.headers.Authorization = `Bearer ${accessToken}`;
    }

    if (config.headers?.protected !== undefined) {
      delete config.headers.protected;
    }
    return config;
  });

  return api;
};

const api = createApiInstance();

/**
 * A generic request abstraction for json requests
 * T is the expected type/interface outcome
 */
export const apiRequest = async <T>(config: ApiRequestOptions) => {
  try {
    const response = await api.request<T>({
      url: config.url,
      method: config.method,
      headers: {
        ...config.headers,
      },
      params: config.params,
      data: config.data,
    });

    return response.data;
  } catch (e: unknown) {
    if (e instanceof AxiosError) {
      throw new Error(e.response?.data.message);
    } else {
      throw new Error("something went wrong. please try again later.");
    }
  }
};

/**
 * A generic request abstraction for multipart requests
 * T is the type/interface of the multipart request
 * R is the type/interface of the expected outcome
 */

export const multipartApiRequest = async <
  T extends Record<string, unknown>,
  R = unknown,
>(
  config: MultipartRequestOptions<T>,
): Promise<R> => {
  try {
    const formData = buildFormData(config.data);

    const response = await api.request<R>({
      url: config.url,
      method: config.method,
      data: formData,
      headers: {
        ...config.headers,
        "Content-Type": "multipart/form-data",
        protected: config.protected,
      },
      params: config.params,
    });
    return response.data;
  } catch (e: unknown) {
    if (e instanceof AxiosError) {
      throw new Error(e.response?.data.message);
    } else {
      throw new Error("Something went wrong. Please try again later.");
    }
  }
};

export default api;
