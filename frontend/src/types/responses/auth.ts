import type { User } from "../models/user";

export type LoginResponse = {
  access_token: string;
  token_type: string;
  user: User;
};
