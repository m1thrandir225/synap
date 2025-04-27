import type { Note } from "@/types/models/note";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "../ui/card";
import { ScrollArea } from "../ui/scroll-area";
import NoteCard from "../notes/NoteCard";

interface ComponentProps extends React.ComponentPropsWithoutRef<"div"> {
  items: Note[];
}

const CourseNotes: React.FC<ComponentProps> = ({ items }) => {
  return (
    <Card className="w-full h-full">
      <CardHeader>
        <CardTitle> Notes </CardTitle>
        <CardDescription>Notes that are related to this course</CardDescription>
      </CardHeader>
      <CardContent>
        <ScrollArea className="w-full h-[400px]">
          {items.map((note) => (
            <NoteCard item={note} />
          ))}
        </ScrollArea>
      </CardContent>
    </Card>
  );
};

export default CourseNotes;
