import { useAuthStore } from "@/stores/auth.store";
import { createFileRoute, Link, useNavigate } from "@tanstack/react-router";
import { useEffect } from "react";

export const Route = createFileRoute("/")({
  component: App,
});

function App() {
  const { _hasHydrated, isAuthenticated, logout } = useAuthStore();
  const navigate = useNavigate();
  if (!_hasHydrated) {
    return <p> Loading ... </p>;
  }

  useEffect(() => {
    if (isAuthenticated) {
      navigate({ to: "/dashboard" });
    }
  }, [isAuthenticated]);

  return (
    <div>
      <h1> Welcome to Synap</h1>
      <button onClick={logout}> Logout </button>
    </div>
  );
}
