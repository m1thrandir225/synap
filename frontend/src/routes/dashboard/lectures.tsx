import {
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
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
  return (
    <div className="w-full flex flex-col items-start gap-8">
      <Card className="w-full">
        <CardHeader>
          <CardTitle>Lectures</CardTitle>
          <CardDescription>All your lectures in one place</CardDescription>
        </CardHeader>
      </Card>
    </div>
  );
}
