import type { UploadedFile } from "../models/uploaded-file";

export type UploadFileRequest = {
  file: File;
};

export type UploadFileResponse = string;
