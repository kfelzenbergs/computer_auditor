from datetime import datetime
from scp import SCPClient
import json


def check_configured_users(ssh):
    print("gathering configured users")

    # get configured user accounts
    command = 'powershell -command "Get-LocalUser | ConvertTo-Json"'
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.read()

    account_list = []
    if result:
        result = json.loads(result)

        for account in result:
            # Enabled, Name, LastLogon

            if account['LastLogon']:
                timestamp_received = int(account['LastLogon'].split('(')[1].split(')')[0]) / 1000
                lastLogon = str(datetime.fromtimestamp(timestamp_received))
            else:
                lastLogon = False

            obj_struct = {
                "Enabled": account['Enabled'],
                "LastLogon": lastLogon,
                "Name": account['Name']
            }

            account_list.append(obj_struct)

    return account_list


def check_bitlocker_status(ssh):
    print("check bitlocker status")

    # get volume bitlocker status
    command = 'powershell -command "Get-BitlockerVolume | ConvertTo-Json"'
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.read()

    # MountPoint, LockStatus

    volume_bitlocker_status = []
    if result:
        result = json.loads(result)

        obj_struct = {
            "MountPoint": result['MountPoint'],
            "LockStatus": result["LockStatus"],
        }

        volume_bitlocker_status.append(obj_struct)

    return volume_bitlocker_status




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

    command = 'powershell -command "Get-HotFix  | ConvertTo-Json"'
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.read()
    return result


def get_mpcomputerstatus(ssh):
    print("get various computer stats")

    command = 'powershell -command "Get-MpComputerStatus | ConvertTo-Json"'
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.read()
    result = json.loads(result)
    
    return result


def check_antivirus(ssh):
    print("checks if antivirus is installed")

    # copy binary
    with SCPClient(ssh.get_transport()) as scp:
        print("attempting to upload binary...")
        scp.put('libs/binaries/win_antivirus_check.exe', 'C:')

        print("executing binary...")
        # execute binary
        command = 'powershell -command "C:\\win_antivirus_check.exe"'
        stdin, stdout, stderr = ssh.exec_command(command)
        stdin.close()
        result = stdout.read()
        result = json.loads(result)
        

        print("cleanup..")
        # cleanup
        command = 'powershell -command "Remove-Item C:\\win_antivirus_check.exe"'
        stdin, stdout, stderr = ssh.exec_command(command)
        stdin.close()

        return result




