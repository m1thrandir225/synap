import { isMatch, Link, useMatches } from "@tanstack/react-router";
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "./ui/breadcrumb";
import { Fragment } from "react";

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
          const crumbText = item.loaderData?.crumb as string;

          return (
            <Fragment key={item.id}>
              <BreadcrumbItem key={item.id}>
                {isLast ? (
                  <BreadcrumbPage>{crumbText}</BreadcrumbPage>
                ) : (
                  <BreadcrumbLink asChild>
                    <Link
                      to={item.pathname}
                      params={item.params}
                      search={item.search}
                    >
                      {crumbText}
                    </Link>
                  </BreadcrumbLink>
                )}
              </BreadcrumbItem>
              {!isLast && <BreadcrumbSeparator />}
            </Fragment>
          );
        })}
      </BreadcrumbList>
    </Breadcrumb>
  );
};

export default Breadcrumbs;
