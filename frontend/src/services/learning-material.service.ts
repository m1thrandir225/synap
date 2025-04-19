import type { LearningMaterial } from "@/types/models/learning-material"
import config from "@/lib/config.ts";
import {apiRequest} from "@/services/api.service.ts";
const learningmaterialUrl = `${config.apiUrl}/learning-material`

export const learningmaterialService = {
  getAll: () => apiRequest<LearningMaterial[]>({
      ...config,
      url: learningmaterialUrl,
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: {},
      method: "GET"
  }),
  getSingle: (id: string) => apiRequest<LearningMaterial>({
      ...config,
      url: learningmaterialUrl,
      //url: `${learningmaterialUrl}/${id}
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: { id },
      method: "GET"
  })
}