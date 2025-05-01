import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function extractInitials(firstName: string, lastName: string): string {
  return `${firstName.charAt(0)} ${lastName.charAt(0)}`.toUpperCase();
}

export function formatDate(input: string): string {
  const date = new Date(input);

  return date.toLocaleDateString("en-US", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

export function formatBytesToMb(bytes: number): string {
  if (typeof bytes !== "number" || bytes < 0 || isNaN(bytes) || bytes === 0) {
    return "0.00 MB";
  }

  const bytesPerMB = 1024 * 1024;

  const megabytes = bytes / bytesPerMB;

  return `${megabytes.toFixed(2)} MB`;
}
