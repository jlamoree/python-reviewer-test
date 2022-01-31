"""
Runs a command and logs it to S3
Usage:
  lab-3.py something
"""

import subprocess
import sys
import boto3
from datetime import datetime, timezone

PROFILE="workshop"
BUCKET="aws-workshop-bad-logs"

boto3.setup_default_session(profile_name=PROFILE)
s3 = boto3.client("s3")


def main(argv):
    cmd = None
    if argv is None or len(argv) == 0:
        print("You are a bad person.")
        sys.exit(1)
    if argv[0] == "1":
        cmd = ["echo", "one"]
    elif argv[0] == "2":
        cmd = ["echo", "two"]
    elif argv[0] == "3":
        cmd = ["echo", "three"]
    if cmd is None:
        print("Sorry, couldn't match your command.")
        sys.exit(1)

    log_file_name = datetime.now(timezone.utc).strftime("%Y_%m_%d") + "_logfile"
    kickoff_subprocess(cmd, log_file_name)
    upload_output_to_s3(log_file_name)


def kickoff_subprocess(cmd, log_file_name):
    process = subprocess.call(cmd, shell=False)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    output = timestamp + " Command: " + cmd[0] + " | Arg: " + cmd[1] + " | Return Code: " + str(process) + "\n"
    with open(log_file_name, "a+") as file:
        file.write(output)


def upload_output_to_s3(log_file_name):
    with open(log_file_name, "rb") as f:
        s3.upload_fileobj(f, BUCKET, log_file_name)


if __name__ == "__main__":
    main(sys.argv[1:])
