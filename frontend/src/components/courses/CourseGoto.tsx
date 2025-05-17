import { Link } from "@tanstack/react-router";
import { Button } from "../ui/button";
import { Undo2 } from "lucide-react";

interface ComponentProps {
  course_id: string;
}

const CourseGoto: React.FC<ComponentProps> = ({ course_id }) => {
  return (
    <Button asChild variant={"outline"}>
      <Link to="/dashboard/courses/$courseId" params={{ courseId: course_id }}>
        <Undo2 />
        Course Page
      </Link>
    </Button>
  );
};

export default CourseGoto;
