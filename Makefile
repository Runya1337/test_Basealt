git: push

add:
	git add .

commit:
	@read -p "Введите сообщение коммита: " msg; \
	git commit -m "$$msg"

push: add commit
	git push