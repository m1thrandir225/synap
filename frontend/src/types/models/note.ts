export type Note = {
  id: string;
  user_id: string;
  course_id: string;
  title: string;
  content: string;
  created_at: string;
  updated_at: string;
};

const user1Id = "f47ac10b-58cc-4372-a567-0e02b2c3d479";
const user2Id = "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d";
const course1Id = "c7a4f3d5-1e8c-4b7a-9f0d-2c8e1a5b6d9e";
const course2Id = "a3b8f5e2-7d4a-4c1b-8e9f-1d7c0a4b5e8f";
const course3Id = "d9e2b1c7-6f3e-4a0d-9c8b-0e5d3b9a1c6e";

export const dummyNotes: Note[] = [
  {
    id: "1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed",
    user_id: user1Id,
    course_id: course1Id,
    title: "Introduction to TypeScript Types",
    content: `
# TypeScript Basics: Types

TypeScript adds static typing to JavaScript. This helps catch errors during development.

## Core Primitive Types

* \`string\`: Represents text values like "Hello World".
* \`number\`: Represents numeric values like 42 or 3.14.
* \`boolean\`: Represents \`true\` or \`false\`.

## Example

\`\`\`typescript
let message: string = "Hello!";
let count: number = 100;
let isActive: boolean = true;
\`\`\`

**Note:** Using types makes the code more predictable.
    `,
    created_at: "2025-04-28T10:00:00.000Z",
    updated_at: "2025-04-29T11:30:00.000Z",
  },
  {
    id: "5e8f9b2d-7c1a-4d0e-8b3f-2c7e1a6b4d9c",
    user_id: user2Id,
    course_id: course2Id,
    title: "React Hooks Overview",
    content: `
# React Hooks

Hooks let you use state and other React features without writing a class.

## Common Hooks

1.  **useState**: Lets you add state to functional components.
2.  **useEffect**: Lets you perform side effects (like data fetching or subscriptions).
3.  **useContext**: Lets you subscribe to React context without nesting.

## useState Example

\`\`\`jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
\`\`\`

[Official React Hooks Docs](https://reactjs.org/docs/hooks-intro.html)
    `,
    created_at: "2025-04-29T14:15:30.123Z",
    updated_at: "2025-04-29T14:15:30.123Z",
  },
  {
    id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d",
    user_id: user1Id,
    course_id: course3Id,
    title: "Database Normalization",
    content: `
# Database Normalization

Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity.

## Normal Forms

* **First Normal Form (1NF):** Ensure atomicity of columns (no repeating groups). Each cell holds a single value.
* **Second Normal Form (2NF):** Be in 1NF and ensure all non-key attributes are fully functional dependent on the primary key.
* **Third Normal Form (3NF):** Be in 2NF and remove transitive dependencies.

### Key Goals

-   Minimize data redundancy.
-   Avoid data modification issues (insert, update, delete anomalies).
-   Simplify queries.

*Remember to balance normalization with performance needs.*
    `,
    created_at: "2025-04-25T09:00:00.000Z",
    updated_at: "2025-04-30T00:15:00.500Z",
  },
  {
    id: "f0e9d8c7-b6a5-4b4c-9d8e-7f6a5b4c3d2e",
    user_id: user2Id,
    course_id: course1Id,
    title: "TypeScript Interfaces vs Types",
    content: `
# Interfaces vs Type Aliases in TypeScript

Both \`interface\` and \`type\` can be used to define the shape of an object.

## Interface

\`\`\`typescript
interface Point {
  x: number;
  y: number;
}

interface Point { // Declaration merging IS allowed
  z?: number;
}

const p1: Point = { x: 10, y: 20 };
\`\`\`

## Type Alias

\`\`\`typescript
type Coordinate = {
  lat: number;
  lon: number;
};

// type Coordinate = { alt: number }; // Error: Duplicate identifier 'Coordinate'. Merging not allowed.

type ID = string | number; // Types can represent unions, intersections, primitives etc.

const coord1: Coordinate = { lat: 40.71, lon: -74.00 };
const userId: ID = "user-123";
\`\`\`

| Feature             | Interface                  | Type Alias               |
|---------------------|----------------------------|--------------------------|
| **Object Shape** | Yes                        | Yes                      |
| **Primitive Alias** | No                         | Yes                      |
| **Union/Tuple** | No                         | Yes                      |
| **Declaration Merge** | Yes                        | No                       |
| **Implements** | Yes (for classes)          | Yes (for classes in TS 3.7+) |

_General advice: Use \`interface\` for object shapes until you need features from \`type\`._
    `,
    created_at: "2025-04-30T00:05:10.987Z",
    updated_at: "2025-04-30T00:05:10.987Z",
  },
];
