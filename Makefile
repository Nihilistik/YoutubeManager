########################################
RUN_COMMAND=docker-compose -f local.yml run --rm django

########################################

tests: $(ATTRS)
	$(RUN_COMMAND) coverage run -m pytest $(ATTRS)


coverage:
	$(RUN_COMMAND) coverage report

.PHONY: tests coverage
