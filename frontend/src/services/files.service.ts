import config from "@/lib/config";
import { apiRequest, multipartApiRequest } from "./api.service";
import type {
  DeleteFileResponse,
  DownloadFileResponse,
  UploadFileRequest,
  UploadFileResponse,
} from "@/types/responses/files";
import type { UploadedFile } from "@/types/models/uploaded-file";

const fileURL = `${config.apiUrl}/files`;

const fileService = {
  getUserFiles: () =>
    apiRequest<UploadedFile[]>({
      url: fileURL,
      method: "GET",
      headers: undefined,
      protected: true,
      params: undefined,
    }),
  uploadFile: (input: UploadFileRequest) =>
    multipartApiRequest<UploadFileRequest, UploadFileResponse>({
      url: `${fileURL}`,
      method: "POST",
      headers: undefined,
      protected: true,
      data: input,
      params: undefined,
    }),
  downloadFile: (file_id: string) =>
    apiRequest<DownloadFileResponse>({
      url: `${fileURL}/${file_id}`,
      method: "GET",
      headers: undefined,
      protected: true,
      params: undefined,
      responseType: "json",
    }),
  deleteFile: (file_id: string) =>
    apiRequest<DeleteFileResponse>({
      url: `${fileURL}/${file_id}`,
      method: "DELETE",
      headers: undefined,
      protected: true,
      params: undefined,
      responseType: "json",
    }),
};

export default fileService;
