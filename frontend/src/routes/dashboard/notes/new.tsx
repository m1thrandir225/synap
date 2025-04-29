import NoteEditor from "@/components/notes/NoteEditor";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useMutation } from "@tanstack/react-query";
import { createFileRoute } from "@tanstack/react-router";
import { Loader2 } from "lucide-react";
import { useState } from "react";

export const Route = createFileRoute("/dashboard/notes/new")({
  component: RouteComponent,
});

function RouteComponent() {
  const [name, setName] = useState("");

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
      <div className="grid gap-2 w-full">
        <Label htmlFor="name"> Name </Label>
        <Input
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="The name of the note"
        />
      </div>
      <NoteEditor className="w-full min-h-[450px] " />
      <Button className="self-end" disabled={isPending} onClick={saveNote}>
        {isPending ? <Loader2 className="animate-spin" /> : <p> Save </p>}
      </Button>
    </div>
  );
}
