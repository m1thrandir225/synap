import { useTheme } from "@/hooks/use-theme";
import { cn } from "@/lib/utils";
import MDEditor from "@uiw/react-md-editor";
import { useState } from "react";
import rehypeSanitize from "rehype-sanitize";

interface ComponentProps extends React.ComponentPropsWithoutRef<"div"> {
  onlyPreview?: boolean;
  contentValue: string | undefined;
  setContentValue: React.Dispatch<React.SetStateAction<string | undefined>>;
}

const NoteEditor: React.FC<ComponentProps> = ({
  contentValue,
  setContentValue,
  className,
  ...props
}) => {
  const { theme } = useTheme();
  return (
    <div data-color-mode={theme} className={cn(className)} {...props}>
      <MDEditor
        className="w-full !h-full"
        value={contentValue}
        onChange={setContentValue}
        previewOptions={{
          rehypePlugins: [[rehypeSanitize]],
        }}
      />
    </div>
  );
};

export default NoteEditor;
