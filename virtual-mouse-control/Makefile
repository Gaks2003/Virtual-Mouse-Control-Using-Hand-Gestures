.PHONY: install test lint build run clean deploy

# Install dependencies
install:
	pip install -r requirements.txt
	pip install pytest flake8

# Run tests
test:
	pytest tests/ -v

# Lint code
lint:
	flake8 src/ --max-line-length=127

# Build Docker image
build:
	docker build -t virtual-mouse-control:latest .

# Run application locally
run:
	python src/app.py

# Run with Docker
docker-run:
	docker-compose up --build

# Clean up
clean:
	docker stop virtual-mouse-control 2>/dev/null || true
	docker rm virtual-mouse-control 2>/dev/null || true
	docker rmi virtual-mouse-control:latest 2>/dev/null || true
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true

# Deploy application
deploy:
	chmod +x deploy.sh
	./deploy.sh

# Development setup
dev-setup: install
	pip install -e .

# Package for distribution
package:
	python setup.py sdist bdist_wheel