import NoteEditor from "@/components/notes/NoteEditor";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/notes/new")({
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className="w-full h-full min-h-[400px]">
      <NoteEditor />
    </div>
  );
}
