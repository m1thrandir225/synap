import Loader from "@/components/Loader";
import { Button } from "@/components/ui/button";
import { useAuthStore } from "@/stores/auth.store";
import { createFileRoute, Link, useNavigate } from "@tanstack/react-router";
import { Activity, Github, LogIn, NotepadText } from "lucide-react";
import { useEffect } from "react";

export const Route = createFileRoute("/")({
  component: App,
});

function App() {
  const { _hasHydrated, isAuthenticated } = useAuthStore();
  const navigate = useNavigate();
  if (!_hasHydrated) {
    return <Loader />;
  }

  useEffect(() => {
    if (isAuthenticated) {
      navigate({ to: "/dashboard" });
    }
  }, [isAuthenticated]);

  return (
    <div className="h-screen w-screen overflow-hidden flex flex-col gap-2 items-center justify-center relative">
      <p className="text-sm font-mono"> Welcome to </p>
      <div className="w-2xl bg-accent border rounded-xl p-8 flex flex-col gap-12 items-center justify-center">
        <div className="flex flex-col items-center justify-center gap-2">
          <div className="flex flex-row  items-center gap-2">
            <Activity size={24} />
            <h1 className="text-[48px] font-mono">Synap</h1>
          </div>
          <p className="font-mono">
            An AI Powered platform designed for students
          </p>
        </div>
        <div className="flex flex-col items-center justify-center gap-4">
          <h1 className="text-lg font-bold font-mono"> Get Started: </h1>
          <div className="flex flex-row gap-4 items-center">
            <Button variant={"default"} asChild>
              <Link to="/login">
                <LogIn />
                Login
              </Link>
            </Button>
            <Button variant={"outline"} asChild>
              <Link to="/register">
                <NotepadText />
                Register
              </Link>
            </Button>
          </div>
        </div>
      </div>
      <div className="absolute left-auto right-auto bottom-8">
        <a href="https://github.com/m1thrandir225/synap" target="_blank">
          <Github />
        </a>
      </div>
    </div>
  );
}
