import { isMatch, Link, useMatches } from "@tanstack/react-router";
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "./ui/breadcrumb";

const Breadcrumbs: React.FC = () => {
  const matches = useMatches();

  if (matches.some((match) => match.status === "pending")) {
    return null;
  }

  const matchesWithCrumbs = matches.filter((match) =>
    isMatch(match, "loaderData.crumb"),
  );

  return (
    <Breadcrumb>
      <BreadcrumbList>
        {matchesWithCrumbs.map((item, i) => {
          const isLast = i === matchesWithCrumbs.length - 1;
          const crumbText = item.loaderData?.crumb as string; // We already filtered for string type

          return (
            <BreadcrumbItem key={item.id}>
              {isLast ? (
                <BreadcrumbPage>{crumbText}</BreadcrumbPage>
              ) : (
                <BreadcrumbLink asChild>
                  <Link
                    to={item.pathname} // Use pathname for cleaner links (adjust if fullPath is needed)
                    params={item.params} // Pass params for dynamic routes
                    search={item.search} // Pass search params if relevant
                  >
                    {crumbText}
                  </Link>
                </BreadcrumbLink>
              )}
              {!isLast && <BreadcrumbSeparator />}
            </BreadcrumbItem>
          );
        })}
      </BreadcrumbList>
    </Breadcrumb>
  );
};

export default Breadcrumbs;
