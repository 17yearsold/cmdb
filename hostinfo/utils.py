import nmap
import telnetlib
import re
import paramiko


def get_active_hosts(host=''):
    nm = nmap.PortScanner()
    result = nm.scan(hosts=host, arguments='-n -sV', ports='22')
    active_list = []
    for host in nm.all_hosts():
        if result['scan'][host]['tcp'][22]['state'] == 'open':
            active_list.append(host)
    return active_list


def login_ssh_key(hostname='', port=22, username='root',
                  private_key='doc/id_rsa', command=''):
    # pkey = paramiko.RSAKey.from_private_key_file(private_key)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, password='westos')
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode('utf-8')

