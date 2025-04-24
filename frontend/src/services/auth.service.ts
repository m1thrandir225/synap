import type { LoginResponse } from "@/types/responses/auth";
import { apiRequest } from "./api.service";
import config from "@/lib/config";

const authURL = `${config.apiUrl}/auth`;

const authService = {
  login: (input: { username: string; password: string }) =>
    apiRequest<LoginResponse>({
      url: authURL,
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      params: undefined,
      protected: false,
      data: input,
    }),
};

export default authService;
