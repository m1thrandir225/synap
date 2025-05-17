import CourseLectures from "@/components/courses/CourseLectures";
import LectureList from "@/components/lectures/LectureList";
import NoteList from "@/components/notes/NoteList";
import {Card, CardContent, CardHeader, CardTitle} from "@/components/ui/card";
import {noteQueries} from "@/queries/notes.queries";
import {summarizationQueries} from "@/queries/summarization.queries";
import summarizationService from "@/services/summarization.service";
import {useSuspenseQuery} from "@tanstack/react-query";
import {createFileRoute, Link} from "@tanstack/react-router";
import {Library, Notebook} from "lucide-react";

export const Route = createFileRoute("/dashboard/")({
  component: RouteComponent,
  loader: ({context: {queryClient}}) => {
    const summaries = queryClient.ensureQueryData(
      summarizationQueries.getUserSummarizations
    );
    const notes = queryClient.ensureQueryData(noteQueries.getNotes);
    return {
      summaries,
      notes,
    };
  },
});

function RouteComponent() {
  const {data: notes} = useSuspenseQuery(noteQueries.getNotes);
  const {data: summaries} = useSuspenseQuery(
    summarizationQueries.getUserSummarizations
  );
  return (
    <div className="flex flex-col items-start gap-8">
      <div className="w-full h-full grid grid-cols-2 gap-4">
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
          to="/dashboard/notes"
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
            <NoteList items={notes} />
          </CardContent>
        </Card>

        <Card className="w-full">
          <CardHeader>
            <CardTitle>Recent Lectures</CardTitle>
          </CardHeader>
          <CardContent>
            <LectureList items={summaries} />
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
