export type AuthStore = {
  //State
  user: Object | null;
  accessToken: string | null;
  accessTokenExpiresAt: number | null;
  isAuthenticated: boolean | null;
  _hasHydrated: boolean;

  //State Actions
  setTokens: (accessToken: string, expiresIn: number) => void;
  setUser: (user: Object | null) => void;
  logout: () => void;
  checkAuth: () => void;
  setHasHydrated: (state: boolean) => void;
};
