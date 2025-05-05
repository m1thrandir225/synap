import config from "@/lib/config";
import { apiRequest, multipartApiRequest } from "./api.service";
import type {
  UploadFileRequest,
  UploadFileResponse,
} from "@/types/responses/files";

const fileURL = `${config.apiUrl}/files`;

const fileService = {
  getUserFiles: () =>
    apiRequest<{ filename: string }[]>({
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
};

export default fileService;
