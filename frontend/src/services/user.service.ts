import type { User } from "@/types/models/user"
import config from "@/lib/config.ts";
import {apiRequest} from "@/services/api.service.ts";
const userUrl = `${config.apiUrl}/user`

export const userService = {
  getAll: () => apiRequest<User[]>({
      ...config,
      url: userUrl,
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: {},
      method: "GET"
  }),
  getSingle: (id: string) => apiRequest<User>({
      ...config,
      url: userUrl,
      //url: `${userUrl}/${id}`
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: { id },
      method: "GET"
  })
}