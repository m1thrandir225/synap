import CourseCard from "@/components/courses/CourseCard";
import CourseGrid from "@/components/courses/CourseGrid";
import { Button } from "@/components/ui/button";
import { dummyCourses } from "@/types/models/course";
import { createFileRoute, Link } from "@tanstack/react-router";
import { Plus } from "lucide-react";

//TODO: implement queryClient and fetcher when backend routes are ready
export const Route = createFileRoute("/dashboard/courses/")({
  loader: () => {
    return dummyCourses;
  },
  component: RouteComponent,
});

function RouteComponent() {
  const courses = dummyCourses;
  return (
    <div className="w-full h-full flex flex-col items-start gap-8">
      <div className="flex flex-row items-center justify-between w-full">
        <h1 className="font-bold text-2xl">Courses</h1>
        <Button asChild size={"icon"} variant={"secondary"}>
          <Link to="/dashboard/courses">
            <Plus />
          </Link>
        </Button>
      </div>
      <CourseGrid items={courses} />
    </div>
  );
}
