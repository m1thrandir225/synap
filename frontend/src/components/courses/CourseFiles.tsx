import type { UploadedFile } from "@/types/models/uploaded-file";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "../ui/card";
import UploadedFileList from "../files/UploadedFileList";
import { Button } from "../ui/button";
import { Link } from "@tanstack/react-router";
import { Upload } from "lucide-react";

interface Props {
  courseId: string;
  items: UploadedFile[];
}

const CourseFiles: React.FC<Props> = (props) => {
  const { items, courseId } = props;

  return (
    <Card className="w-full">
      <CardHeader className="flex flex-row items-center justify-between">
        <div className="flex flex-col items-start gap-2 ">
          <CardTitle>Files</CardTitle>
          <CardDescription>Files associated with this course</CardDescription>
        </div>
        <Button asChild size={"icon"} variant={"outline"}>
          <Link
            to="/dashboard/courses/$courseId/upload"
            params={{ courseId: courseId }}
          >
            <Upload />
          </Link>
        </Button>
      </CardHeader>
      <CardContent className="w-full h-full">
        <UploadedFileList items={items} />
      </CardContent>
    </Card>
  );
};

export default CourseFiles;
