import CourseCard from "@/components/courses/CourseCard";
import CourseLectures from "@/components/courses/CourseLectures";
import CourseNotes from "@/components/courses/CourseNotes";
import { dummyCourses } from "@/types/models/course";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/courses/$courseId/")({
  loader: ({ params }) => {
    const course = dummyCourses.find((el) => el.id === params.courseId);
    return {
      course,
    };
  },
  component: RouteComponent,
});

function RouteComponent() {
  const { course } = Route.useLoaderData();

  if (!course) {
    return <h1> Not Found </h1>;
  }
  return (
    <div className="w-full h-full flex flex-col items-start gap-8">
      <CourseCard course={course} />
      <div className="grid grid-cols-2 w-full gap-8">
        <CourseLectures items={[]} />
        <CourseNotes notes={[]} />
      </div>
    </div>
  );
}
