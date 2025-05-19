import type { UploadedFile } from "@/types/models/uploaded-file";
import { ScrollArea } from "../ui/scroll-area";
import SummarizationForm from "../summarizations/SummarizationForm";
import FileDownload from "./FileDownload";

interface ComponentProps {
  items: UploadedFile[];
}

const UploadedFileList: React.FC<ComponentProps> = (props) => {
  const { items } = props;

  return (
    <ScrollArea className="max-h-[500px]  h-auto w-full">
      {items.map((item) => (
        <div className="w-full border py-4 my-2 px-4 rounded-md flex flex-row items-center justify-between">
          <p>{item.file_name}</p>
          <div className="flex flex-row items-center gap-4">
            <SummarizationForm file_id={item.id} />
            <FileDownload id={item.id} text="Download" />
          </div>
        </div>
      ))}
    </ScrollArea>
  );
};
export default UploadedFileList;
