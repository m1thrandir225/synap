import config from "@/lib/config";
import { apiRequest, multipartApiRequest } from "./api.service";
import type {
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
  downloadFile: (filename: string) =>
    apiRequest<Blob>({
      url: `${fileURL}/${filename}`,
      method: "GET",
      headers: undefined,
      protected: true,
      params: undefined,
      responseType: "blob",
    }),
};

export default fileService;
