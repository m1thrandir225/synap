import { Outlet, createRootRoute } from "@tanstack/react-router";

import Header from "../components/Header";
import DefaultLayout from "@/layouts/default";
import { useAuthStore } from "@/stores/auth.store";

export const Route = createRootRoute({
  component: () => <App />,
});

const App: React.FC = () => {
  const hasHydrated = useAuthStore((state) => state._hasHydrated);

  if (!hasHydrated) {
    return <p> Loading ... </p>;
  }
  return <DefaultLayout />;
};
