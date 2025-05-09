import CourseForm from "@/components/courses/CourseForm";
import { courseQueries } from "@/queries/courses.queries";
import coursesServices from "@/services/courses.service";
import { type Course } from "@/types/models/course";
import type { EditCourseRequest } from "@/types/responses/courses";
import { useMutation, useSuspenseQuery } from "@tanstack/react-query";
import { createFileRoute, useParams, useRouter } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/courses/$courseId/edit")({
  loader: ({ params, context: { queryClient } }) => {
    const course = queryClient.ensureQueryData(
      courseQueries.getCourse(params.courseId),
    );
    return {
      course,
      crumb: "Edit",
    };
  },
  component: RouteComponent,
});

function RouteComponent() {
  const { courseId } = Route.useParams();
  const { data: course } = useSuspenseQuery(courseQueries.getCourse(courseId));
  const router = useRouter();
  const { mutateAsync } = useMutation({
    mutationKey: ["edit-course", course?.id],
    mutationFn: async (input: EditCourseRequest) =>
      coursesServices.editCourse(input),
    onSuccess: (response) => {
      router.navigate({
        to: "/dashboard/courses/$courseId",
        params: { courseId },
      });
    },
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
