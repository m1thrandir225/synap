import config from "@/lib/config";
import { apiRequest } from "./api.service";
import type { Course } from "@/types/models/course";
import type {
  CreateCourseRequest,
  EditCourseRequest,
} from "@/types/responses/courses";

const coursesURL = `${config.apiUrl}/courses`;

const coursesServices = {
  getCoursesForUser: () =>
    apiRequest<Course[]>({
      url: `${coursesURL}/user`,
      method: "GET",
      protected: true,
      headers: undefined,
      params: undefined,
    }),
  getCourseById: (id: string) =>
    apiRequest<Course>({
      url: `${coursesURL}/${id}`,
      method: "GET",
      protected: true,
      headers: undefined,
      params: undefined,
    }),
  createCourse: (input: CreateCourseRequest) =>
    apiRequest<Course>({
      url: `${coursesURL}`,
      method: "POST",
      headers: undefined,
      protected: true,
      params: undefined,
      data: input,
    }),
  editCourse: (input: EditCourseRequest) =>
    apiRequest<Course>({
      url: `${coursesURL}/${input.id}`,
      method: "PUT",
      headers: undefined,
      protected: true,
      params: undefined,
      data: input,
    }),
  deleteCourse: (id: string) =>
    apiRequest<Course>({
      url: `${coursesURL}/${id}`,
      method: "DELETE",
      headers: undefined,
      protected: true,
      params: undefined,
      data: undefined,
    }),
};

export default coursesServices;
