import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/dashboard/notes/$noteId/')({
  component: RouteComponent,
})

function RouteComponent() {
  return <div>Hello "/dashboard/notes/$noteId/"!</div>
}
