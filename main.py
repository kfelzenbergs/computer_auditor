import paramiko
import json


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
    


print(json.dumps(results))
