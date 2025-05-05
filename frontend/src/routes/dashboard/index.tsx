import FileList from "@/components/files/FileList";
import LectureList from "@/components/lectures/LectureList";
import NoteList from "@/components/notes/NoteList";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { dummyNotes } from "@/types/models/note";
import { dummyFiles } from "@/types/models/uploaded-file";
import { createFileRoute, Link } from "@tanstack/react-router";
import { Book, Library, Notebook, Pen } from "lucide-react";

export const Route = createFileRoute("/dashboard/")({
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className="flex flex-col items-start gap-8">
      <div className="w-full h-full grid grid-cols-3 gap-4">
        <Link
          to="/dashboard/courses"
          className="w-full h-[250px] flex items-center justify-center border border-amber-100 bg-amber-200 rounded-lg group text-amber-400 hover:text-amber-200 hover:bg-amber-400 transition-all ease-in-out duration-300 gap-4 hover:font-bold hover:text-lg"
        >
          <Library
            size={32}
            className="group-hover:scale-150 transition-all ease-in-out duration-300"
          />
          <h1> Courses </h1>
        </Link>
        <Link
          to="/dashboard/lectures"
          className="w-full h-[250px] flex items-center justify-center border border-cyan-100 bg-cyan-200 rounded-lg group text-cyan-400 hover:text-cyan-200 hover:bg-cyan-400 transition-all ease-in-out duration-300 gap-4 hover:font-bold hover:text-lg"
        >
          <Book
            size={32}
            className="group-hover:scale-150 transition-all ease-in-out duration-300"
          />
          <h1> Lectures </h1>
        </Link>
        <Link
          to="/dashboard/notes"
          className="w-full h-[250px] flex items-center justify-center border border-pink-100 bg-pink-200 rounded-lg group text-pink-400 hover:text-pink-200 hover:bg-pink-400 transition-all ease-in-out duration-300 gap-4 hover:font-bold hover:text-lg"
        >
          <Pen
            size={32}
            className="group-hover:scale-150 transition-all ease-in-out duration-300"
          />
          <h1> Notes </h1>
        </Link>
      </div>
      <div className="grid grid-cols-2 w-full gap-8">
        <Card className="w-full">
          <CardHeader>
            <CardTitle>Recent Notes</CardTitle>
          </CardHeader>
          <CardContent>
            <NoteList items={dummyNotes} />
          </CardContent>
        </Card>

        <Card className="w-full">
          <CardHeader>
            <CardTitle>Recent Lectures</CardTitle>
          </CardHeader>
          <CardContent>
            <NoteList items={dummyNotes} />
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
