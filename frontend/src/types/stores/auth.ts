import type { User } from "../models/user";
import type { LoginResponse } from "../responses/auth";

export type AuthStore = {
  //State
  user: User | null;
  accessToken: string | null;
  accessTokenExpireTime: Date | null;
  refreshToken: string | null;
  refreshTokenExpireTime: Date | null;
  isAuthenticated: boolean | null;
  _hasHydrated: boolean;

  //State Actions
  login: (input: LoginResponse) => void;
  setUser: (user: User) => void;
  logout: () => void;
  checkAuth: () => boolean;
  setHasHydrated: (state: boolean) => void;
};
