import type { Course } from "@/types/models/course";
import { Card, CardDescription, CardHeader, CardTitle } from "../ui/card";
import { Link } from "@tanstack/react-router";
import { Button } from "../ui/button";
import { Pen } from "lucide-react";
import CourseDeleteDialog from "./CourseDeleteDialog";

interface ComponentProps {
  course: Omit<Course, "user_id" | "created_at" | "updated_at" | "notes">;
  inGrid?: boolean;
}

const CourseCard: React.FC<ComponentProps> = ({ course, inGrid }) => {
  if (inGrid) {
    return (
      <Link
        to="/dashboard/courses/$courseId"
        params={{ courseId: course.id }}
        className="w-full h-full"
      >
        <Card className="hover:bg-muted/50 cursor-pointer w-full h-full">
          <CardHeader>
            <CardTitle>{course.name}</CardTitle>
            <CardDescription>{course.content}</CardDescription>
          </CardHeader>
        </Card>
      </Link>
    );
  }
  return (
    <Card className="h-auto w-full">
      <CardHeader>
        <div className="flex flex-row items-center justify-between">
          <div className="flex flex-col items-start gap-2">
            <CardTitle>{course.name}</CardTitle>
            <CardDescription>{course.content}</CardDescription>
          </div>
          <div className="flex flex-row items-center gap-2">
            <Button asChild size={"icon"} variant={"secondary"}>
              <Link
                to="/dashboard/courses/$courseId/edit"
                params={{ courseId: course.id }}
              >
                <Pen />
              </Link>
            </Button>
            <CourseDeleteDialog courseId={course.id} />
          </div>
        </div>
      </CardHeader>
    </Card>
  );
};

export default CourseCard;
