export type LearningMaterial = {
  id: string;
  title: string;
  description: string;
  url: string;
  material_type: "video" | "article";
  created_at: string;
};
