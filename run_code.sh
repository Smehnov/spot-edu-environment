sudo chmod 600 ./id_ed25519
eval `ssh-agent`
ssh-add ./id_ed25519
cat lesson1.py | ssh -6 student@200:42f6:d055:e74e:ce4a:35aa:953a:70f7 python3 -