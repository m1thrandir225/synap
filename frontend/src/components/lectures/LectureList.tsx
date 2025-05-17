import { ScrollArea } from "@radix-ui/react-scroll-area";
import ListEmpty from "../ListEmpty";
import type { Summarization } from "@/types/models/summarization";
import LectureListItem from "./LectureListItem";

interface ComponentProps {
  items: Summarization[];
}

const LectureList: React.FC<ComponentProps> = (props) => {
  const { items } = props;

  if (items.length < 1) {
    return <ListEmpty />;
  }

  return (
    <ScrollArea className="w-full h-[400px]">
      {items.map((item) => (
        <LectureListItem lecture={item} />
      ))}
    </ScrollArea>
  );
};

export default LectureList;
