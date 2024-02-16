import hashlib
import poll
poll.install()
from pyrad.client import Client
from pyrad.dictionary import Dictionary
from pyrad.packet import AccessRequest, AccessAccept
import sys

def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config

def authenticate_with_radius(config):
    client = Client(server=config['IP'], secret=config['RadiusSecret'].encode(), dict=Dictionary("dictionary"))

    if config['Method'] == 'CHAP':
        # CHAP Implementation
        chap_id = 1  # CHAP ID, typically a single octet
        challenge = b'some_random_challenge'  # The CHAP challenge
        hashed = hashlib.md5(bytes([chap_id]) + config['Password'].encode() + challenge).digest()

        # Create an Access-Request packet
        req = client.CreateAuthPacket(code=AccessRequest, User_Name=config['Username'])
        req["CHAP-Password"] = bytes([chap_id]) + hashed
        req["CHAP-Challenge"] = challenge
        req["Called-Station-Id"] = "hotspotname" #comment if unneeded
        req["NAS-Port-Type"] = 19 #Wireless CCITT 802.11
    elif config['Method'] == 'PAP':
        # PAP Implementation
        req = client.CreateAuthPacket(code=AccessRequest, User_Name=config['Username'])
        req["User-Password"] = req.PwCrypt(config['Password'])
    elif config['Method'] == 'MSCHAPv2':
        # MSCHAPv2 Implementation (placeholder, requires actual implementation)
        pass
    else:
        print("Unsupported authentication method")
        return

    # Send request
    try:
        reply = client.SendPacket(req)
        if reply.code == AccessAccept:
            print("Authentication successful")
        else:
            print("Authentication failed")
    except Exception as e:
        print(f"Failed to connect to the RADIUS server: {e}")


if __name__ == "__main__":
    config_file = 'config.txt'
    config = read_config(config_file)
    authenticate_with_radius(config)
