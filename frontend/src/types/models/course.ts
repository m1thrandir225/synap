import type { Note } from "./note";

export type Course = {
  id: string;
  name: string;
  user_id: string;
  content: string;
  created_at: string;
  updated_at: string;
};

export const dummyCourses: Course[] = [
  {
    id: "f47ac10b-58cc-4372-a567-0e02b2c3d479", // Hardcoded ID
    name: "Introduction to TypeScript",
    user_id: "1a2b3c4d-5e6f-4172-8384-95a6b7c8d9e0", // Hardcoded User ID 1
    content:
      "Learn the basics of TypeScript, including types, interfaces, and classes.",
    created_at: "2024-01-15T10:00:00Z",
    updated_at: "2024-04-20T14:30:00Z",
  },
  {
    id: "98b6fae3-1b4e-49a8-b69d-7b7d6a51d8e2", // Hardcoded ID
    name: "Advanced React Patterns",
    user_id: "f0e9d8c7-b6a5-4234-9567-847362514098", // Hardcoded User ID 2
    content:
      "Deep dive into advanced React concepts like hooks, context, and performance optimization.",
    created_at: "2023-11-01T08:00:00Z",
    updated_at: "2024-04-15T16:00:00Z",
  },
  {
    id: "c7e1b0a5-6d3c-4f7a-8b9e-1c2d3e4f5a6b", // Hardcoded ID
    name: "Node.js Fundamentals",
    user_id: "550e8400-e29b-41d4-a716-446655440000", // Hardcoded User ID 3
    content:
      "Explore backend development using Node.js, Express, and asynchronous programming.",
    created_at: "2024-02-01T12:00:00Z",
    updated_at: "2024-02-01T12:00:00Z",
  },
  {
    id: "3f2a1b0c-8d7e-4c6f-9a8b-5e4d3c2b1a0f", // Hardcoded ID
    name: "Database Design with PostgreSQL",
    user_id: "1a2b3c4d-5e6f-4172-8384-95a6b7c8d9e0", // Hardcoded User ID 1 (Repeated)
    content:
      "Learn relational database design principles and SQL with PostgreSQL.",
    created_at: "2023-09-10T14:00:00Z",
    updated_at: "2024-03-10T10:00:00Z",
  },
  {
    id: "b9e8d7c6-a5b4-4987-8432-1f0e9d8c7b6a", // Hardcoded ID
    name: "CSS Grid and Flexbox Mastery",
    user_id: "f0e9d8c7-b6a5-4234-9567-847362514098", // Hardcoded User ID 2 (Repeated)
    content: "Master modern CSS layout techniques using Grid and Flexbox.",
    created_at: "2024-03-15T09:30:00Z",
    updated_at: "2024-04-25T11:00:00Z",
  },
  {
    id: "6a5b4c3d-2e1f-4098-9a1b-8c7d6e5f4a3b", // Hardcoded ID
    name: "Introduction to Docker",
    user_id: "1a2b3c4d-5e6f-4172-8384-95a6b7c8d9e0", // Hardcoded User ID 1 (Repeated)
    content:
      "Understand containerization concepts and learn to use Docker for development and deployment.",
    created_at: "2024-04-01T11:00:00Z",
    updated_at: "2024-04-22T13:45:00Z",
  },
  {
    id: "d1e2f3a4-b5c6-4789-8d9e-a0b1c2d3e4f5", // Hardcoded ID
    name: "Python for Data Science",
    user_id: "550e8400-e29b-41d4-a716-446655440000", // Hardcoded User ID 3 (Repeated)
    content:
      "Learn Python programming fundamentals and libraries like NumPy and Pandas for data analysis.",
    created_at: "2023-07-20T10:00:00Z",
    updated_at: "2024-02-15T17:00:00Z",
  },
  {
    id: "7b8c9d0e-1f2a-43b4-9c5d-6e7f8a9b0c1d", // Hardcoded ID
    name: "Web Security Essentials",
    user_id: "1a2b3c4d-5e6f-4172-8384-95a6b7c8d9e0", // Hardcoded User ID 1 (Repeated)
    content:
      "Understand common web vulnerabilities (XSS, CSRF, SQLi) and how to prevent them.",
    created_at: "2024-01-05T16:00:00Z",
    updated_at: "2024-04-01T12:10:00Z",
  },
  {
    id: "e0f1a2b3-c4d5-46e7-8f9a-b0c1d2e3f4a5", // Hardcoded ID
    name: "GraphQL Fundamentals",
    user_id: "f0e9d8c7-b6a5-4234-9567-847362514098", // Hardcoded User ID 2 (Repeated)
    content:
      "Learn the core concepts of GraphQL, including schemas, queries, mutations, and subscriptions.",
    created_at: "2024-03-10T13:00:00Z",
    updated_at: "2024-03-10T13:00:00Z",
  },
  {
    id: "4a5b6c7d-8e9f-40a1-b2c3-d4e5f6a7b8c9", // Hardcoded ID
    name: "Cloud Computing with AWS",
    user_id: "abcde123-fgh4-5678-ijkl-mnop98765432", // Hardcoded User ID 4
    content:
      "Introduction to cloud concepts and core AWS services like EC2, S3, and Lambda.",
    created_at: "2023-10-10T09:00:00Z",
    updated_at: "2024-04-18T10:30:00Z",
  },
  {
    id: "9d8c7b6a-5e4f-4321-a0b1-c2d3e4f5a6b7", // Hardcoded ID
    name: "Unit Testing in JavaScript",
    user_id: "1a2b3c4d-5e6f-4172-8384-95a6b7c8d9e0", // Hardcoded User ID 1 (Repeated)
    content:
      "Learn testing principles and how to write unit tests for JavaScript code using frameworks like Jest.",
    created_at: "2024-02-20T14:00:00Z",
    updated_at: "2024-04-12T09:00:00Z",
  },
  {
    id: "1f0e9d8c-7b6a-45b4-8c3d-2e1f0a9b8c7d", // Hardcoded ID
    name: "Introduction to Machine Learning",
    user_id: "550e8400-e29b-41d4-a716-446655440000", // Hardcoded User ID 3 (Repeated)
    content:
      "Basic concepts of machine learning, including supervised and unsupervised learning algorithms.",
    created_at: "2023-12-05T11:30:00Z",
    updated_at: "2024-03-28T14:00:00Z",
  },
  {
    id: "8c7d6e5f-4a3b-4210-9f8e-7d6c5b4a3f2e", // Hardcoded ID
    name: "Building APIs with Python Flask",
    user_id: "f0e9d8c7-b6a5-4234-9567-847362514098", // Hardcoded User ID 2 (Repeated)
    content:
      "Learn to build RESTful APIs using the Python microframework Flask.",
    created_at: "2024-03-01T10:00:00Z",
    updated_at: "2024-04-26T15:00:00Z",
  },
  {
    id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d", // Hardcoded ID
    name: "Version Control with Git",
    user_id: "1a2b3c4d-5e6f-4172-8384-95a6b7c8d9e0", // Hardcoded User ID 1 (Repeated)
    content:
      "Master version control concepts and workflows using Git and platforms like GitHub/GitLab.",
    created_at: "2023-08-15T15:00:00Z",
    updated_at: "2023-08-15T15:00:00Z",
  },
];
