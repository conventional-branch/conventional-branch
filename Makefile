all: compile-assets compile-site
all-dev: compile-assets-dev serve-site-dev

compile-site:
	echo "Generating static website"
	hugo
	echo "Website generated"

compile-assets:
	echo "Compiling assets"
	cd themes/conventional-branch && npm install && npm run build
	echo "Assets compiled"

serve-site-dev:
	echo "Serving website"
	hugo server --bind=0.0.0.0

compile-assets-dev:
	echo "Compiling assets"
	cd themes/conventional-branch && npm install && npm run start &

test:
	@echo "Running site tests against http://localhost:1313/ ..."
	@pages="\
		http://localhost:1313/ \
		http://localhost:1313/zh/ \
		http://localhost:1313/about/ \
		http://localhost:1313/#summary \
		http://localhost:1313/#specification" ;\
	for page in $$pages; do \
		echo -n "Testing $$page ... "; \
		curl -sSf -o /dev/null $$page && echo "✅ OK" || (echo "❌ FAILED"; exit 1); \
	done

