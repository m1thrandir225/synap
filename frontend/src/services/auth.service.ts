import {
  type RegisterResponse,
  type LoginRequest,
  type LoginResponse,
  type RegisterRequest,
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
};

export default authService;
