import type { Note } from "@/types/models/note";

import NoteCard from "./NoteCard";
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
