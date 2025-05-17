import type { Summarization } from "@/types/models/summarization";
import { Card, CardHeader, CardTitle } from "../ui/card";

import FileDownload from "../files/FileDownload";

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
          <FileDownload
            filename={item.file.file_name}
            text="Download Original"
          />
        </div>
      </CardHeader>
    </Card>
  );
};

export default LectureCard;
