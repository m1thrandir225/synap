import { Download, Loader2 } from "lucide-react";
import { Button } from "../ui/button";
import { Fragment, useState } from "react";
import fileService from "@/services/files.service";

interface ComponentProps {
  id: string;
  text: string;
}

const FileDownload: React.FC<ComponentProps> = (props) => {
  const { id, text } = props;
  const [isLoading, setIsLoading] = useState<boolean>(false);
  async function downloadFile() {
    try {
      setIsLoading(true);
      const file = await fileService.downloadFile(id);

      const link = document.createElement("a");
      link.href = file.url;
      link.setAttribute("download", file.filename);

      document.body.appendChild(link);
      link.click();
      console.log("Download initiated for:", file.filename);

      link.parentNode?.removeChild(link);
    } catch (e) {
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <Button disabled={isLoading} onClick={downloadFile} variant={"outline"}>
      {isLoading ? (
        <Loader2 className="animate-spin" />
      ) : (
        <Fragment>
          <Download />
          {text}
        </Fragment>
      )}
    </Button>
  );
};

export default FileDownload;
