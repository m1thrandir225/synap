
import type { Note } from "@/types/models/note"
import config from "@/lib/config.ts";
import {apiRequest} from "@/services/api.service.ts";
const noteUrl = `${config.apiUrl}/note`

export const noteService = {
  getAll: () => apiRequest<Note[]>({
      ...config,
      url: noteUrl,
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: {},
      method: "GET"
  }),
  getSingle: (id: string) => apiRequest<Note>({
      ...config,
      url: noteUrl,
      //url: `${noteUrl}/${id}`
      protected: true,
      headers: {
          'Content-Type': 'application/json',
      },
      params: { id },
      method: "GET"
  })
}