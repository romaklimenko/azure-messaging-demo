.DEFAULT_GOAL := default

default:
	@echo "Please specify a target"

chmod:
	chmod +x ./shell/*.sh

deploy:
	./shell/deploy.sh

undeploy:
	./shell/undeploy.sh

eg_pub:
	python ./python/event_grid/publisher.py

eg_sub:
	python ./python/event_grid/subscriber.py

eh_pub:
	python ./python/event_hub/publisher.py

eh_sub:
	python ./python/event_hub/subscriber.py

sb_pub:
	python ./python/service_bus/publisher.py

sb_sub1:
	python ./python/service_bus/subscriber_one.py

sb_sub2:
	python ./python/service_bus/subscriber_two.py

sa_pub:
	python ./python/storage_account/publisher.py

sa_sub:
	python ./python/storage_account/subscriber.py
