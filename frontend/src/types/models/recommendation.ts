import type { LearningMaterial } from "./learning-material";

export type Recommendation = {
  file_id: string;
  learning_material_id: string;
  id: string;
  created_at: string;
  learning_material: LearningMaterial;
};
