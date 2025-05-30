import RegisterForm from "@/components/auth/RegisterForm";
import authService from "@/services/auth.service";
import { useAuthStore } from "@/stores/auth.store";
import type { RegisterRequest } from "@/types/responses/auth";
import { useMutation } from "@tanstack/react-query";
import { createFileRoute, Link, useRouter } from "@tanstack/react-router";
import { Activity } from "lucide-react";
import { toast } from "sonner";

export const Route = createFileRoute("/(auth)/register")({
  component: RouteComponent,
});

function RouteComponent() {
  const authStore = useAuthStore();
  const router = useRouter();
  const { mutateAsync, status } = useMutation({
    mutationKey: ["register"],
    mutationFn: (input: RegisterRequest) => authService.register(input),
    onSuccess: (response) => {
      authStore.login(response);

      toast.success("Welcome to Synap!");
      router.navigate({
        to: "/dashboard",
        replace: true,
      });
    },
    onError: (error) => {
      toast.error(`Error: ${error.message}`);
    },
  });
  return (
    <div className="flex min-h-svh flex-col items-center justify-center gap-6 bg-muted p-6 md:p-10">
      <div className="flex w-full max-w-sm flex-col gap-6">
        <Link
          to="/"
          className="flex items-center gap-2 self-center font-mono font-medium"
        >
          <Activity />
          Synap
        </Link>
        <RegisterForm
          submitValues={async (input) => {
            mutateAsync(input);
          }}
          isLoading={status === "pending"}
        />
      </div>
    </div>
  );
}
