# Stage 1: Install dependencies
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# Stage 2: Build the app
# This stage now uses the 'standalone' output
FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# Stage 3: Final production image
# This stage is now much smaller and more efficient
FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production

# Copy the standalone output
COPY --from=builder /app/.next/standalone ./

# Copy the public folder
COPY --from=builder /app/public ./public

# Copy the static assets
COPY --from=builder /app/.next/static ./.next/static

EXPOSE 3000
# Run the new standalone server
CMD ["node", "server.js"]
#git add next.config.ts Dockerfile
# git commit -m "fix: configure Next.js standalone output for Docker"
# git push origin main