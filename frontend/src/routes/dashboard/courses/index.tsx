import { Button } from "@/components/ui/button";
import { createFileRoute, Link } from "@tanstack/react-router";
import { Plus } from "lucide-react";
import CourseGrid from "@/components/courses/CourseGrid";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { courseQueries } from "@/queries/courses.queries";
import { useSuspenseQuery } from "@tanstack/react-query";
export const Route = createFileRoute("/dashboard/courses/")({
  loader: ({ context: { queryClient } }) => {
    return queryClient.ensureQueryData(courseQueries.getCourses());
  },
  component: RouteComponent,
});

function RouteComponent() {
  const { data: courses } = useSuspenseQuery(courseQueries.getCourses());
  return (
    <div className="w-full h-full flex flex-col items-start gap-8">
      <Card className="w-full">
        <CardHeader>
          <div className="flex flex-row items-center justify-between w-full">
            <div className="flex flex-col items-start gap-4">
              <CardTitle>Courses</CardTitle>
              <CardDescription>All of your created courses</CardDescription>
            </div>
            <Button asChild size={"icon"} variant={"default"}>
              <Link to="/dashboard/courses/new">
                <Plus />
              </Link>
            </Button>
          </div>
        </CardHeader>
      </Card>

      <Card className="w-full">
        <CardContent>
          {courses.length == 0 && (
            <p>
              Your courses will appear here. Click the + button to create one
            </p>
          )}
          {courses.length > 0 && <CourseGrid items={courses} />}
        </CardContent>
      </Card>
    </div>
  );
}
