

def check_configured_users(ssh):
    print("gathering configured users")

    # get who i am: username
    command = "net user"
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.readlines()
    print(result)


def check_bitlocker_status(ssh):
    print("check bitlocker status")

    # get who i am: username
    command = "manage-bde -status"
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.readlines()
    print(result)

def check_msdefender_status(ssh):
    print("check ms defender status")

    # get who i am: username
    command = "sc query windefend"
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.readlines()
    print(result)

def check_winfirewall_status(ssh):
    print("check windows firewall status")

    # get who i am: username
    command = "netsh advfirewall show allprofiles state"
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.readlines()
    print(result)

def check_drive_status(ssh):
    print("check windows drive and mount status")

    command = 'powershell -command "Get-PSDrive"'
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.readlines()
    print(result)


def check_last_update_status(ssh):
    print("check when windows was last updated")

    command = 'powershell -command Get-HotFix'
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.readlines()
    print(result)


def get_mpcomputerstatus(ssh):
    print("get various computer stats")

    command = 'powershell -command "Get-MpComputerStatus"'
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.readlines()
    
    return result
