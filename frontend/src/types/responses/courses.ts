export type CreateCourseRequest = {
  name: string;
  description: string;
};

export type CreateCourseResponse = {};

export type EditCourseRequest = CreateCourseRequest & {
  id: string;
};

export type EditCourseResponse = CreateCourseResponse & {};
