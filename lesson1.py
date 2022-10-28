ROBOT_IP="192.168.50.3"
SPOT_USERNAME="admin"
SPOT_PASSWORD=""


# Helpers to control camera drawing
import requests
VIDEOSERVER_URL="http://luke.merklebot:8000/"
VIDEOSERVER_TOKEN="1234"

def notify_start_line():
    requests.post(VIDEOSERVER_URL + "start_line", json={"token": VIDEOSERVER_TOKEN})


def notify_stop_line():
    requests.post(VIDEOSERVER_URL + "stop_line", json={"token": VIDEOSERVER_TOKEN})

def notify_clear_canvas():
    requests.post(VIDEOSERVER_URL + "clear_canvas", json={"token": VIDEOSERVER_TOKEN})

# WRITE YOUR CODE HERE

