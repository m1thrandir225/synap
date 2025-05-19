import CourseForm from "@/components/courses/CourseForm";
import coursesServices from "@/services/courses.service";
import type { CreateCourseRequest } from "@/types/responses/courses";
import { useMutation } from "@tanstack/react-query";
import { createFileRoute, useRouter } from "@tanstack/react-router";
import { toast } from "sonner";

export const Route = createFileRoute("/dashboard/courses/new")({
  component: RouteComponent,
  loader: () => {
    return {
      crumb: "New",
    };
  },
});

function RouteComponent() {
  const router = useRouter();
  const { mutateAsync, status } = useMutation({
    mutationKey: ["new-course"],
    mutationFn: async (input: CreateCourseRequest) =>
      coursesServices.createCourse(input),
    onSuccess: ({ id }) => {
      toast.success("Sucessfully created a new course!");
      router.navigate({
        to: "/dashboard/courses/$courseId",
        params: { courseId: id },
      });
    },
    onError: (error) => {
      toast.error(`Error: ${error.message}`);
    },
  });
  return (
    <div className="w-full flex flex-col gap-8 items-center justify-center h-full">
      <CourseForm
        title="Create Course"
        description="Enter details for your new course:"
        submitValues={async (input) => {
          mutateAsync(input);
        }}
        isLoading={status === "pending"}
      />
    </div>
  );
}
