import { Button } from "@/components/ui/button";
import {
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { createFileRoute, Link } from "@tanstack/react-router";
import { Plus, Upload } from "lucide-react";

export const Route = createFileRoute("/dashboard/files")({
  component: RouteComponent,
  loader: () => {
    return {
      crumb: "Files",
    };
  },
});

function RouteComponent() {
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
    </div>
  );
}
