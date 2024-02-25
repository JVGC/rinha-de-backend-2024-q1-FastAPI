.PHONY: help
help:
	@echo "Usage: make \033[36m<command>\033[0m"
	@echo
	@echo 'Commands:'
	@awk 'BEGIN {FS = ":.*##"; printf "\033[36m\033[0m"} /^[$$()% 0-9a-zA-Z_-]+:.*?##/ { printf "\033[36m%16s\033[0m%s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
	@echo

.PHONY: run
run: ## Run the application
	poetry run uvicorn src.main:app --reload