---
server: www.example.com
domainname: example.me
mode: Prod
deployment_name: outline
locale: en_US.UTF-8
timezone: America/New_York
port_number: 45000
project_repo: git@github.com:powellc/outline.git
branch: master
dbpass: jzxovijlsakdfj0ojookfjl32k3jrl
port_number: 30000
postgis: False
bower: True
sentry_key: None
secret_key: ALKJSDFLKXJCOVIJSELKJFEWLKJSLDFKJLEKJ-KLEJWLFEKJ