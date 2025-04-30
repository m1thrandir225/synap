export type CreateCourseRequest = {
  name: string;
  content: string;
};

export type CreateCourseResponse = {};

export type EditCourseRequest = CreateCourseRequest & {
  id: string;
};

export type EditCourseResponse = CreateCourseResponse & {};
