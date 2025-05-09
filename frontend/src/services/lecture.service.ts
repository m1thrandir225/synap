import config from "@/lib/config";
import { apiRequest } from "./api.service";
import type { Lecture } from "@/types/models/lecture";

const lectureURL = `${config.apiUrl}/lectures`;

export const lectureService = {
  getLectures: () =>
    apiRequest<Lecture[]>({
      url: lectureURL,
      method: "GET",
      protected: true,
      headers: undefined,
      params: undefined,
    }),
  createLecture: () =>
    apiRequest<Lecture>({
      url: lectureURL,
      method: "POST",
      protected: true,
      headers: undefined,
      params: undefined,
    }),
  getLecture: (id: string) =>
    apiRequest<Lecture>({
      url: `${lectureURL}/${id}`,
      method: "GET",
      protected: true,
      headers: undefined,
      params: undefined,
    }),
  updateLecture: (id: string) =>
    apiRequest<Lecture>({
      url: `${lectureURL}/${id}`,
      method: "PUT",
      protected: true,
      headers: undefined,
      params: undefined,
    }),
  deleteLecture: (id: string) =>
    apiRequest<boolean>({
      url: `${lectureURL}/${id}`,
      protected: true,
      method: "DELETE",
      headers: undefined,
      params: undefined,
    }),
};
