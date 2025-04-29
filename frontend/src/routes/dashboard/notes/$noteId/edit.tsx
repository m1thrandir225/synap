import NoteEditor from "@/components/notes/NoteEditor";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { dummyNotes } from "@/types/models/note";
import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";

export const Route = createFileRoute("/dashboard/notes/$noteId/edit")({
  loader: async ({ params }) => {
    const note = dummyNotes.find((el) => el.id === params.noteId);
    return {
      note,
      crumb: "Edit",
    };
  },
  component: RouteComponent,
});

function RouteComponent() {
  const { note } = Route.useLoaderData();
  const [name, setName] = useState<string | undefined>(note?.title);
  const [content, setContent] = useState<string | undefined>(note?.content);
  if (!note) {
    return <p> Not found ...</p>;
  }
  return (
    <div className="w-full flex flex-col items-start gap-8">
      <Card className="w-full">
        <CardHeader>
          <CardTitle>Editing: {note.title}</CardTitle>
        </CardHeader>
      </Card>
      <Card className="w-full">
        <CardContent className="min-h-[400px] flex flex-col gap-4 items-start">
          <div className="grid gap-2 w-full">
            <Label htmlFor="name">Name</Label>
            <Input value={name} onChange={(e) => setName(e.target.value)} />
          </div>
          <NoteEditor
            className="h-full w-full"
            contentValue={content}
            setContentValue={setContent}
          />
          <Button className="self-end">Save Changes</Button>
        </CardContent>
      </Card>
    </div>
  );
}
