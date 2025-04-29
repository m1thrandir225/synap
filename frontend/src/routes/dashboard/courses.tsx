import { createFileRoute, Outlet } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/courses")({
  component: RouteComponent,
  loader: () => {
    return {
      crumb: "Courses",
    };
  },
});

function RouteComponent() {
  return <Outlet />;
}
