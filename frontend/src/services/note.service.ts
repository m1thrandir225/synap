import config from "@/lib/config";
import { apiRequest } from "./api.service";
import type { Note } from "@/types/models/note";
import type {
  CreateNoteRequest,
  EditNoteRequest,
} from "@/types/responses/notes";

const notesURL = `${config.apiUrl}/notes`;

const noteServices = {
  getUserNotes: () =>
    apiRequest<Note[]>({
      url: `${notesURL}`,
      method: "GET",
      protected: true,
      headers: undefined,
      params: undefined,
    }),
  getNotesForCourse: (courseId: string) =>
    apiRequest<Note[]>({
      url: `${notesURL}?course_id=${courseId}`,
      method: "GET",
      protected: true,
      headers: undefined,
      params: undefined,
    }),
  createNote: (input: CreateNoteRequest) =>
    apiRequest<Note>({
      url: `${notesURL}`,
      method: "POST",
      protected: true,
      headers: undefined,
      params: undefined,
      data: input,
    }),
  updateNote: (noteId: string, input: EditNoteRequest) =>
    apiRequest<Note>({
      url: `${notesURL}/${noteId}`,
      method: "PUT",
      protected: true,
      headers: undefined,
      params: undefined,
      data: input,
    }),
  deleteNote: (noteId: string) =>
    apiRequest<boolean>({
      url: `${notesURL}/${noteId}`,
      method: "DELETE",
      protected: true,
      headers: undefined,
      params: undefined,
    }),
};

export default noteServices;
