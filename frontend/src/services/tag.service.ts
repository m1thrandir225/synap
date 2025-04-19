import type { Tag } from "@/types/models/tag"
import config from "@/lib/config.ts";
import {apiRequest} from "@/services/api.service.ts";
const tagUrl = `${config.apiUrl}/tag`

export const tagService = {
  getAll: () => apiRequest<Tag[]>({
      ...config,
      url: tagUrl,
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: {},
      method: "GET"
  }),
  getSingle: (id: string) => apiRequest<Tag>({
      ...config,
      url: tagUrl,
      //url: `${tagUrl}/${id}`
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: { id },
      method: "GET"
  })
}