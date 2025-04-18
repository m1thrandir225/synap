import { createFileRoute, Link } from "@tanstack/react-router";

export const Route = createFileRoute("/")({
  component: App,
});

function App() {
  return (
    <div>
      <h1> Hello from synap !</h1>
      <p> Backend {import.meta.env.VITE_BACKEND_URL}</p>
      <Link to="/dashboard"> Dashboard </Link>
    </div>
  );
}
