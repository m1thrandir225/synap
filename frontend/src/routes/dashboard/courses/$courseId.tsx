import CourseCard from "@/components/courses/CourseCard";
import CourseLectures from "@/components/courses/CourseLectures";
import CourseNotes from "@/components/courses/CourseNotes";
import { dummyCourses } from "@/types/models/course";
import { createFileRoute, useLoaderData } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/courses/$courseId")({
  loader: ({ params }) => {
    return dummyCourses.find((el) => el.id === params.courseId);
  },
  component: RouteComponent,
});

function RouteComponent() {
  const course = Route.useLoaderData();

  if (!course) {
    return <h1> Not Found </h1>;
  }
  return (
    <div className="w-full h-full flex flex-col items-start gap-8">
      <CourseCard course={course} />

      <CourseLectures items={[]} />

      <CourseNotes items={[]} />
    </div>
  );
}
