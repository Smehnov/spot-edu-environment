import sys
print(sys.version)

# Helpers to control camera drawing
import requests
VIDEOSERVER_URL=""
VIDEOSERVER_TOKEN=""

def notify_start_line():
    requests.post(VIDEOSERVER_URL + "start_line", json={"token": VIDEOSERVER_TOKEN})


def notify_stop_line():
    requests.post(VIDEOSERVER_URL + "stop_line", json={"token": VIDEOSERVER_TOKEN})


def main():
    print('Start execution')
    publish_learner_name("Alex")

    pass


if __name__ == '__main__':
    main()