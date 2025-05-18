import { formatDate } from "@/lib/utils";
import type { Summarization } from "@/types/models/summarization";
import { Link } from "@tanstack/react-router";
import { Asterisk } from "lucide-react";

interface ComponentProps {
  lecture: Summarization;
}

const LectureListItem: React.FC<ComponentProps> = (props) => {
  const { lecture } = props;
  return (
    <Link
      to="/dashboard/lectures/$summarizationId"
      params={{ summarizationId: lecture.id }}
      className="w-ful h-full"
    >
      <div className="p-4 border rounded-md my-2 hover:bg-muted transition-all ease-in-out duration-300 flex flex-row items-center justify-between">
        {lecture.name}

        <div className="text-sm text-neutral-500 flex flex-row items-center gap-2">
          {formatDate(lecture.updated_at)}
          <Asterisk size={16} />
        </div>
      </div>
    </Link>
  );
};

export default LectureListItem;
