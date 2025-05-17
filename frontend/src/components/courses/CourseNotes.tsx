import type { Note } from "@/types/models/note";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "../ui/card";
import NoteList from "../notes/NoteList";
import { Button } from "../ui/button";
import { Link, useParams } from "@tanstack/react-router";
import { Plus } from "lucide-react";

interface ComponentProps {
  notes: Note[];
}

const CourseNotes: React.FC<ComponentProps> = (props) => {
  const { notes } = props;
  const { courseId } = useParams({
    from: "/dashboard/courses/$courseId",
  });
  return (
    <Card className="w-full h-auto">
      <CardHeader>
        <div className="flex flex-row items-center justify-between w-full">
          <div className="flex flex-col items-start gap-2">
            <CardTitle> Notes </CardTitle>
            <CardDescription>Your notes on the course:</CardDescription>
          </div>
          <Button asChild size={"icon"} variant={"outline"}>
            <Link
              to="/dashboard/notes/new"
              search={{
                courseId: courseId,
              }}
            >
              <Plus />
            </Link>
          </Button>
        </div>
      </CardHeader>
      <CardContent>
        <NoteList items={notes} />
      </CardContent>
    </Card>
  );
};

export default CourseNotes;
