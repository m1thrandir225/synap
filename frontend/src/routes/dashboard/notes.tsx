import { createFileRoute, Outlet } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/notes")({
  component: RouteComponent,
  loader: () => {
    return {
      crumb: "Notes",
    };
  },
});

function RouteComponent() {
  return <Outlet />;
}
