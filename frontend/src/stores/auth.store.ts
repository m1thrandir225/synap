import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";
import type { AuthStore } from "@/types/stores/auth";

export const useAuthStore = create<AuthStore>()(
  persist(
    (set, get) => ({
      user: null,
      accessToken: null,
      refreshToken: null,
      accessTokenExpireTime: null,
      refreshTokenExpireTime: null,
      isAuthenticated: null,

      login: (input) => {
        set({
          accessToken: input.access_token,
          user: input.user,
          refreshToken: input.refresh_token,
          accessTokenExpireTime: new Date(input.access_token_expire_time),
          refreshTokenExpireTime: new Date(input.refresh_token_expire_time),
          isAuthenticated: true,
        });
      },

      setUser: (user) => {
        set({ user, isAuthenticated: !!user });
      },
      logout: () => {
        set({
          user: null,
          isAuthenticated: null,
          accessToken: null,
        });
      },

      checkAuth: () => {
        const now = new Date();

        const refreshTokenExpireTime = get().refreshTokenExpireTime;
        const refreshToken = get().refreshToken;

        if (
          !refreshToken ||
          !refreshTokenExpireTime ||
          now > refreshTokenExpireTime
        ) {
          get().logout();
          return false;
        }

        return true;
      },

      //Store hydration from storage
      _hasHydrated: false,
      setHasHydrated: (state) => {
        set({
          _hasHydrated: state,
        });
      },
    }),
    {
      name: "auth-storage",
      storage: createJSONStorage(() => localStorage),
      onRehydrateStorage: (state) => {
        return () => state.setHasHydrated(true);
      },
    },
  ),
);
