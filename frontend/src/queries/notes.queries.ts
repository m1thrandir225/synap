import noteServices from "@/services/note.service";
import { queryOptions } from "@tanstack/react-query";

export const noteQueries = {
  getNotes: queryOptions({
    queryKey: ["notes"],
    queryFn: () => noteServices.getUserNotes(),
  }),
  getNote: (id: string) =>
    queryOptions({
      queryKey: ["note", id],
      queryFn: () => noteServices.getNote(id),
    }),
};
