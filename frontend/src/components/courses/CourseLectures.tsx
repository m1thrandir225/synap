import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "../ui/card";
import LectureList from "../lectures/LectureList";
import type { Summarization } from "@/types/models/summarization";

interface ComponentProps extends React.ComponentPropsWithoutRef<"div"> {
  items: Summarization[];
}

const CourseLectures: React.FC<ComponentProps> = (props) => {
  const { items } = props;
  return (
    <Card className="w-full h-auto">
      <CardHeader>
        <CardTitle> Lectures </CardTitle>
        <CardDescription> Lectures asociated with this course </CardDescription>
      </CardHeader>
      <CardContent>
        <LectureList items={items} />
      </CardContent>
    </Card>
  );
};

export default CourseLectures;
