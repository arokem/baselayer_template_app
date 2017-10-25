.DEFAULT_GOAL := run

baselayer/README.md:
	git submodule update --init --remote
	$(MAKE) baselayer-update

.PHONY: baselayer-update run log
baselayer-update:
	./baselayer/tools/submodule_update.sh

log:
	make -C baselayer log

run:
	make -C baselayer run

run_testing:
	make -C baselayer run_testing

run_production:
	make -C baselayer run_production

test:
	make -C baselayer test

test_headless:
	make -C baselayer test_headless

db_init:
	make -C baselayer db_init

db_clear:
	make -C baselayer db_clear

-include "baselayer/README.md"  # always clone baselayer if it doesn't exist
