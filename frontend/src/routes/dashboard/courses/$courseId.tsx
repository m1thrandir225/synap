import CourseCard from "@/components/courses/CourseCard";
import CourseLectures from "@/components/courses/CourseLectures";
import CourseNotes from "@/components/courses/CourseNotes";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/courses/$courseId")({
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className="w-full h-full flex flex-col items-start gap-8">
      <CourseCard
        course={{
          id: "",
          name: "Example",
          content: "Example Description",
        }}
      />

      <CourseLectures items={[]} />

      <CourseNotes items={[]} />
    </div>
  );
}
