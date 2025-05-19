import type { Summarization } from "@/types/models/summarization";
import { Card, CardHeader, CardTitle } from "../ui/card";

import FileDownload from "../files/FileDownload";
import CourseGoto from "../courses/CourseGoto";

interface ComponentProps {
  item: Summarization;
}

const LectureCard: React.FC<ComponentProps> = (props) => {
  const { item } = props;

  return (
    <Card className="w-full">
      <CardHeader>
        <div className="flex flex-row items-center w-full justify-between">
          <CardTitle>{item.name}</CardTitle>
          <div className="flex flex-row gap-2">
            <CourseGoto course_id={item.file.course_id} />
            <FileDownload id={item.file.id} text="Download Original" />
          </div>
        </div>
      </CardHeader>
    </Card>
  );
};

export default LectureCard;
