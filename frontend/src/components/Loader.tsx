import { cn } from "@/lib/utils";
import { GraduationCap } from "lucide-react";

const Loader: React.FC<React.ComponentPropsWithoutRef<"div">> = ({
  className,
  ...props
}) => {
  return (
    <div
      className={cn(
        className,
        "min-h-screen min-w-screen w-full h-full flex items-center justify-center bg-secondary",
      )}
      {...props}
    >
      <GraduationCap
        width={128}
        height={128}
        className="text-primary animate-bounce"
      />
    </div>
  );
};

export default Loader;
