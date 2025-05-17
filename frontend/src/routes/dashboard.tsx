import Loader from "@/components/Loader";
import DashboardLayout from "@/layouts/dashboard";
import { useAuthStore } from "@/stores/auth.store";
import { createFileRoute, redirect } from "@tanstack/react-router";

export const Route = createFileRoute("/dashboard")({
  beforeLoad: ({ location }) => {
    const isAuthenticated = useAuthStore.getState().isAuthenticated;

    if (!isAuthenticated) {
      throw redirect({
        to: "/login",
        search: {
          redirect: location.href,
        },
      });
    }
  },
  component: RouteComponent,
  loader: () => {
    return {
      crumb: "Dashboard",
    };
  },
  pendingComponent: Loader,
});

function RouteComponent() {
  return <DashboardLayout />;
}
