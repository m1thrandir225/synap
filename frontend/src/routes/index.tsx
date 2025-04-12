import { createFileRoute } from "@tanstack/react-router";
import logo from "../logo.svg";
import DefaultLayout from "@/layouts/default";

export const Route = createFileRoute("/")({
  component: App,
});

function App() {
  return <h1> Hello from Synap!</h1>;
}
