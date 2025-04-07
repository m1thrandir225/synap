import { create } from "zustand";
import { persist } from "zustand/middleware";
import type { AuthStore } from "~/types/stores/auth";

export const useAuthStore = create<AuthStore>()(
  persist(
    (set) => ({
      user: null,
      accessToken: null,
      accessTokenExpiresAt: null,
      refreshToken: null,
      refreshTokenExpiresAt: null,
    }),
    { name: "auth-storage" },
  ),
);
