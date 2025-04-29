import NotePreview from "@/components/notes/NotePreview";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { dummyNotes } from "@/types/models/note";
import { createFileRoute, Link } from "@tanstack/react-router";
import MDEditor from "@uiw/react-md-editor";
import { Pen } from "lucide-react";

export const Route = createFileRoute("/dashboard/notes/$noteId/")({
  loader: async ({ params }) => {
    const note = dummyNotes.find((el) => el.id === params.noteId);
    return {
      note,
    };
  },
  component: RouteComponent,
});

function RouteComponent() {
  const { note } = Route.useLoaderData();

  if (!note) {
    return <p> Not found ...</p>;
  }
  return (
    <div className="flex flex-col items-start gap-8">
      <Card className="w-full">
        <CardHeader className="w-full flex flex-row items-center justify-between">
          <CardTitle>{note.title}</CardTitle>
          <div className="flex flex-row items-center gap-2">
            <Button asChild size={"icon"} variant={"outline"}>
              <Link
                to="/dashboard/notes/$noteId/edit"
                params={{ noteId: note.id }}
              >
                <Pen />
              </Link>
            </Button>
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
