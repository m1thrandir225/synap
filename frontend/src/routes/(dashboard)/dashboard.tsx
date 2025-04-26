import DashboardLayout from "@/layouts/dashboard";
import { useAuthStore } from "@/stores/auth.store";
import { createFileRoute, redirect } from "@tanstack/react-router";

export const Route = createFileRoute("/(dashboard)/dashboard")({
  beforeLoad: ({ context, location }) => {
    const authStore = useAuthStore.getState();

    if (!authStore.isAuthenticated) {
      throw redirect({
        to: "/login",
        search: {
          redirect: location.href,
        },
      });
    }
  },
  component: RouteComponent,
});

function RouteComponent() {
  return <DashboardLayout />;
}
