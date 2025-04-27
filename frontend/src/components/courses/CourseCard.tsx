import type { Course } from "@/types/models/course";
import { Card, CardDescription, CardHeader, CardTitle } from "../ui/card";
import { Link } from "@tanstack/react-router";

interface ComponentProps extends React.ComponentPropsWithoutRef<"div"> {
  course: Omit<Course, "user_id" | "created_at" | "updated_at" | "notes">;
}

const CourseCard: React.FC<ComponentProps> = ({ course, ...props }) => {
  return (
    <Link to="/dashboard/courses/$courseId" params={{ courseId: course.id }}>
      <Card className="hover:bg-muted/50 cursor-pointer">
        <CardHeader>
          <CardTitle>{course.name}</CardTitle>
          <CardDescription>{course.content}</CardDescription>
        </CardHeader>
      </Card>
    </Link>
  );
};

export default CourseCard;
