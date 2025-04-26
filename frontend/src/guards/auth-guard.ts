import { useAuthStore } from "@/stores/auth.store";
import { redirect } from "@tanstack/react-router";
export const authGuard = () => {
  const { _hasHydrated, isAuthenticated } = useAuthStore.getState();

  if (!_hasHydrated) {
    return new Promise((resolve) => {
      const unsubscribe = useAuthStore.subscribe((state) => {
        if (state._hasHydrated) {
          unsubscribe();
          if (!state.isAuthenticated) {
            resolve(redirect({ to: "/" }));
          } else {
            resolve({ isAuthenticated: true });
          }
        }
      });
    });
  }

  if (!isAuthenticated) {
    return redirect({ to: "/" });
  }

  return { isAuthenticated: true };
};
