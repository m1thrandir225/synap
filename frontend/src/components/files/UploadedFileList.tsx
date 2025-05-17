import type { UploadedFile } from "@/types/models/uploaded-file";
import { ScrollArea } from "../ui/scroll-area";
import { Button } from "../ui/button";
import { Download, Stars } from "lucide-react";
import {
  Dialog,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
  DialogContent,
} from "../ui/dialog";
import { useMutation } from "@tanstack/react-query";
import summarizationService from "@/services/summarization.service";
import type { CreateSummarizationRequest } from "@/types/responses/summarization";
import SummarizationForm from "../summarizations/SummarizationForm";

interface ComponentProps {
  items: UploadedFile[];
}

const UploadedFileList: React.FC<ComponentProps> = (props) => {
  const { items } = props;

  return (
    <ScrollArea className="max-h-[500px] h-auto w-full">
      {items.map((item) => (
        <div className="w-full border  py-4 px-4 rounded-md flex flex-row items-center justify-between">
          <p>{item.file_name}</p>
          <div className="flex flex-row items-center gap-4">
            <SummarizationForm file_id={item.id} />
            <Button variant={"outline"}>
              <Download />
              Download
            </Button>
          </div>
        </div>
      ))}
    </ScrollArea>
  );
};
export default UploadedFileList;
