from flask import Flask, request, jsonify, render_template
import socket
import platform
import os
import psutil

app = Flask(__name__)

@app.route('/')
def get_info_html():
    client_ip = request.remote_addr

    try:
        client_hostname = socket.gethostbyaddr(client_ip)[0]
    except socket.herror:
        client_hostname = "Hostname could not be resolved"

    backend_server_hostname = socket.gethostname()

    try:
        backend_server_ip = socket.gethostbyname(backend_server_hostname)
    except socket.gaierror:
        backend_server_ip = "Unknown IP"

    system_info = {
        'os_name': platform.system(),
        'os_version': platform.release(),
        'kernel_version': platform.version(),
        'architecture': platform.machine(),
        'processor': platform.processor(),
        'python_version': platform.python_version(),
        'backend_hostname': backend_server_hostname,
        'backend_ip_address': backend_server_ip
    }
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            hours = int(uptime_seconds // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            system_info['uptime'] = f"{hours} hours {minutes} minutes"
    except FileNotFoundError:
        system_info['uptime'] = "Unknown"

    try:
        system_info['cpu_cores'] = os.cpu_count()
    except NotImplementedError:
        system_info['cpu_cores'] = "Unknown"

    system_info['cpu_percent'] = psutil.cpu_percent(interval=0.1)

    memory = psutil.virtual_memory()
    system_info['memory_total'] = f"{memory.total / (1024**3):.2f} GB"
    system_info['memory_used'] = f"{memory.used / (1024**3):.2f} GB"
    system_info['memory_percent'] = memory.percent

    return render_template('index.html',
                           client_ip=client_ip,
                           client_hostname=client_hostname,
                           system_info=system_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
