STUDENT_ID = 0
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

def mark_attempt(STUDENT_ID):
    requests.post(f"http://localhost:6688/attempt/{STUDENT_ID}")

#START HERE
import time
import bosdyn.client
from bosdyn.client.robot_command import RobotCommandClient, RobotCommandBuilder, blocking_stand
from bosdyn.geometry import EulerZXY


def main():
    print('Start execution')
    


if __name__ == '__main__':
    main()