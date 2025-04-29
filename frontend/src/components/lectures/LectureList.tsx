import type { Lecture } from "@/types/models/lecture";
import { ScrollArea } from "@radix-ui/react-scroll-area";
import LectureCard from "./LectureCard";
import ListEmpty from "../ListEmpty";

interface ComponentProps {
  items: Lecture[];
}

const LectureList: React.FC<ComponentProps> = (props) => {
  const { items } = props;

  if (items.length < 1) {
    return <ListEmpty />;
  }

  return (
    <ScrollArea className="w-full h-[400px]">
      {items.map((item) => (
        <LectureCard item={item} />
      ))}
    </ScrollArea>
  );
};

export default LectureList;
