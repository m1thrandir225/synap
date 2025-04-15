type RequestOptions = {
  url: string;
  protected: boolean | undefined;
  headers: Record<string, string> | undefined;
  params: Record<string, string> | undefined;
};

export type ApiRequestOptions = RequestOptions & {
  method: "GET" | "POST" | "PUT" | "PATCH" | "DELETE";
  data?: Record<string, unknown>;
};

export type MultipartRequestOptions<T extends Record<string, unknown>> =
  RequestOptions & {
    method: "GET" | "POST";
    data: T;
  };
