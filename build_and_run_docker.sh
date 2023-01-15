echo "Building backend container"
docker build backend -f backend/backend.dockerfile
echo ""

echo "Building frontend container"
docker build frontend -f frontend/frontend.dockerfile
echo ""

echo "Running all via docker-compose"
docker-compose up
echo ""
