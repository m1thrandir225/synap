import type { Recommendation } from "@/types/models/recommendation";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "../ui/card";

import RecommendationCard from "./RecommendationCard";

interface ComponentProps {
  items: Recommendation[];
}

const RecommendationList: React.FC<ComponentProps> = (props) => {
  const { items } = props;

  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle>Recommendations: </CardTitle>
        <CardDescription>
          We recommend the following items to continue your learning journey
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="w-full grid grid-cols-4 gap-4">
          {items.map((item) => (
            <RecommendationCard item={item} />
          ))}
        </div>
      </CardContent>
    </Card>
  );
};

export default RecommendationList;
