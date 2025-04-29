import NoteList from "@/components/notes/NoteList";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/notes/")({
  component: RouteComponent,
  loader: () => {
    return {};
  },
});

function RouteComponent() {
  return <NoteList items={[]} />;
}
