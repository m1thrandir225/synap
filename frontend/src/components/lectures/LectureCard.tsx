import type { Summarization } from "@/types/models/summarization";
import { Card, CardDescription, CardHeader, CardTitle } from "../ui/card";

interface ComponentProps {
  item: Summarization;
}

const LectureCard: React.FC<ComponentProps> = (props) => {
  const { item } = props;
  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle>{item.name}</CardTitle>
      </CardHeader>
    </Card>
  );
};

export default LectureCard;
