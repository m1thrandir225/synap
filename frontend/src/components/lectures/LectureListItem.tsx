import type { Summarization } from "@/types/models/summarization";
import { Link } from "@tanstack/react-router";

interface ComponentProps {
  lecture: Summarization;
}

const LectureListItem: React.FC<ComponentProps> = (props) => {
  const { lecture } = props;
  return (
    <Link
      to="/dashboard/lectures/$summarizationId"
      params={{ summarizationId: lecture.id }}
      className="my-2 group"
    >
      <h1 className="w-full border px-4 py-2 rounded-lg my-2 group-hover:bg-neutral-100 transition-all ease-in-out duration-300">
        {lecture.name}
      </h1>
    </Link>
  );
};

export default LectureListItem;
