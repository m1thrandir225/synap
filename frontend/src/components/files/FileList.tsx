import type { UploadedFile } from "@/types/models/uploaded-file";
import {
  flexRender,
  getCoreRowModel,
  getPaginationRowModel,
  useReactTable,
  type ColumnDef,
} from "@tanstack/react-table";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuTrigger,
} from "../ui/dropdown-menu";
import { Button } from "../ui/button";
import { MoreHorizontal } from "lucide-react";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "../ui/table";
import { TablePagination } from "../table/TablePagination";
import { formatBytesToMb } from "@/lib/utils";
import fileService from "@/services/files.service";
import { toast } from "sonner";
import queryClient from "@/lib/queryClient";

const columns: ColumnDef<UploadedFile>[] = [
  {
    accessorKey: "file_name",
    header: "Name",
  },
  {
    accessorKey: "file_size",
    header: "Size",
    cell: ({ row }) => {
      const file_size = row.original.file_size;

      return <span>{formatBytesToMb(file_size)}</span>;
    },
  },

  {
    id: "actions",
    cell: ({ row }) => {
      const uploaded_file = row.original;
      const deleteFile = async () => {
        try {
          const response = await fileService.deleteFile(uploaded_file.id);
          toast.success(response.message);
          queryClient.invalidateQueries({
            queryKey: ["files"],
          });
        } catch (e) {
          toast.error(`Error: ${e}`);
        }
      };
      return (
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant={"ghost"} className="h-8 w-8 p-0">
              <span className="sr-only"> Open Menu </span>
              <MoreHorizontal className="h-4 w-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuLabel> Actions </DropdownMenuLabel>
            <DropdownMenuItem onClick={deleteFile}>Delete</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      );
    },
  },
];

interface ComponentProps {
  items: UploadedFile[];
}

const FileList: React.FC<ComponentProps> = ({ items }) => {
  const table = useReactTable({
    data: items,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
  });

  return (
    <div>
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            {table.getHeaderGroups().map((headerGroup) => (
              <TableRow key={headerGroup.id}>
                {headerGroup.headers.map((header) => {
                  return (
                    <TableHead key={header.id}>
                      {header.isPlaceholder
                        ? null
                        : flexRender(
                            header.column.columnDef.header,
                            header.getContext(),
                          )}
                    </TableHead>
                  );
                })}
              </TableRow>
            ))}
          </TableHeader>
          <TableBody>
            {table.getRowModel().rows?.length ? (
              table.getRowModel().rows.map((row) => (
                <TableRow
                  key={row.id}
                  data-state={row.getIsSelected() && "selected"}
                >
                  {row.getVisibleCells().map((cell) => (
                    <TableCell key={cell.id}>
                      {flexRender(
                        cell.column.columnDef.cell,
                        cell.getContext(),
                      )}
                    </TableCell>
                  ))}
                </TableRow>
              ))
            ) : (
              <TableRow>
                <TableCell
                  colSpan={columns.length}
                  className="h-24 text-center"
                >
                  No results.
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </div>
      <TablePagination table={table} />
    </div>
  );
};

export default FileList;
