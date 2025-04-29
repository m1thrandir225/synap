import { useTheme } from "@/hooks/use-theme";
import { cn } from "@/lib/utils";
import MDEditor from "@uiw/react-md-editor";
import { useState } from "react";
import rehypeSanitize from "rehype-sanitize";

interface ComponentProps extends React.ComponentPropsWithoutRef<"div"> {
  onlyPreview?: boolean;
}

const NoteEditor: React.FC<ComponentProps> = ({ className, ...props }) => {
  const { theme } = useTheme();
  const [value, setValue] = useState<string | undefined>(undefined);
  return (
    <div data-color-mode={theme} className={cn(className)} {...props}>
      <MDEditor
        className="w-full !h-full"
        value={value}
        onChange={setValue}
        previewOptions={{
          rehypePlugins: [[rehypeSanitize]],
        }}
      />
    </div>
  );
};

export default NoteEditor;
