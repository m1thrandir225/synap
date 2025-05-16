import FileList from "@/components/files/FileList";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import fileQueries from "@/queries/files.queries";
import { type UploadedFile } from "@/types/models/uploaded-file";
import { useSuspenseQuery } from "@tanstack/react-query";
import { createFileRoute, Link } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/files/")({
  component: RouteComponent,
  loader: ({ context: { queryClient } }) => {
    const files = queryClient.ensureQueryData(fileQueries.getUserFiles);

    return {
      files,
    };
  },
});

function RouteComponent() {
  const { data: files } = useSuspenseQuery(fileQueries.getUserFiles);
  return (
    <div className="w-full h-full flex flex-col items-start gap-8">
      <Card className="w-full">
        <CardHeader>
          <div className="flex flex-row items-center justify-between w-full">
            <div className="flex flex-col items-start gap-4">
              <CardTitle>Files</CardTitle>
              <CardDescription>All of your uploaded files.</CardDescription>
            </div>
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
