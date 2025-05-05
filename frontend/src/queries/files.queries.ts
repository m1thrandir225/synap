import fileService from "@/services/files.service";
import { queryOptions } from "@tanstack/react-query";

const fileQueries = {
  getUserFiles: queryOptions({
    queryKey: ["files"],
    queryFn: () => fileService.getUserFiles(),
  }),
};

export default fileQueries;
