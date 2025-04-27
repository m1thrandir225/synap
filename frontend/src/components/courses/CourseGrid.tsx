import type { Course } from "@/types/models/course";
import CourseCard from "./CourseCard";

interface ComponentProps extends React.ComponentPropsWithoutRef<"div"> {
  items: Course[];
}

const CourseGrid: React.FC<ComponentProps> = ({ items, ...props }) => {
  return (
    <div className="w-full gap-12 grid lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-2 grid-cols-1">
      {items.map((course) => (
        <CourseCard course={course} key={course.id} />
      ))}
    </div>
  );
};
export default CourseGrid;
