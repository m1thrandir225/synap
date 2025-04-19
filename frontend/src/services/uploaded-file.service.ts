import type { UploadedFile } from "@/types/models/uploaded-file"
import config from "@/lib/config.ts";
import {apiRequest} from "@/services/api.service.ts";
const uploadedfileUrl = `${config.apiUrl}/uploaded-file`

export const uploadedfileService = {
  getAll: () => apiRequest<UploadedFile[]>({
      ...config,
      url: uploadedfileUrl,
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: {},
      method: "GET"
  }),
  getSingle: (id: string) => apiRequest<UploadedFile>({
      ...config,
      url: uploadedfileUrl,
      //url: `${uploadedfileUrl}/${id}`
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: { id },
      method: "GET"
  })
}