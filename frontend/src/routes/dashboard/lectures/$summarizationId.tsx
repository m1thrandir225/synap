import LectureCard from "@/components/lectures/LectureCard";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import queryClient from "@/lib/queryClient";
import { summarizationQueries } from "@/queries/summarization.queries";
import { useSuspenseQuery } from "@tanstack/react-query";
import { createFileRoute } from "@tanstack/react-router";
import { Loader2 } from "lucide-react";

export const Route = createFileRoute("/dashboard/lectures/$summarizationId")({
  component: RouteComponent,
  loader: ({ context: { queryClient }, params }) => {
    const lecture = queryClient.ensureQueryData(
      summarizationQueries.getSummarization(params.summarizationId),
    );
    return {
      lecture,
      crumb: lecture.then((res) => res.name),
    };
  },
  pendingComponent: () => {
    return <Loader2 className="animate-spin" />;
  },
  errorComponent: () => {
    return <h1> Something went wrong...</h1>;
  },
  notFoundComponent: () => {
    return <h1> The current item is not found.</h1>;
  },
});

function RouteComponent() {
  const { summarizationId } = Route.useParams();
  const { data: summarization } = useSuspenseQuery(
    summarizationQueries.getSummarization(summarizationId),
  );
  return (
    <div className="w-full h-full flex flex-col items-start gap-8">
      <LectureCard item={summarization} />
      <Card className="w-full">
        <CardHeader>
          <CardTitle>Summary</CardTitle>
        </CardHeader>
        <CardContent>
          <p>{summarization.summary_text}</p>
        </CardContent>
      </Card>
    </div>
  );
}
