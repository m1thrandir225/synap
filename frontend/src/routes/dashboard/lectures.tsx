import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard/lectures")({
  component: RouteComponent,
  loader: async ({}) => {
    return {
      crumb: "Lectures",
    };
  },
});

function RouteComponent() {
  return <div>Hello "/dashboard/lectures"!</div>;
}
