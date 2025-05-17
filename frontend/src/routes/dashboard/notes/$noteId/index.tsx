import CourseGoto from "@/components/courses/CourseGoto";
import NoteDeleteDialog from "@/components/notes/NoteDeleteDialog";
import NotePreview from "@/components/notes/NotePreview";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { noteQueries } from "@/queries/notes.queries";
import { useSuspenseQuery } from "@tanstack/react-query";
import { createFileRoute, Link } from "@tanstack/react-router";
import { Pen, Undo2 } from "lucide-react";

export const Route = createFileRoute("/dashboard/notes/$noteId/")({
  loader: async ({ params, context: { queryClient } }) => {
    return queryClient.ensureQueryData(noteQueries.getNote(params.noteId));
  },
  component: RouteComponent,
});

function RouteComponent() {
  const { noteId } = Route.useParams();
  const { data: note } = useSuspenseQuery(noteQueries.getNote(noteId));

  return (
    <div className="flex flex-col items-start gap-8">
      <Card className="w-full">
        <CardHeader className="w-full flex flex-row items-center justify-between">
          <CardTitle>{note.title}</CardTitle>
          <div className="flex flex-row items-center gap-2">
            <CourseGoto course_id={note.course_id} />

            <Button asChild size={"icon"} variant={"outline"}>
              <Link
                to="/dashboard/notes/$noteId/edit"
                params={{ noteId: note.id }}
              >
                <Pen />
              </Link>
            </Button>
            <NoteDeleteDialog noteId={note.id} />
          </div>
        </CardHeader>
      </Card>

      <Card className="w-full">
        <CardContent>
          <NotePreview content={note.content} />
        </CardContent>
      </Card>
    </div>
  );
}
