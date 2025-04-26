import type { LoginRequest, LoginResponse } from "@/types/responses/auth";
import { apiRequest, multipartApiRequest } from "./api.service";
import config from "@/lib/config";

const authURL = `${config.apiUrl}/auth`;

const authService = {
  login: (input: { username: string; password: string }) =>
    multipartApiRequest<LoginRequest, LoginResponse>({
      url: `${authURL}/login`,
      method: "POST",
      headers: undefined,
      params: undefined,
      protected: false,

      data: input,
    }),
};

export default authService;
