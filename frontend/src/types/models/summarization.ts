import type { UploadedFile } from "./uploaded-file";
import type { Recommendation } from "./recommendation";

export type Summarization = {
  id: string;
  file_id: string;
  name: string;
  summary_text: string;
  ai_model_used: string | undefined;
  created_at: string;
  updated_at: string;
  file: UploadedFile;
  recommendations: Recommendation[];
};
