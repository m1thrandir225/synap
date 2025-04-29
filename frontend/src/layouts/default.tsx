import { Outlet } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/react-router-devtools";

/*
 * Default Layout for all pages
 */
const DefaultLayout: React.FC<React.PropsWithChildren> = (props) => {
  return (
    <div className="w-full">
      <main className="h-full w-full">
        <Outlet />
      </main>
      <TanStackRouterDevtools position="top-right" />
    </div>
  );
};

export default DefaultLayout;
