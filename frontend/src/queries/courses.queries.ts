import queryClient from "@/lib/queryClient";
import coursesServices from "@/services/courses.service";
import { queryOptions } from "@tanstack/react-query";

export const courseQueries = {
  getCourses: () =>
    queryOptions({
      queryKey: ["courses"],
      queryFn: () => coursesServices.getCoursesForUser(),
    }),
  getCourse: (id: string) =>
    queryOptions({
      queryKey: ["course", id],
      queryFn: () => coursesServices.getCourseById(id),
    }),
};
