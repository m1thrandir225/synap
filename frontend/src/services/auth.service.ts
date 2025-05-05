import {
  type RegisterResponse,
  type LoginRequest,
  type LoginResponse,
  type RegisterRequest,
  type RefreshTokenResponse,
  type LogoutResponse,
} from "@/types/responses/auth";
import { apiRequest, multipartApiRequest } from "./api.service";
import config from "@/lib/config";

const authURL = `${config.apiUrl}/auth`;

const authService = {
  login: (input: LoginRequest) =>
    multipartApiRequest<LoginRequest, LoginResponse>({
      url: `${authURL}/login`,
      method: "POST",
      headers: undefined,
      params: undefined,
      protected: false,

      data: input,
    }),
  register: (input: RegisterRequest) =>
    apiRequest<RegisterResponse>({
      url: `${authURL}/signup`,
      method: "POST",
      headers: undefined,
      params: undefined,
      protected: false,
      data: input,
    }),
  refreshToken: (token: string) =>
    apiRequest<RefreshTokenResponse>({
      url: `${authURL}/refresh`,
      method: "POST",
      data: {
        refresh_token: token,
      },
      params: undefined,
      protected: false,
      headers: undefined,
    }),
  logout: () =>
    apiRequest<LogoutResponse>({
      url: `${authURL}/logout`,
      method: "POST",
      headers: undefined,
      data: undefined,
      protected: true,
      params: undefined,
      withCredentials: true,
    }),
};

export default authService;
