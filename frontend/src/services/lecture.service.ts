import type { Lecture } from "@/types/models/lecture"
import config from "@/lib/config.ts";
import {apiRequest} from "@/services/api.service.ts";
const lectureUrl = `${config.apiUrl}/lecture`

export const lectureService = {
  getAll: () => apiRequest<Lecture[]>({
      ...config,
      url: lectureUrl,
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: {},
      method: "GET"
  }),
  getSingle: (id: string) => apiRequest<Lecture>({
      ...config,
      url: lectureUrl,
      //url: `${lectureUrl}/${id}`
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: { id },
      method: "GET"
  })
}