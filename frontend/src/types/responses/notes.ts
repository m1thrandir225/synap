import type { Note } from "../models/note";

export type CreateNoteRequest = {
  title: string;
  content: string;
  course_id: string;
};

export type CreateNoteResponse = Note & {};

export type EditNoteRequest = {
  content: string;
  course_id: string;
  title: string;
};

export type EditNoteResponse = Note & {};
