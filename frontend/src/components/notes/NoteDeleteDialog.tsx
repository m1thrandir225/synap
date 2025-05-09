import { useMutation } from "@tanstack/react-query";
import { useState } from "react";
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
import { Loader2, Trash } from "lucide-react";
import noteServices from "@/services/note.service";
import queryClient from "@/lib/queryClient";
import { useRouter } from "@tanstack/react-router";

interface ComponentProps {
  noteId: string;
}

const NoteDeleteDialog: React.FC<ComponentProps> = (props) => {
  const [dialogActive, setDialogActive] = useState(false);
  const { noteId } = props;

  const router = useRouter();

  const { mutateAsync, status } = useMutation({
    mutationFn: async () => noteServices.deleteNote(noteId),
    onSuccess: (response) => {
      setDialogActive(false);

      queryClient.invalidateQueries({
        queryKey: ["notes"],
      });

      router.navigate({
        to: "/dashboard/notes",
      });
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
export default NoteDeleteDialog;
