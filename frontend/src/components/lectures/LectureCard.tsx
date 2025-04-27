import type { Lecture } from "@/types/models/lecture";

interface ComponentProps {
  item: Lecture;
}

//TODO: implement
const LectureCard: React.FC<ComponentProps> = ({ item }) => {
  return <div> Lecture Card..</div>;
};

export default LectureCard;
