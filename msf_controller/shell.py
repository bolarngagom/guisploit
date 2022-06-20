from . import client as client_controller


def exec_cmd(session_id, cmd):
    client = client_controller.load_client()
    shell = client.sessions.session('1')
    shell.write(cmd)
    output = shell.read()
    return output
