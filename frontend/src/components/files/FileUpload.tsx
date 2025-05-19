import * as React from "react";
import { useCallback, useEffect, useState } from "react";
import {
  X,
  Upload,
  FileIcon,
  CheckCircle,
  AlertCircle,
  Presentation,
  FileTextIcon,
} from "lucide-react";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";

export type FileWithPreview = {
  file: File;
  preview?: string;
  progress?: number;
  error?: string;
  uploaded?: boolean;
};

type FileUploadProps = {
  value?: File[];
  onChange?: (files: File[]) => void;
  onUpload?: (file: File) => Promise<string | void>;
  accept?: string;
  multiple?: boolean;
  maxSize?: number; // in MB
  maxFiles?: number;
  disabled?: boolean;
  className?: string;
};

export function FileUpload({
  value,
  onChange,
  onUpload,
  accept = ".pdf,.doc,.docx,.ppt,.pptx",
  multiple = false,
  maxSize = 50, // 50MB
  maxFiles = 5,
  disabled = false,
  className,
}: FileUploadProps) {
  const [files, setFiles] = useState<FileWithPreview[]>([]);
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = React.useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (value) {
      const newFiles = value.map((file) => ({
        file,
        preview: file.type.startsWith("image/")
          ? URL.createObjectURL(file)
          : undefined,
      }));
      setFiles(newFiles);
    }
  }, [value]);

  useEffect(() => {
    return () => {
      files.forEach((file) => {
        if (file.preview) {
          URL.revokeObjectURL(file.preview);
        }
      });
    };
  }, [files]);

  const handleFiles = useCallback(
    async (newFiles: File[]) => {
      if (disabled) return;

      const acceptedExtensions = accept
        .split(",")
        .map((ext) => ext.trim().toLowerCase());
      const extensionValidatedFiles: File[] = [];
      const rejectedForExtension: string[] = [];

      newFiles.forEach((file) => {
        const fileName = file.name || "";
        const extensionParts = fileName.split(".");
        // Ensure there's an actual extension part after the dot
        const fileExtension =
          extensionParts.length > 1
            ? `.${extensionParts.pop()?.toLowerCase()}`
            : "";

        if (fileExtension && acceptedExtensions.includes(fileExtension)) {
          extensionValidatedFiles.push(file);
        } else {
          rejectedForExtension.push(fileName || "Unnamed file");
        }
      });

      if (rejectedForExtension.length > 0) {
        alert(
          `The following files have unsupported extensions and were not added: ${rejectedForExtension.join(", ")}.\nAccepted extensions: ${accept}`,
        );
      }

      if (extensionValidatedFiles.length === 0 && newFiles.length > 0) {
        return;
      }

      const validFiles = newFiles.filter(
        (file) => file.size <= maxSize * 1024 * 1024,
      );

      if (multiple && files.length + validFiles.length > maxFiles) {
        alert(`You can only upload up to ${maxFiles} files.`);
        return;
      }

      const filesWithPreviews = validFiles.map((file) => ({
        file,
        preview: undefined,
        progress: 0,
      }));

      const updatedFiles = multiple
        ? [...files, ...filesWithPreviews]
        : filesWithPreviews;

      setFiles(updatedFiles);

      if (onChange) {
        onChange(updatedFiles.map((f) => f.file));
      }

      if (onUpload) {
        for (let i = 0; i < filesWithPreviews.length; i++) {
          const fileWithPreview = filesWithPreviews[i];

          try {
            const updateProgress = (progress: number) => {
              setFiles((currentFiles) => {
                return currentFiles.map((f) => {
                  if (f.file === fileWithPreview.file) {
                    return { ...f, progress };
                  }
                  return f;
                });
              });
            };

            const progressInterval = setInterval(() => {
              setFiles((currentFiles) => {
                return currentFiles.map((f) => {
                  if (
                    f.file === fileWithPreview.file &&
                    f.progress !== undefined &&
                    f.progress < 90
                  ) {
                    return { ...f, progress: f.progress + 10 };
                  }
                  return f;
                });
              });
            }, 300);

            // Actual upload
            await onUpload(fileWithPreview.file);

            clearInterval(progressInterval);

            setFiles((currentFiles) => {
              return currentFiles.map((f) => {
                if (f.file === fileWithPreview.file) {
                  return { ...f, progress: 100, uploaded: true };
                }
                return f;
              });
            });
          } catch (error) {
            setFiles((currentFiles) => {
              return currentFiles.map((f) => {
                if (f.file === fileWithPreview.file) {
                  return {
                    ...f,
                    error:
                      error instanceof Error ? error.message : "Upload failed",
                    progress: undefined,
                  };
                }
                return f;
              });
            });
          }
        }
      }
    },
    [disabled, files, maxFiles, maxSize, multiple, onChange, onUpload],
  );

  const handleDragOver = useCallback(
    (e: React.DragEvent<HTMLDivElement>) => {
      e.preventDefault();
      e.stopPropagation();
      if (!disabled) {
        setIsDragging(true);
      }
    },
    [disabled],
  );

  const handleDragLeave = useCallback((e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
  }, []);

  const handleDrop = useCallback(
    (e: React.DragEvent<HTMLDivElement>) => {
      e.preventDefault();
      e.stopPropagation();
      setIsDragging(false);

      if (disabled) return;

      const droppedFiles = Array.from(e.dataTransfer.files);
      handleFiles(droppedFiles);
    },
    [disabled, handleFiles],
  );

  const handleFileInputChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      if (e.target.files && e.target.files.length > 0) {
        const selectedFiles = Array.from(e.target.files);
        handleFiles(selectedFiles);

        // Reset the input value so the same file can be selected again
        if (fileInputRef.current) {
          fileInputRef.current.value = "";
        }
      }
    },
    [handleFiles],
  );

  const removeFile = useCallback(
    (fileToRemove: FileWithPreview) => {
      setFiles((currentFiles) => {
        const updatedFiles = currentFiles.filter(
          (f) => f.file !== fileToRemove.file,
        );

        // Call onChange with the updated raw File objects
        if (onChange) {
          onChange(updatedFiles.map((f) => f.file));
        }

        // Revoke the preview URL to avoid memory leaks
        if (fileToRemove.preview) {
          URL.revokeObjectURL(fileToRemove.preview);
        }

        return updatedFiles;
      });
    },
    [onChange],
  );

  const openFileDialog = useCallback(() => {
    if (!disabled && fileInputRef.current) {
      fileInputRef.current.click();
    }
  }, [disabled]);

  const getFileIcon = (fileName: string) => {
    const extension = fileName.split(".").pop()?.toLowerCase();

    switch (extension) {
      case "pdf":
        return <FileTextIcon className="h-6 w-6 text-red-500" />;
      case "doc":
      case "docx":
        return <FileIcon className="h-6 w-6 text-blue-500" />;
      case "ppt":
      case "pptx":
        return <Presentation className="h-6 w-6 text-orange-500" />;
      default:
        return <FileIcon className="h-6 w-6" />;
    }
  };

  return (
    <div className={cn("space-y-4", className)}>
      <div
        className={cn(
          "relative flex flex-col items-center justify-center rounded-lg border-2 border-dashed p-6 transition-colors",
          isDragging
            ? "border-primary bg-primary/5"
            : "border-muted-foreground/25",
          disabled && "cursor-not-allowed opacity-60",
          "hover:border-primary/50",
        )}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onClick={openFileDialog}
      >
        <input
          ref={fileInputRef}
          type="file"
          accept={accept}
          multiple={multiple}
          className="sr-only"
          onChange={handleFileInputChange}
          disabled={disabled}
        />

        <div className="flex flex-col items-center justify-center space-y-2 text-center">
          <div className="flex h-12 w-12 items-center justify-center rounded-full bg-primary/10">
            <Upload className="h-6 w-6 text-primary" />
          </div>
          <div className="flex flex-col space-y-1">
            <p className="text-sm font-medium">
              Drag & drop files here, or click to select files
            </p>
            <p className="text-xs text-muted-foreground">
              {multiple
                ? `Upload up to ${maxFiles} files (max ${maxSize}MB each)`
                : `Upload a file (max ${maxSize}MB)`}
            </p>
            <p className="text-xs text-muted-foreground">
              Accepts: PDF, DOC, DOCX, PPT, PPTX (max {maxSize}MB)
            </p>
          </div>
        </div>
      </div>

      {files.length > 0 && (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {files.map((fileWithPreview, index) => (
            <div
              key={`${fileWithPreview.file.name}-${index}`}
              className="relative flex flex-col overflow-hidden rounded-lg border bg-background"
            >
              <div className="flex items-center justify-between border-b p-2">
                <div className="flex items-center space-x-2 truncate">
                  <div className="h-6 w-6 shrink-0">
                    {getFileIcon(fileWithPreview.file.name)}
                  </div>
                  <span className="truncate text-sm">
                    {fileWithPreview.file.name}
                  </span>
                </div>
                <Button
                  type="button"
                  variant="ghost"
                  size="icon"
                  className="h-7 w-7"
                  onClick={(e) => {
                    e.stopPropagation();
                    removeFile(fileWithPreview);
                  }}
                  disabled={disabled}
                >
                  <X className="h-4 w-4" />
                  <span className="sr-only">Remove file</span>
                </Button>
              </div>

              <div className="p-4 text-sm">
                <p>
                  <strong>Size:</strong>{" "}
                  {(fileWithPreview.file.size / (1024 * 1024)).toFixed(2)} MB
                </p>
                <p>
                  <strong>Type:</strong>{" "}
                  {fileWithPreview.file.type || "Unknown"}
                </p>
              </div>

              {fileWithPreview.progress !== undefined && (
                <div className="p-2">
                  <Progress value={fileWithPreview.progress} className="h-2" />
                </div>
              )}

              {fileWithPreview.uploaded && (
                <div className="absolute bottom-2 right-2 rounded-full bg-background p-1">
                  <CheckCircle className="h-5 w-5 text-green-500" />
                </div>
              )}

              {fileWithPreview.error && (
                <div className="p-2 text-xs text-red-500 flex items-center space-x-1">
                  <AlertCircle className="h-4 w-4" />
                  <span>{fileWithPreview.error}</span>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
