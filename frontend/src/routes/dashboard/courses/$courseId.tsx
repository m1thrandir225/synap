import { dummyCourses } from "@/types/models/course";
import { Outlet } from "@tanstack/react-router";

import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/courses/$courseId")({
  loader: ({ params }) => {
    const course = dummyCourses.find((el) => el.id === params.courseId);
    return {
      course,
      crumb: course?.name,
    };
  },
  component: RouteComponent,
});

function RouteComponent() {
  return <Outlet />;
}
