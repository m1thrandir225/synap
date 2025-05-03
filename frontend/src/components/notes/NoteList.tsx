import type { Note } from "@/types/models/note";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "../ui/card";
import { ScrollArea } from "../ui/scroll-area";
import NoteCard from "./NoteCard";
import { PackageOpen } from "lucide-react";
import ListEmpty from "../ListEmpty";

interface ComponentProps {
  items: Note[];
}

const NoteList: React.FC<ComponentProps> = (props) => {
  const { items } = props;

  if (items.length < 1) {
    return <ListEmpty />;
  }
  return (
    <div className="w-full min-h-[400px]">
      {items.map((note) => (
        <NoteCard item={note} />
      ))}
    </div>
  );
};

export default NoteList;
