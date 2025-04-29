import { createFileRoute } from "@tanstack/react-router";
import MDEditor from "@uiw/react-md-editor";

export const Route = createFileRoute("/dashboard/notes/$noteId/")({
  component: RouteComponent,
});

function RouteComponent() {
  const source = "# Markdown syntax guide\n## Headers";
  return <MDEditor.Markdown source={source} />;
}
