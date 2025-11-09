# Stage 1 : Install dependencies

FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# Stage 2 : Build the app
FROM node:20-alpine AS builder 
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# This run npm run build
RUN npm run build

# stage 3 : Final production image
FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production

# Copy built app and dependencies
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

EXPOSE 3000
CMD ["npm", "start"]
# git add Dockerfile .github/workflows/deploy.yaml
# git commit -m "feat: add Dockerfile and deploy workflow"
# git push origin main