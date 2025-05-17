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
      className="my-2"
    >
      <h1 className="w-full border px-4 py-2 rounded-lg">{lecture.name}</h1>
    </Link>
  );
};

export default LectureListItem;
