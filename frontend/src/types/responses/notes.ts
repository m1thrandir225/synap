import type { Note } from "../models/note";

export type CreateNoteRequest = {
  title: string;
  content: string;
  user_id: string;
  course_id: string;
};

export type CreateNoteResponse = Note & {};

export type EditNoteRequest = {};

export type EditNoteResponse = Note & {};
