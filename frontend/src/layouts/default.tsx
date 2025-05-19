import { Outlet } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/react-router-devtools";

import { Toaster } from "@/components/ui/sonner";
/*
 * Default Layout for all pages
 */
const DefaultLayout: React.FC<React.PropsWithChildren> = (props) => {
  return (
    <div className="w-full">
      <main className="h-full w-full">
        <Outlet />
      </main>
      <Toaster />
      <TanStackRouterDevtools position="top-right" />
    </div>
  );
};

export default DefaultLayout;
