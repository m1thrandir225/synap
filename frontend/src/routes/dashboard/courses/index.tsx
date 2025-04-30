import { Button } from "@/components/ui/button";
import { dummyCourses } from "@/types/models/course";
import { createFileRoute, Link } from "@tanstack/react-router";
import { Plus } from "lucide-react";
import CourseGrid from "@/components/courses/CourseGrid";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
export const Route = createFileRoute("/dashboard/courses/")({
  loader: () => {
    return {
      dummyCourses,
    };
  },
  component: RouteComponent,
});

function RouteComponent() {
  const courses = dummyCourses;
  return (
    <div className="w-full h-full flex flex-col items-start gap-8">
      <Card className="w-full">
        <CardHeader>
          <div className="flex flex-row items-center justify-between w-full">
            <CardTitle>Courses</CardTitle>
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
          <CourseGrid items={courses} />
        </CardContent>
      </Card>
    </div>
  );
}
