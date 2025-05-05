import { createFileRoute, Outlet } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/files")({
  component: RouteComponent,
  loader: () => {
    return {
      crumb: "Files",
    };
  },
});

function RouteComponent() {
  return <Outlet />;
}
