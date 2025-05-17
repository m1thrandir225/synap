import type { Recommendation } from "@/types/models/recommendation";
import { Card, CardDescription, CardHeader, CardTitle } from "../ui/card";
import { capitalize } from "@/lib/utils";
import { Newspaper, Video } from "lucide-react";

interface ComponentProps {
  item: Recommendation;
}
const RecommendationCard: React.FC<ComponentProps> = (props) => {
  const { item } = props;
  return (
    <a
      target="_blank"
      href={item.learning_material.url}
      className="w-full group h-[220px]"
    >
      <Card className="w-full h-full overflow-hidden group-hover:border-neutral-400 transition-all ease-in-out duration-300">
        <CardHeader>
          <p className="flex flex-row items-center gap-2 text-[10px]">
            {item.learning_material.material_type === "article" ? (
              <Newspaper size={16} />
            ) : (
              <Video size={16} />
            )}
            {capitalize(item.learning_material.material_type)}
          </p>
          <CardTitle className="text-wrap">
            {item.learning_material.title}
          </CardTitle>
          <CardDescription>
            {item.learning_material.description}
          </CardDescription>
        </CardHeader>
      </Card>
    </a>
  );
};

export default RecommendationCard;
