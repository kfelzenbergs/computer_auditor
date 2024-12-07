import paramiko
import json

from libs.checklist import (
    check_bitlocker_status, 
    check_configured_users, 
    check_msdefender_status, 
    check_winfirewall_status,
    check_drive_status,
    check_last_update_status,
    get_mpcomputerstatus
)

# define a list of servers
servers = [
    "windows_host",
]

results = []
server_data_template = {
    "HOST": "",
    "IDENTITY": "",
    "VERSION_CODENAME": ""
}

# connect to each server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


for server in servers:
    ssh.connect(
        hostname=server,
        username="u",
        password="password"
    )

    # get who i am: username
    command = "whoami"
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.readlines()
    print(result)

    server_data = {}
    # for line in result:
    #     print(line)

    
    server_data["HOST"] = server

    # check_configured_users(ssh)
    # check_bitlocker_status(ssh)
    # check_msdefender_status(ssh)
    # check_winfirewall_status(ssh)
    # check_drive_status(ssh)
    # check_last_update_status(ssh)
    # info = get_mpcomputerstatus(ssh)
    # for line in info:
    #     print(line)
    


print(json.dumps(results))
