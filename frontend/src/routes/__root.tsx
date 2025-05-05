import {
  createRootRoute,
  createRootRouteWithContext,
} from "@tanstack/react-router";

import DefaultLayout from "@/layouts/default";
import type { QueryClient } from "@tanstack/react-query";

export const Route = createRootRouteWithContext<{
  queryClient: QueryClient;
}>()({
  component: () => <App />,
});

const App: React.FC = () => {
  return <DefaultLayout />;
};
