import { useTheme } from "@/hooks/use-theme";
import MDEditor from "@uiw/react-md-editor";
import { useState } from "react";
import rehypeSanitize from "rehype-sanitize";

const NoteEditor: React.FC = () => {
  const { theme } = useTheme();
  const [value, setValue] = useState<string | undefined>(undefined);

  return (
    <div data-color-mode={theme}>
      <MDEditor
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
