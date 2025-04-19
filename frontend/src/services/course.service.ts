import type { Course } from "@/types/models/course"
import {apiRequest} from "@/services/api.service.ts";
import config from "@/lib/config.ts";
const courseUrl = `${config.apiUrl}/course`

export const courseService = {
  getAll: () => apiRequest<Course[]>({
      ...config,
      url: courseUrl,
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: {},
      method: "GET"
  }),
  getSingle: (id: string) => apiRequest<Course>({
      ...config,
      url: courseUrl,
      //url: `${courseUrl}/${id}`
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: { id },
      method: "GET"
  })
}