import type { UploadedFile } from "../models/uploaded-file";

export type UploadFileRequest = {
  file: File;
  course_id: string;
};

export type UploadFileResponse = UploadedFile;
