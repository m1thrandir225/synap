import NoteEditor from "@/components/notes/NoteEditor";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { dummyCourses } from "@/types/models/course";
import { dummyNotes } from "@/types/models/note";
import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";

export const Route = createFileRoute("/dashboard/notes/$noteId/edit")({
  loader: async ({ params }) => {
    const note = dummyNotes.find((el) => el.id === params.noteId);
    const courses = dummyCourses;

    return {
      courses,
      note,
      crumb: "Edit",
    };
  },
  component: RouteComponent,
});

function RouteComponent() {
  const { courses, note } = Route.useLoaderData();
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
          <div className="grid gap-2 w-full">
            <Label htmlFor="courseId">Course</Label>
            <Select
              defaultValue={courses.find((el) => el.id === note.course_id)?.id}
            >
              <SelectTrigger className="w-full">
                <SelectValue id="courseId" placeholder="Select a course" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectLabel>Courses</SelectLabel>
                  {courses.map((item) => (
                    <SelectItem value={item.id}>{item.name}</SelectItem>
                  ))}
                </SelectGroup>
              </SelectContent>
            </Select>
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
