import Loader from "@/components/Loader";
import { noteQueries } from "@/queries/notes.queries";
import { dummyNotes } from "@/types/models/note";
import { createFileRoute, Outlet } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/notes/$noteId")({
  component: RouteComponent,
  loader: ({ params, context: { queryClient } }) => {
    const note = queryClient.ensureQueryData(
      noteQueries.getNote(params.noteId),
    );

    return {
      crumb: note.then((res) => res.title),
    };
  },
  pendingComponent: Loader,
});

function RouteComponent() {
  return <Outlet />;
}
