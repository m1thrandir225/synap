import LoginForm from "@/components/auth/LoginForm";
import authService from "@/services/auth.service";
import { useAuthStore } from "@/stores/auth.store";
import type { LoginRequest } from "@/types/responses/auth";
import { useMutation } from "@tanstack/react-query";
import {
  createFileRoute,
  Link,
  useRouter,
  useSearch,
} from "@tanstack/react-router";
import { Activity } from "lucide-react";
import { toast } from "sonner";
import * as z from "zod";

const loginSearchSchema = z.object({
  redirect: z.string().optional(),
});

export const Route = createFileRoute("/(auth)/login")({
  component: RouteComponent,
  validateSearch: loginSearchSchema,
});

function RouteComponent() {
  const authStore = useAuthStore();
  const { redirect } = useSearch({ strict: false });
  const router = useRouter();
  const { mutateAsync, status } = useMutation({
    mutationKey: ["login"],
    mutationFn: (input: LoginRequest) => authService.login(input),
    onSuccess: (response) => {
      authStore.login(response);

      toast.success("Welcome Back!");
      //Redirect to redirectRoute or to dashboard
      if (redirect && typeof redirect === "string") {
        const decodedRedirect = decodeURIComponent(redirect);
        router.navigate({ to: decodedRedirect, replace: true });
      } else {
        router.navigate({
          to: "/dashboard",
          replace: true,
        });
      }
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
          className="flex items-center gap-2 self-center font-medium font-mono"
        >
          <Activity />
          Synap
        </Link>
        <LoginForm
          submitValues={async (values) => {
            await mutateAsync(values);
          }}
          isLoading={status === "pending"}
        />
      </div>
    </div>
  );
}
