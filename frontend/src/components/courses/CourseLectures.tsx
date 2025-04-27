import type { Lecture } from "@/types/models/lecture";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "../ui/card";
import { ScrollArea } from "@radix-ui/react-scroll-area";
import LectureCard from "../lectures/LectureCard";

interface ComponentProps extends React.ComponentPropsWithoutRef<"div"> {
  items: Lecture[];
}

const CourseLectures: React.FC<ComponentProps> = ({ items }) => {
  return (
    <Card className="w-full h-full">
      <CardHeader>
        <CardTitle> Lectures </CardTitle>
        <CardDescription> Lectures asociated with this course </CardDescription>
      </CardHeader>
      <CardContent>
        <ScrollArea className="w-full h-[400px]">
          {items.map((lecture) => (
            <LectureCard item={lecture} key={lecture.id} />
          ))}
        </ScrollArea>
      </CardContent>
    </Card>
  );
};

export default CourseLectures;
