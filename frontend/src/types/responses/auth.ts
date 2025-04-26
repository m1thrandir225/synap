import type { User } from "../models/user";

export type LoginRequest = {
  username: string;
  password: string;
};

export type LoginResponse = {
  access_token: string;
  token_type: string;
  user: User;
};

export type RegisterRequest = {
  first_name: string;
  last_name: string;
  email: string;
  password: string;
};

export type RegisterResponse = LoginResponse & {};
