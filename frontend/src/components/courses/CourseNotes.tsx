import type { Note } from "@/types/models/note";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "../ui/card";
import NoteList from "../notes/NoteList";

interface ComponentProps {
  notes: Note[];
}

const CourseNotes: React.FC<ComponentProps> = (props) => {
  const { notes } = props;
  return (
    <Card className="w-full h-auto">
      <CardHeader>
        <CardTitle> Notes </CardTitle>
        <CardDescription>Your notes on the course:</CardDescription>
      </CardHeader>
      <CardContent>
        <NoteList items={notes} />
      </CardContent>
    </Card>
  );
};

export default CourseNotes;
