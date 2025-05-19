import type { UploadedFile } from "../models/uploaded-file";

export type UploadFileRequest = {
  file: File;
  course_id: string;
};

export type UploadFileResponse = UploadedFile;

export type DownloadFileResponse = {
  url: string;
  filename: string;
};

export type DeleteFileResponse = {
  message: string;
};
