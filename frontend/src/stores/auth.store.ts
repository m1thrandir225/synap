import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";
import type { AuthStore } from "@/types/stores/auth";
import authService from "@/services/auth.service";

export const useAuthStore = create<AuthStore>()(
  persist(
    (set, get) => ({
      user: null,
      accessToken: null,
      accessTokenExpiresAt: null,
      isAuthenticated: null,

      login: (input) => {
        set({
          accessToken: input.access_token,
          user: input.user,
          isAuthenticated: true,
        });
      },
      setTokens: (accessToken, expiresIn) => {
        const expiresAt = Date.now() + expiresIn * 1000;
        set({
          accessToken,
          accessTokenExpiresAt: expiresAt,
          isAuthenticated: true,
        });
      },
      setUser: (user) => {
        set({ user, isAuthenticated: !!user });
      },
      logout: () => {
        set({
          user: null,
          accessTokenExpiresAt: null,
          isAuthenticated: null,
          accessToken: null,
        });
      },

      //TODO: implement checking of refresh token logic
      checkAuth: async () => {
        try {
          const result = await authService.refreshToken();

          get().login(result);
        } catch (e: any) {
          //call unsucessfull
          get().logout();
        }
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
