import { PackageOpen } from "lucide-react";

const ListEmpty: React.FC = () => {
  return (
    <div className="flex flex-row items-start gap-4 text-sm text-neutral-400">
      <PackageOpen />
      <p>No items found </p>
    </div>
  );
};

export default ListEmpty;
