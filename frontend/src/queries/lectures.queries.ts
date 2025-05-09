import { lectureService } from "@/services/lecture.service";
import { queryOptions } from "@tanstack/react-query";

export const lectureQueries = {
  getLectures: queryOptions({
    queryKey: ["lectures"],
    queryFn: () => lectureService.getLectures(),
  }),
  getLecture: (id: string) =>
    queryOptions({
      queryKey: ["lecture", id],
      queryFn: () => lectureService.getLecture(id),
    }),
};
