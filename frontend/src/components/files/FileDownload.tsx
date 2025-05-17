import { Download, Loader2 } from "lucide-react";
import { Button } from "../ui/button";
import { Fragment, useState } from "react";
import fileService from "@/services/files.service";

interface ComponentProps {
  filename: string;
  text: string;
}

const FileDownload: React.FC<ComponentProps> = (props) => {
  const { filename, text } = props;
  const [isLoading, setIsLoading] = useState<boolean>(false);
  async function downloadFile() {
    try {
      setIsLoading(true);
      const blob = await fileService.downloadFile(filename);

      const url = window.URL.createObjectURL(blob);

      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", filename);

      document.body.appendChild(link);
      link.click();
      console.log("Download initiated for:", filename);

      link.parentNode?.removeChild(link);
      window.URL.revokeObjectURL(url);
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
