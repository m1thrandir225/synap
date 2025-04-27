import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/dashboard/courses/$courseId/edit')({
  component: RouteComponent,
})

function RouteComponent() {
  return <div>Hello "/dashboard/courses/$courseId/edit"!</div>
}
