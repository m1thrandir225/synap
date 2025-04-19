//file: example.service.ts
import type { RecommendationInteraction } from "@/types/models/recommendation-interaction"
import config from "@/lib/config.ts";
import {apiRequest} from "@/services/api.service.ts";
const recommendationinteractionUrl = `${config.apiUrl}/recommendationinteraction`

export const recommendationinteractionService = {
  getAll: () => apiRequest<RecommendationInteraction[]>({
      ...config,
      url: recommendationinteractionUrl,
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: {},
      method: "GET"
  }),
  getSingle: (id: string) => apiRequest<RecommendationInteraction>({
      ...config,
      url: recommendationinteractionUrl,
      //url: `${recommendationinteractionUrl}/${id}`
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: { id },
      method: "GET"
  })
}