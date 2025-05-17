import NoteList from "@/components/notes/NoteList";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
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
          className="w-full h-[250px] flex items-center justify-center border  rounded-lg group hover:shadow-md transition-all ease-in-out duration-300 gap-4 "
        >
          <Library
            size={32}
            className=" transition-all ease-in-out duration-300"
          />
          <h1> Courses </h1>
        </Link>
        <Link
          to="/dashboard/courses"
          className="w-full h-[250px] flex items-center justify-center border  rounded-lg group hover:shadow-md transition-all ease-in-out duration-300 gap-4 "
        >
          <Book
            size={32}
            className=" transition-all ease-in-out duration-300"
          />
          <h1> Lectures </h1>
        </Link>

        <Link
          to="/dashboard/courses"
          className="w-full h-[250px] flex items-center justify-center border  rounded-lg group hover:shadow-md transition-all ease-in-out duration-300 gap-4 "
        >
          <Notebook
            size={32}
            className=" transition-all ease-in-out duration-300"
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
