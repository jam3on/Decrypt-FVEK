import argparse
from binascii import unhexlify
from Crypto.Cipher import AES
from sty import fg, ef
from sys import exit

# main program
if __name__ == '__main__':
    # init command line parser
    parser = argparse.ArgumentParser(description='BitLocker Key Decryptor')
    parser.add_argument('-vmk', type=str, required=True, help='Hex-encoded Volume Master Key (VMK)')
    parser.add_argument('-nonce', type=str, required=True, help='Hex-encoded Nonce')
    parser.add_argument('-mac', type=str, required=True, help='Hex-encoded MAC')
    parser.add_argument('-key', type=str, required=True, help='Hex-encoded encrypted Full Volume Encryption Key (FVEK)')

    # parse command line arguments
    args = parser.parse_args()

    try:
        vmk = unhexlify(args.vmk)
    except:
        print("[-] Error: Could not decode the Volume Master Key (VMK)")
        exit(1)

    try:
        nonce = unhexlify(args.nonce)
    except:
        print("[-] Error: Could not decode the Nonce")
        exit(1)

    try:
        mac = unhexlify(args.mac)
    except:
        print("[-] Error: Could not decode the MAC")
        exit(1)

    try:
        encrypted_fvek = unhexlify(args.key)
    except:
        print("[-] Error: Could not decode the encrypted Full Volume Encryption Key (FVEK)")
        exit(1)           

    # initialize AES-CCM with given VMK and nonce
    cipher = AES.new(vmk, AES.MODE_CCM, nonce=nonce)

    try:
        # decrypt and verify encrypted Full Volume Master Key (FVMK)
        plaintext = cipher.decrypt_and_verify(encrypted_fvek, mac)
        decrypted_fvek = plaintext[12:]
        print("FVEK:{}".format(decrypted_fvek.hex()))

        # write FVEK file for use with dislocker
        with open("fvek", "w") as f:
            f.write(decrypted_fvek.hex())

    except KeyError:
        print("[-] Error: Could not decrypt the encrypted Full Volume Encryption Key (FVEK)")
        exit(1)
