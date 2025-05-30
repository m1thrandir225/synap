import NoteList from "@/components/notes/NoteList";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { noteQueries } from "@/queries/notes.queries";
import { useSuspenseQuery } from "@tanstack/react-query";
import { createFileRoute, Link } from "@tanstack/react-router";
import { Plus } from "lucide-react";

export const Route = createFileRoute("/dashboard/notes/")({
  component: RouteComponent,
  loader: ({ context: { queryClient } }) => {
    return queryClient.ensureQueryData(noteQueries.getNotes);
  },
});

function RouteComponent() {
  const { data: notes } = useSuspenseQuery(noteQueries.getNotes);
  return (
    <div className="w-full h-full flex flex-col items-start gap-8">
      <Card className="w-full">
        <CardHeader className="w-full flex flex-row items-center justify-between">
          <div className="flex flex-col items-start gap-4">
            <CardTitle>Notes</CardTitle>
            <CardDescription>Your personal notes.</CardDescription>
          </div>
          <Button asChild size={"icon"} variant={"default"}>
            <Link to="/dashboard/notes/new">
              <Plus />
            </Link>
          </Button>
        </CardHeader>
      </Card>
      <Card className="w-full">
        <CardContent>
          <NoteList items={notes} />
        </CardContent>
      </Card>
    </div>
  );
}
