import type { Note } from "./note";
import type { Summarization } from "./summarization";
import type { UploadedFile } from "./uploaded-file";

export type Course = {
  id: string;
  name: string;
  user_id: string;
  description: string;
  created_at: string;
  updated_at: string;
  notes: Note[];
  uploaded_files: UploadedFile[];
  summaries: Summarization[];
};
