import { Loader2, Trash } from "lucide-react";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "../ui/alert-dialog";
import { Button } from "../ui/button";
import { useMutation } from "@tanstack/react-query";
import coursesServices from "@/services/courses.service";
import { useState } from "react";
import queryClient from "@/lib/queryClient";
import { useRouter } from "@tanstack/react-router";
import { toast } from "sonner";

interface ComponentProps {
  courseId: string;
}

const CourseDeleteDialog: React.FC<ComponentProps> = (props) => {
  const [dialogActive, setDialogActive] = useState(false);
  const { courseId } = props;
  const router = useRouter();
  const { mutateAsync, status } = useMutation({
    mutationFn: async () => coursesServices.deleteCourse(courseId),
    onSuccess: () => {
      toast.success("Sucessfully deleted course!");
      setDialogActive(false);

      queryClient.invalidateQueries({ queryKey: ["courses"] });
      router.navigate({
        to: "/dashboard/courses",
      });
    },
    onError: (error) => {
      toast.error(`Error: ${error.message}`);
    },
  });

  const handleDelete = async () => {
    try {
      await mutateAsync();
    } catch (e) {
      throw e;
    }
  };
  return (
    <AlertDialog open={dialogActive} onOpenChange={setDialogActive}>
      <AlertDialogTrigger>
        <Button size={"icon"} variant={"destructive"}>
          <Trash />
        </Button>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>
            Are you sure you want to continue?
          </AlertDialogTitle>
          <AlertDialogDescription>
            There is no way to revert this action.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Cancel</AlertDialogCancel>
          <AlertDialogAction asChild>
            <Button disabled={status === "pending"} onClick={handleDelete}>
              {status === "pending" ? (
                <Loader2 className="animate-spin" />
              ) : (
                <p>Continue</p>
              )}
            </Button>
          </AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  );
};

export default CourseDeleteDialog;
