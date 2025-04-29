import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function extractInitials(firstName: string, lastName: string): string {
  return `${firstName.charAt(0)} ${lastName.charAt(0)}`.toUpperCase();
}
