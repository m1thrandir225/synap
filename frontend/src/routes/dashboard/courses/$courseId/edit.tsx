import CourseForm from "@/components/courses/CourseForm";
import { dummyCourses, type Course } from "@/types/models/course";
import type { EditCourseRequest } from "@/types/responses/courses";
import { useMutation } from "@tanstack/react-query";
import { createFileRoute, useParams } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/courses/$courseId/edit")({
  loader: ({ params }) => {
    const course = dummyCourses.find((el) => el.id === params.courseId);
    return {
      course,
      crumb: "Edit",
    };
  },
  component: RouteComponent,
});

function RouteComponent() {
  const { course } = Route.useLoaderData();
  const { mutateAsync } = useMutation({
    mutationKey: ["edit-course", course?.id],
    mutationFn: async (input: EditCourseRequest) => "edited data",
    onSuccess: (response) => {},
  });

  if (!course) {
    return <h1> Not Found ...</h1>;
  }

  return (
    <div className="w-full flex flex-col gap-8 items-center justify-center h-full">
      <CourseForm
        title="Eidt Course Details"
        description="Change the details of the current course:"
        defaultValues={course}
        submitValues={async (input) => {
          mutateAsync({
            ...input,
            id: course.id,
          });
        }}
      />
    </div>
  );
}
