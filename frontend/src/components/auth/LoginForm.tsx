import { Link } from "@tanstack/react-router";
import { Button } from "../ui/button";
import { Input } from "../ui/input";
import { Label } from "../ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "../ui/card";
import { cn } from "@/lib/utils";
import { useForm } from "react-hook-form";
import * as z from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "../ui/form";

const loginFormSchema = z.object({
  username: z.string().email(),
  password: z.string(),
});

type LoginFormSchemaType = z.infer<typeof loginFormSchema>;

interface ComponentProps extends React.ComponentPropsWithoutRef<"div"> {
  submitValues: (values: LoginFormSchemaType) => Promise<void>;
}

const LoginForm: React.FC<ComponentProps> = ({
  submitValues,
  className,
  ...props
}) => {
  const form = useForm<LoginFormSchemaType>({
    resolver: zodResolver(loginFormSchema),
  });

  async function onSubmit(values: LoginFormSchemaType) {
    try {
      await submitValues(values);
    } catch (e: any) {
      throw new Error(e.message);
    }
  }
  return (
    <div className={cn("flex flex-col gap-6", className)} {...props}>
      <Card>
        <CardHeader className="text-center">
          <CardTitle className="text-xl">Welcome back</CardTitle>
        </CardHeader>
        <CardContent>
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)}>
              <div className="grid gap-6">
                <div className="grid gap-6">
                  <div className="grid gap-2">
                    <FormField
                      control={form.control}
                      name="username"
                      render={({ field }) => (
                        <FormItem>
                          <FormLabel> Email </FormLabel>
                          <FormControl>
                            <Input {...field} placeholder="m@example.com" />
                          </FormControl>
                          <FormMessage />
                        </FormItem>
                      )}
                    />
                  </div>
                  <div className="grid gap-2">
                    <FormField
                      control={form.control}
                      name="password"
                      render={({ field }) => (
                        <FormItem>
                          <FormLabel className="flex items-center">
                            Password
                          </FormLabel>
                          <FormControl>
                            <Input
                              {...field}
                              type="password"
                              placeholder="m@example.com"
                            />
                          </FormControl>
                          <FormMessage />
                        </FormItem>
                      )}
                    />
                  </div>
                  <Button type="submit" className="w-full">
                    Login
                  </Button>
                </div>
                <div className="text-center text-sm">
                  Don&apos;t have an account?{" "}
                  <Link to="/register" className="underline underline-offset-4">
                    Sign up
                  </Link>
                </div>
              </div>
            </form>
          </Form>
        </CardContent>
      </Card>
    </div>
  );
};

export default LoginForm;
