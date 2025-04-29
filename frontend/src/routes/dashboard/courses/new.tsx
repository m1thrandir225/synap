import CourseForm from "@/components/courses/CourseForm";
import type { CreateCourseRequest } from "@/types/responses/courses";
import { useMutation } from "@tanstack/react-query";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/courses/new")({
  component: RouteComponent,
  loader: () => {
    return {
      crumb: "New",
    };
  },
});

function RouteComponent() {
  const { mutateAsync } = useMutation({
    mutationKey: ["new-course"],
    mutationFn: async (input: CreateCourseRequest) => "hello World",
    onSuccess: (response) => {},
  });
  return (
    <div className="w-full flex flex-col gap-8 items-center justify-center h-full">
      <CourseForm
        title="Create Course"
        description="Enter details for your new course:"
        submitValues={async (input) => {
          mutateAsync(input);
        }}
      />
    </div>
  );
}
