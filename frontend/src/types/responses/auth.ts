import type { User } from "../models/user";

export type LoginRequest = {
  username: string;
  password: string;
};

export type LoginResponse = {
  access_token: string;
  access_token_expire_time: string;
  refresh_token: string;
  refresh_token_expire_time: string;
  user: User;
};

export type RegisterRequest = {
  first_name: string;
  last_name: string;
  email: string;
  password: string;
};

export type RegisterResponse = LoginResponse & {};

export type RefreshTokenResponse = LoginResponse & {};

export type LogoutResponse = {
  details: string;
};
