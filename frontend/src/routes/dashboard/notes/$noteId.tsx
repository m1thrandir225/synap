import { dummyNotes } from "@/types/models/note";
import { createFileRoute, Outlet } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/notes/$noteId")({
  component: RouteComponent,
  loader: ({ params }) => {
    const note = dummyNotes.find((el) => el.id === params.noteId);

    return {
      crumb: `${note?.title}`,
    };
  },
});

function RouteComponent() {
  return <Outlet />;
}
