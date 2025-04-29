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
import { Textarea } from "../ui/textarea";
import { Button } from "../ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "../ui/card";
const courseFormSchema = z.object({
  name: z.string(),
  content: z.string(),
});

type CourseFormSchemaType = z.infer<typeof courseFormSchema>;

interface ComponentProps {
  defaultValues?: CourseFormSchemaType;
  title: string;
  description: string;
  submitValues: (input: CourseFormSchemaType) => Promise<void>;
}

const CourseForm: React.FC<ComponentProps> = ({
  defaultValues,
  submitValues,
  title,
  description,
}) => {
  const form = useForm<CourseFormSchemaType>({
    resolver: zodResolver(courseFormSchema),
    defaultValues,
  });

  async function onSubmit(values: CourseFormSchemaType) {
    try {
      await submitValues(values);
    } catch (e: unknown) {
      throw e;
    }
  }
  return (
    <Card className="w-full max-w-[550px]">
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        <CardDescription>{description}</CardDescription>
      </CardHeader>
      <CardContent>
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

            <div className="grid gap-2">
              <FormField
                control={form.control}
                name="content"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel> Content </FormLabel>
                    <FormControl>
                      <Textarea {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
            </div>
            <Button type="submit" size={"default"} variant={"outline"}>
              Submit
            </Button>
          </form>
        </Form>
      </CardContent>
    </Card>
  );
};

export default CourseForm;
