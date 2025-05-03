import { useTheme } from "@/hooks/use-theme";
import { cn } from "@/lib/utils";
import MDEditor from "@uiw/react-md-editor";

interface ComponentProps extends React.ComponentPropsWithoutRef<"div"> {
  content: string;
}

const NotePreview: React.FC<ComponentProps> = ({
  className,
  content,
  ...props
}) => {
  const { theme } = useTheme();
  return (
    <div data-color-mode={theme} className={cn(className, "w-full")} {...props}>
      <MDEditor.Markdown source={content} />
    </div>
  );
};

export default NotePreview;
