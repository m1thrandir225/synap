import type { User } from "../models/user";
import type { LoginResponse } from "../responses/auth";

export type AuthStore = {
  //State
  user: User | null;
  accessToken: string | null;
  accessTokenExpiresAt: number | null;
  isAuthenticated: boolean | null;
  _hasHydrated: boolean;

  //State Actions
  login: (input: LoginResponse) => void;
  setTokens: (accessToken: string, expiresIn: number) => void;
  setUser: (user: User) => void;
  logout: () => void;
  checkAuth: () => Promise<void>;
  setHasHydrated: (state: boolean) => void;
};
