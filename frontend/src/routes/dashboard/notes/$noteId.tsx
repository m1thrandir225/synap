import { createFileRoute, Outlet } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/notes/$noteId")({
  component: RouteComponent,
});

function RouteComponent() {
  return <Outlet />;
}
