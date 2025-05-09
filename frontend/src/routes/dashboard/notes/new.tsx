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
import type { Course } from "@/types/models/course";
import { useMutation } from "@tanstack/react-query";
import { createFileRoute } from "@tanstack/react-router";
import { Loader2 } from "lucide-react";
import { useState } from "react";

export const Route = createFileRoute("/dashboard/notes/new")({
  component: RouteComponent,
  loader: async () => {
    const courses = [] as Course[];

    return {
      courses,
      crumb: "New",
    };
  },
});

function RouteComponent() {
  const { courses } = Route.useLoaderData();
  const [name, setName] = useState("");
  const [content, setContent] = useState<string | undefined>("");
  const { mutateAsync, isPending } = useMutation({
    mutationFn: async () => "",
    onSuccess: (response) => {
      //TODO: route to new note
    },
  });

  const saveNote = async () => {
    try {
      await mutateAsync();
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
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="The name of the note"
            />
          </div>
          <div className="grid gap-2 w-full">
            <Label htmlFor="courseId">Course</Label>
            <Select>
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
          <Button className="self-end" disabled={isPending} onClick={saveNote}>
            {isPending ? <Loader2 className="animate-spin" /> : <p> Save </p>}
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}
