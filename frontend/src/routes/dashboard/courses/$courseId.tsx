import { courseQueries } from "@/queries/courses.queries";
import { Outlet } from "@tanstack/react-router";

import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/courses/$courseId")({
  loader: ({ params, context: { queryClient } }) => {
    const course = queryClient.ensureQueryData(
      courseQueries.getCourse(params.courseId),
    );
    return {
      course,
      crumb: course.then((res) => res.name),
    };
  },
  component: RouteComponent,
});

function RouteComponent() {
  return <Outlet />;
}
