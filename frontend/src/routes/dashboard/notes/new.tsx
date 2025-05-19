import NoteEditor from "@/components/notes/NoteEditor";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
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
import noteServices from "@/services/note.service";
import type { Course } from "@/types/models/course";
import type { CreateNoteRequest } from "@/types/responses/notes";
import { useMutation, useSuspenseQuery } from "@tanstack/react-query";
import { createFileRoute, useRouter } from "@tanstack/react-router";
import { Loader2 } from "lucide-react";
import { useState } from "react";
import { toast } from "sonner";
import * as z from "zod";

const searchParams = z.object({
  courseId: z.string().optional(),
});

export const Route = createFileRoute("/dashboard/notes/new")({
  component: RouteComponent,
  validateSearch: searchParams,
  loader: async ({ context: { queryClient } }) => {
    const courses = queryClient.ensureQueryData(courseQueries.getCourses());
    return {
      courses,
      crumb: "New",
    };
  },
});

function RouteComponent() {
  const { data: courses } = useSuspenseQuery(courseQueries.getCourses());
  const router = useRouter();
  const { courseId } = Route.useSearch();
  const [title, setTitle] = useState<string | undefined>(undefined);
  const [content, setContent] = useState<string | undefined>(undefined);
  const [selectedCourse, setSelectedCourse] = useState<string | undefined>(
    courseId,
  );
  const { mutateAsync, status } = useMutation({
    mutationFn: async (input: CreateNoteRequest) =>
      noteServices.createNote(input),
    onSuccess: (response) => {
      toast.success("Sucessfully created a new note!");
      router.navigate({
        to: "/dashboard/notes/$noteId",
        params: { noteId: response.id },
      });
    },
    onError: (error) => {
      toast.error(`Error: ${error.message}`);
    },
  });

  const saveNote = async () => {
    try {
      if (!selectedCourse || !title || !content) {
        return;
      }
      await mutateAsync({
        course_id: selectedCourse,
        content: content,
        title: title,
      });
    } catch (e: unknown) {
      throw e;
    }
  };
  return (
    <div className="w-full h-full min-h-[400px] flex flex-col items-start gap-8">
      <Card className="w-full">
        <CardHeader>
          <CardTitle> New Note </CardTitle>
          <CardDescription>
            Create a new note by adding a name, and adding your content written
            in markdown!
          </CardDescription>
        </CardHeader>
      </Card>
      <Card className="w-full ">
        <CardContent className="flex flex-col gap-4">
          <div className="grid gap-2 w-full">
            <Label htmlFor="name"> Name </Label>
            <Input
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="The name of the note"
            />
          </div>
          <div className="grid gap-2 w-full">
            <Label htmlFor="courseId">Course</Label>
            <Select value={selectedCourse} onValueChange={setSelectedCourse}>
              <SelectTrigger className="w-full">
                <SelectValue placeholder="Select a course" />
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
            className="w-full min-h-[450px]"
            contentValue={content}
            setContentValue={setContent}
          />
          <Button
            className="self-end"
            disabled={status === "pending"}
            onClick={saveNote}
          >
            {status === "pending" ? (
              <Loader2 className="animate-spin" />
            ) : (
              <p> Save </p>
            )}
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}
