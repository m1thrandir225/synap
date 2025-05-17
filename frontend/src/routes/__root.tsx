import {
  createRootRoute,
  createRootRouteWithContext,
} from "@tanstack/react-router";

import DefaultLayout from "@/layouts/default";
import type { QueryClient } from "@tanstack/react-query";

export const Route = createRootRouteWithContext<{
  queryClient: QueryClient;
}>()({
  head: () => ({
    meta: [
      {
        name: "description",
        content: "AI powered platform made for students",
      },
      {
        title: "Synap",
      },
    ],
  }),
  component: () => <App />,
});

const App: React.FC = () => {
  return <DefaultLayout />;
};
