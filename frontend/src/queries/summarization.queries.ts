import summarizationService from "@/services/summarization.service";

import { queryOptions } from "@tanstack/react-query";

export const summarizationQueries = {
  getSummarization: (id: string) =>
    queryOptions({
      queryKey: ["summarization", id],
      queryFn: () => summarizationService.getSummarization(id),
    }),
};
