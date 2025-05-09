import { FileUpload } from "@/components/files/FileUpload";
import fileService from "@/services/files.service";
import type { UploadFileRequest } from "@/types/responses/files";
import { useMutation } from "@tanstack/react-query";
import { createFileRoute, useRouter } from "@tanstack/react-router";
import { useState } from "react";

export const Route = createFileRoute("/dashboard/courses/$courseId/upload")({
  component: RouteComponent,
  loader: () => {
    return {
      crumb: "Upload File",
    };
  },
});

function RouteComponent() {
  const { courseId } = Route.useParams();
  const [files, setFiles] = useState<File[]>([]);
  const router = useRouter();
  const { status, mutateAsync } = useMutation({
    mutationKey: ["upload-file"],
    mutationFn: (input: UploadFileRequest) => fileService.uploadFile(input),
    onSuccess: () => {
      router.navigate({
        to: "/dashboard/courses/$courseId",
        params: { courseId },
      });
    },
  });

  const handleUpload = async (file: File): Promise<void> => {
    try {
      await mutateAsync({
        file,
        course_id: courseId,
      });
    } catch (err: any) {
      throw err;
    }
  };

  return (
    <main className="container mx-auto py-10 px-4">
      <div className="mx-auto max-w-3xl space-y-6">
        <div className="space-y-2 text-center">
          <h1 className="text-3xl font-bold">Document Upload</h1>
          <p className="text-muted-foreground">
            Upload a document file (PDF, DOC, DOCX, PPT, PPTX) up to 50MB
          </p>
        </div>

        <div className="rounded-lg border bg-card p-6 shadow-sm">
          <FileUpload
            value={files}
            onChange={setFiles}
            onUpload={handleUpload}
            maxSize={50}
            multiple={false}
            accept=".pdf,.doc,.docx,.ppt,.pptx"
          />
        </div>

        {files.length > 0 && (
          <div className="rounded-lg border bg-card p-6 shadow-sm">
            <h2 className="text-xl font-semibold mb-4">Selected Document</h2>
            <div className="space-y-2">
              {files.map((file, index) => {
                const extension = file.name.split(".").pop()?.toLowerCase();
                const fileType =
                  {
                    pdf: "PDF Document",
                    doc: "Word Document",
                    docx: "Word Document",
                    ppt: "PowerPoint Presentation",
                    pptx: "PowerPoint Presentation",
                  }[extension || ""] || "Document";

                return (
                  <div key={index} className="rounded-lg border p-4">
                    <p className="font-medium">{file.name}</p>
                    <p className="text-sm text-muted-foreground">
                      Type: {fileType}
                    </p>
                    <p className="text-sm text-muted-foreground">
                      Size: {(file.size / (1024 * 1024)).toFixed(2)} MB
                    </p>
                  </div>
                );
              })}
            </div>
          </div>
        )}
      </div>
    </main>
  );
}
