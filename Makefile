git: push

add:
	git add .

commit:
	@read -p "Введите сообщение коммита: " msg; \
	git commit -m "$$msg"

push: add commit
	git push

black:
	@echo "Checking code format with black..."
	black package_app/

clean:
	rm -rf build package_comparator.egg-info *.json