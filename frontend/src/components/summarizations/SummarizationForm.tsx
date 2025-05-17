import { useForm } from "react-hook-form";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "../ui/form";
import * as z from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { Input } from "../ui/input";
import { Button } from "../ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../ui/dialog";
import { Loader2, Stars } from "lucide-react";
import { useMutation } from "@tanstack/react-query";
import summarizationService from "@/services/summarization.service";
import type { CreateSummarizationRequest } from "@/types/responses/summarization";
import { useState } from "react";
import queryClient from "@/lib/queryClient";
import { useParams, useRouter } from "@tanstack/react-router";

const createSummarizationSchema = z.object({
  name: z.string(),
});

type CreateSummarizationSchemaType = z.infer<typeof createSummarizationSchema>;

interface ComponentProps {
  file_id: string;
}

const SummarizationForm: React.FC<ComponentProps> = (props) => {
  const { file_id } = props;
  const { courseId } = useParams({ from: "/dashboard/courses/$courseId/" });

  const router = useRouter();
  const [dialogOpen, setDialogOpen] = useState(false);

  const { mutateAsync, status } = useMutation({
    mutationKey: ["create-summarization"],
    mutationFn: (input: CreateSummarizationRequest) =>
      summarizationService.createSummarization(input),
    onSuccess: (response) => {
      setDialogOpen(false);
      queryClient.invalidateQueries({
        queryKey: ["course", courseId],
      });
      router.navigate({
        to: "/dashboard/lectures/$summarizationId",
        params: { summarizationId: response.id },
      });
    },
  });
  const form = useForm({
    resolver: zodResolver(createSummarizationSchema),
  });

  async function onSubmit(values: CreateSummarizationSchemaType) {
    try {
      await mutateAsync({
        file_id: file_id,
        name: values.name,
      });
    } catch (e) {
      throw e;
    }
  }
  return (
    <Dialog open={dialogOpen} onOpenChange={setDialogOpen}>
      <DialogTrigger asChild>
        <Button variant={"outline"}>
          <Stars />
          Summarize
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle className="flex flex-row items-center gap-2">
            <Stars /> Create a lecture
          </DialogTitle>
          <DialogDescription>
            Give a name to the file that you want to create a summarization for.
          </DialogDescription>
        </DialogHeader>
        <Form {...form}>
          <form
            onSubmit={form.handleSubmit(onSubmit)}
            className="flex flex-col gap-4 w-full h-full"
          >
            <div className="grid gap-2">
              <FormField
                control={form.control}
                name="name"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel> Name </FormLabel>
                    <FormControl>
                      <Input {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
            </div>
            <Button
              type="submit"
              disabled={status === "pending"}
              size={"default"}
              variant={"outline"}
            >
              {status === "pending" ? (
                <Loader2 className="animate-spin" />
              ) : (
                <span>Submit</span>
              )}
            </Button>
          </form>
        </Form>
      </DialogContent>
    </Dialog>
  );
};

export default SummarizationForm;
