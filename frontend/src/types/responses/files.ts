import type { UploadedFile } from "../models/uploaded-file";

export type UploadFileRequest = {
  file: File;
  course_id: string;
};

export type FileInfo = {
  filename: string;
};

export type UploadFileResponse = FileInfo[];
