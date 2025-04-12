import { Outlet } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/react-router-devtools"; /*
 * Default Layout for all pages
 */
const DefaultLayout: React.FC<React.PropsWithChildren> = (props) => {
  return (
    <div className="w-full bg-blue-200">
      <div className="container mx-auto h-full w-full">
        <Outlet />
      </div>
      <TanStackRouterDevtools />
    </div>
  );
};

export default DefaultLayout;
