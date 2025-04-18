FROM node:20-alpine as base
WORKDIR /app

ARG VITE_BACKEND_URL

RUN npm install -g pnpm

COPY package.json pnpm-lock.yaml ./
ENV NODE_ENV=development

# ---- Dependencies Stage ----
FROM base as dependencies
RUN pnpm install --frozen-lockfile
COPY . .

# ---- Development Stage ----
FROM dependencies as dev
EXPOSE 5173
CMD ["pnpm", "run", "start"]

# ---- Build Stage ----
FROM dependencies as builder
ENV NODE_ENV=production
RUN pnpm run build

# ---- Production Stage ----
FROM nginx:1.25-alpine as prod
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /app/dist .
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
