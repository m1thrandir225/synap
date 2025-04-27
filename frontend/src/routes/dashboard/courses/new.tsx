import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/dashboard/courses/new')({
  component: RouteComponent,
})

function RouteComponent() {
  return <div>Hello "/dashboard/courses/new"!</div>
}
