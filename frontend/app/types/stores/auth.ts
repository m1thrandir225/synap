export type AuthStore = {
  user: Object | null;
  accessToken: string | null;
  accessTokenExpiresAt: Date | null;
  refreshToken: string | null;
  refreshTokenExpiresAt: Date | null;
};
