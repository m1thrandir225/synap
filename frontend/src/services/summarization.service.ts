import config from "@/lib/config";
import { apiRequest } from "./api.service";
import type { Summarization } from "@/types/models/summarization";
import type { CreateSummarizationRequest } from "@/types/responses/summarization";

const summarizationURL = `${config.apiUrl}/summarization`;

const summarizationService = {
  createSummarization: (input: CreateSummarizationRequest) =>
    apiRequest<Summarization>({
      url: `${summarizationURL}/summarize`,
      method: "POST",
      data: input,
      headers: undefined,
      protected: true,
      params: undefined,
    }),
  getSummarization: (id: string) =>
    apiRequest<Summarization>({
      url: `${summarizationURL}/${id}`,
      method: "GET",
      headers: undefined,
      protected: true,
      params: undefined,
    }),
  getUserSummaries: () =>
    apiRequest<Summarization[]>({
      url: summarizationURL,
      method: "GET",
      headers: undefined,
      protected: true,
      params: undefined,
      responseType: "json",
    }),
};

export default summarizationService;
