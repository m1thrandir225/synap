import { formatDate } from "@/lib/utils";
import type { Note } from "@/types/models/note";
import { Link } from "@tanstack/react-router";
import { Pen } from "lucide-react";

interface ComponentProps {
  item: Note;
}

const NoteCard: React.FC<ComponentProps> = ({ item }) => {
  return (
    <Link
      to="/dashboard/notes/$noteId"
      params={{ noteId: item.id }}
      className="w-ful h-full"
    >
      <div className="p-4 border rounded-md my-2 hover:bg-muted transition-all ease-in-out duration-300 flex flex-row items-center justify-between">
        {item.title}
        <div className="text-sm text-neutral-500 flex flex-row items-center gap-2">
          {formatDate(item.updated_at)}
          <Pen width={16} height={16} />
        </div>
      </div>
    </Link>
  );
};

export default NoteCard;
