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
import { courseQueries } from "@/queries/courses.queries";
import { noteQueries } from "@/queries/notes.queries";
import noteServices from "@/services/note.service";
import type { Course } from "@/types/models/course";
import { dummyNotes } from "@/types/models/note";
import type { EditNoteRequest } from "@/types/responses/notes";
import { useMutation, useSuspenseQuery } from "@tanstack/react-query";
import { createFileRoute, useRouter } from "@tanstack/react-router";
import { Loader2 } from "lucide-react";
import { useState } from "react";

export const Route = createFileRoute("/dashboard/notes/$noteId/edit")({
  loader: async ({ params, context: { queryClient } }) => {
    const note = queryClient.ensureQueryData(
      noteQueries.getNote(params.noteId),
    );

    const courses = queryClient.ensureQueryData(courseQueries.getCourses());

    return {
      courses,
      note,
      crumb: "Edit",
    };
  },
  component: RouteComponent,
});

function RouteComponent() {
  const { noteId } = Route.useParams();
  const { data: note } = useSuspenseQuery(noteQueries.getNote(noteId));
  const { data: courses } = useSuspenseQuery(courseQueries.getCourses());
  const [title, setTitle] = useState<string | undefined>(note?.title);
  const [selectedCourse, setSelectedCourse] = useState<string | undefined>(
    note?.course_id,
  );
  const [content, setContent] = useState<string | undefined>(note?.content);

  const router = useRouter();
  const { mutateAsync, status } = useMutation({
    mutationKey: ["edit-note", noteId],
    mutationFn: (input: EditNoteRequest) =>
      noteServices.updateNote(noteId, input),

    onSuccess: (response) => {
      router.navigate({
        to: "/dashboard/notes/$noteId",
        params: { noteId: response.id },
      });
    },
  });

  const handleUpdate = async () => {
    try {
      if (!title || !selectedCourse || !content) {
        return;
      }
      await mutateAsync({
        title: title,
        course_id: selectedCourse,
        content: content,
      });
    } catch (e) {
      throw e;
    }
  };

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
            <Input value={title} onChange={(e) => setTitle(e.target.value)} />
          </div>
          <div className="grid gap-2 w-full">
            <Label htmlFor="courseId">Course</Label>
            <Select
              value={selectedCourse}
              onValueChange={setSelectedCourse}
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
          <Button
            className="self-end"
            disabled={status === "pending"}
            onClick={handleUpdate}
          >
            {status === "pending" ? (
              <Loader2 className="animate-spin" />
            ) : (
              <span> Save Changes </span>
            )}
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}
