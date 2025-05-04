import FileList from "@/components/files/FileList";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { dummyFiles } from "@/types/models/uploaded-file";
import { createFileRoute, Link } from "@tanstack/react-router";
import { Plus, Upload } from "lucide-react";

export const Route = createFileRoute("/dashboard/files")({
  component: RouteComponent,
  loader: () => {
    return {
      files: dummyFiles,
      crumb: "Files",
    };
  },
});

function RouteComponent() {
  const { files } = Route.useLoaderData();
  return (
    <div className="w-full h-full flex flex-col items-start gap-8">
      <Card className="w-full">
        <CardHeader>
          <div className="flex flex-row items-center justify-between w-full">
            <div className="flex flex-col items-start gap-4">
              <CardTitle>Files</CardTitle>
              <CardDescription>All of your uploaded files.</CardDescription>
            </div>
            <Button asChild size={"icon"} variant={"default"}>
              <Link to="/dashboard/courses/new">
                <Upload />
              </Link>
            </Button>
          </div>
        </CardHeader>
      </Card>

      <Card className="w-full">
        <CardContent>
          <FileList items={files} />
        </CardContent>
      </Card>
    </div>
  );
}
