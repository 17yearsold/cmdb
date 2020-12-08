from django.shortcuts import render
from django.http import HttpResponse, Http404
from hostinfo.models import Server
from hostinfo.utils import get_active_hosts, login_ssh_key
from CMDB.settings import commands


# Create your views here.
def hostsinfo(request):
    serverlist = Server.objects.all()
    return render(request, "hostinfo/index.html", {'serverlist': serverlist})


def search(request):
    if request.method == 'GET' and request.GET:
        point = '.'
        seq = []
        for ip in request.GET.values():
            seq.append(ip)
        serverlist = []
        ipaddr = point.join(seq)
        if Server.objects.filter(IP=ipaddr):
            serverlist.append(Server.objects.get(IP=ipaddr))
            return render(request, 'hostinfo/index.html', {'serverlist': serverlist})
        else:
            for active_host in get_active_hosts(ipaddr):
                if active_host == '':
                    return HttpResponse("你访问的IP不存在", status=404)
                else:
                    server = Server()
                    server.IP = active_host
                for command_name, command in commands.items():
                    # command_name="os_type", command="uname"
                    result = login_ssh_key(hostname=active_host, command=command)
                    # set server object attribute
                    setattr(server, command_name, result)
                    # save to mysql
                server.save()
                # Now Scan host info
                serverlist.append(server)
                return render(request, 'hostinfo/index.html', {'serverlist': serverlist})

    return render(request, 'hostinfo/search.html')


def aboutme(request):
    return render(request, "hostinfo/aboutme.html")
