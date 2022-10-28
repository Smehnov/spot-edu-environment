with open('/etc/yggdrasil.conf', 'r') as f:
    ygg = f.read()
ygg = ygg.replace('Peers: []', """
Peers:
[
    tcp://ygg-ru.cofob.ru:18000
    tcp://ygg-ru2.cofob.ru:80
    tcp://ygg.loskiq.dev:17313
    tcp://yggnode.cf:18226
    tls://ygg-ru2.cofob.ru:443
    tls://yggnode.cf:18227
    tls://ygg.loskiq.dev:17314
    tls://minecast.xyz:3785
    tcp://yggdrasil.su:62486
    tls://yggdrasil.su:62586
    tcp://lax.yuetau.net:6642
    tls://lax.yuetau.net:6643
]
""")

with open('/etc/yggdrasil.conf', 'w') as f:
    f.write(ygg)
