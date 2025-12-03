# DeVloped By AbdeeLkarim Amiri
import requests
import os
import psutil
import sys
import jwt
import pickle
import json
import binascii
import time
import urllib3
import xKEys
import base64
import datetime
import re
import socket
import threading
import http.client
import ssl
import gzip
import asyncio
import gc
from flask import Flask, request, jsonify
from io import BytesIO
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import *
from datetime import datetime, timedelta
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from cfonts import render, say
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize Flask app
app = Flask(__name__)

# Global variables for API control
active_bots = {}
bot_instances = {}  # Store actual bot instances for stopping
bot_lock = threading.Lock()
TARGET_QUEUE = []
CURRENT_TARGET = None
API_STATE = {'enabled': True}  # Use dict instead of bool
API_CONFIG_FILE = "api_config.json"

def load_api_config():
    """Load API configuration from file"""
    try:
        if os.path.exists(API_CONFIG_FILE):
            with open(API_CONFIG_FILE, 'r') as f:
                config = json.load(f)
                API_STATE['enabled'] = config.get('enabled', True)
    except:
        pass

def save_api_config():
    """Save API configuration to file"""
    try:
        with open(API_CONFIG_FILE, 'w') as f:
            json.dump({'enabled': API_STATE['enabled']}, f)
    except:
        pass

# Load config on startup
load_api_config()

# Create shortcut variable
API_ENABLED = API_STATE['enabled']

def G_AccEss(U, P):
    UrL = "https://100067.connect.garena.com/oauth/guest/token/grant"
    HE = {
        "Host": "100067.connect.garena.com",
        "User-Agent": Ua(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close",
    }
    dT = {
        "uid": f"{U}",
        "password": f"{P}",
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067",
    }
    try:
        R = requests.post(UrL, headers=HE, data=dT)
        if R.status_code == 200:
            return R.json()["access_token"], R.json()["open_id"]
        else:
            print(R.json())
    except Exception as e:
        print(e)
        ResTarTinG()


def MajorLoGin(PyL):
    context = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection("loginbp.ggblueshark.com", context=context)
    headers = {
        "X-Unity-Version": "2018.4.11f1",
        "ReleaseVersion": "OB51",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-GA": "v1 1",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)",
        "Host": "loginbp.ggblueshark.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
    }
    try:
        conn.request("POST", "/MajorLogin", body=PyL, headers=headers)
        response = conn.getresponse()
        raw_data = response.read()
        if response.getheader("Content-Encoding") == "gzip":
            with gzip.GzipFile(fileobj=BytesIO(raw_data)) as f:
                raw_data = f.read()
        TexT = raw_data.decode(errors="ignore")
        if "BR_PLATFORM_INVALID_OPENID" in TexT or "BR_GOP_TOKEN_AUTH_FAILED" in TexT:
            sys.exit()
        return raw_data.hex() if response.status in [200, 201] else None
    finally:
        conn.close()


Thread(target=AuTo_ResTartinG, daemon=True).start()


class FF_CLient:
    def __init__(self, U, P, target_id=None, max_attempts=10):
        """
        target_id: optional. If provided, it will be used as the GroupID (TarGeT)
        instead of the GroupID parsed from incoming packets.
        max_attempts: number of times to attempt attacking the target (default 10)
        """
        self.empty_count = 0
        self.reader = None
        self.writer = None
        self.target_id = target_id
        self.bot_uid = None
        self.account_uid = U
        self.running = True
        self.attempt_count = 0
        self.max_attempts = max_attempts
        self.Get_FiNal_ToKen_0115(U, P)

    async def STarT(self, JwT_ToKen, AutH_ToKen, ip, port, ip2, port2, key, iv, bot_uid):
        self.bot_uid = bot_uid
        R = asyncio.Event()
        task1 = asyncio.create_task(
            self.ChaT(self.JwT_ToKen, self.AutH_ToKen, ip, port, key, iv, bot_uid, R)
        )
        await R.wait()
        await asyncio.sleep(0.5)
        task2 = asyncio.create_task(
            self.OnLinE(self.JwT_ToKen, self.AutH_ToKen, ip2, port2, key, iv, bot_uid)
        )
        await asyncio.gather(task1)

    async def sF(self):
        if self.writer:
            try:
                self.writer.close()
                await asyncio.sleep(0.2)
                await self.writer.wait_closed()
            except Exception as e:
                print(f" - Error CLose WriTer => {e}")
                ResTarTinG()
        self.reader = None
        self.writer = None
        gc.collect()

    async def OnLinE(self, Token, tok, host2, port2, key, iv, bot_uid):
        T = "ar"
        global writer, writer2, TarGeT, sQ, Nm
        while self.running:
            try:
                self.reader2, self.writer2 = await asyncio.open_connection(host2, int(port2))
                await asyncio.sleep(0.5)
                self.writer2.write(bytes.fromhex(tok))
                await self.writer2.drain()
                await asyncio.sleep(0.4)
                while self.running:
                    try:
                        self.DaTa = await self.reader2.read(9999)
                        if not self.DaTa:
                            await asyncio.sleep(0.2)
                            break
                    except (
                        asyncio.TimeoutError,
                        ConnectionResetError,
                        ConnectionAbortedError,
                        asyncio.IncompleteReadError,
                        BrokenPipeError,
                        OSError,
                        Exception,
                    ) as e:
                        pass
            except (
                asyncio.TimeoutError,
                ConnectionRefusedError,
                ConnectionResetError,
                ConnectionAbortedError,
                asyncio.IncompleteReadError,
                BrokenPipeError,
                OSError,
                Exception,
            ) as e:
                pass

    async def ChaT(self, Token, tok, host, port, key, iv, bot_uid, R):
        T = "fr"
        print(f"Bot UID: {bot_uid}")
        global writer, writer2, TarGeT, sQ, Nm
        while self.running and self.attempt_count < self.max_attempts:
            try:
                self.reader, self.writer = await asyncio.open_connection(host, int(port))
                self.writer.write(bytes.fromhex(tok))
                await self.writer.drain()
                await asyncio.sleep(0.4)
                self.writer.write(GLobaL(T, key, iv))
                await self.writer.drain()
                await asyncio.sleep(0.4)
                R.set()
                while self.running and self.attempt_count < self.max_attempts:
                    try:
                        self.DaTa = await self.reader.read(9999)
                        if not self.DaTa:
                            await asyncio.sleep(0.2)
                            break
                        if self.DaTa.hex().startswith("1200") and b"SecretCode" in self.DaTa:
                            # Increment attempt counter
                            self.attempt_count += 1
                            
                            U = json.loads(DeCode_PackEt(self.DaTa.hex()[10:]))
                            U2 = json.loads(DeCode_PackEt(self.DaTa.hex()[36:]))
                            Uu = json.loads(U["5"]["data"]["8"]["data"])

                            Nm = U2["9"]["data"]["1"]["data"]
                            # Use target_id if provided, otherwise parse from packet
                            if self.target_id:
                                try:
                                    TarGeT = int(self.target_id)
                                except Exception:
                                    # fallback to parsed GroupID if target_id invalid
                                    TarGeT = int(Uu.get("GroupID", 0))
                            else:
                                TarGeT = int(Uu["GroupID"])

                            sQ = Uu["SecretCode"]
                            rQ = Uu.get("RecruitCode")

                            # RedZed_3alamyia_Chat(uid, code , K, I)
                            self.writer.write(RedZed_3alamyia_Chat(TarGeT, sQ, key, iv))
                            await self.writer.drain()

                            # ---- FIXED MESSAGE (no f-string issues) ----
                            msg_part1 = (
                                "-HELLO I AM SPIDEERIO GAMING  !\n\n"
                                "SUBSCRIBE ME ON YOUTUBE  OR BE BANNED \n\n"
                                "SPIDEERIO GAMING : "
                            )
                            msg_part2 = "@spideerio !! \n\n"
                            msg_part3 = (
                                "telegram team channel : @MorpheusBlackEra \n\n"
                                "DEV Telegram username : @spideerio"
                            )

                            full_msg = (
                                "[FF0000][B][C]"
                                + xMsGFixinG(msg_part1)
                                + "[00FF00]"
                                + xMsGFixinG(msg_part2)
                                + "[FFFF00]"
                                + xMsGFixinG(msg_part3)
                            )

                            # send message
                            self.writer.write(RedZed_SendMsg(full_msg, TarGeT, bot_uid, key, iv))
                            await self.writer.drain()

                            await asyncio.sleep(1.5)

                            # send invite
                            try:
                                if hasattr(self, 'writer2'):
                                    self.writer2.write(RedZed_SendInv(bot_uid, TarGeT, key, iv))
                                    await self.writer2.drain()
                            except Exception:
                                # writer2 might not exist or be connected; ignore if it fails
                                pass

                            # quit chat
                            try:
                                self.writer.write(quit_caht_redzed(TarGeT, key, iv))
                                await self.writer.drain()
                            except Exception:
                                pass

                            await asyncio.sleep(1.2)

                            print(f"Bot: {bot_uid} => Target: {TarGeT} [Attempt {self.attempt_count}/{self.max_attempts}]")
                            
                            # Log the successful attack
                            with bot_lock:
                                if self.account_uid not in active_bots:
                                    active_bots[self.account_uid] = []
                                active_bots[self.account_uid].append({
                                    'bot_uid': bot_uid,
                                    'target': TarGeT,
                                    'timestamp': time.time(),
                                    'attempt': self.attempt_count
                                })
                            
                            # Check if we've reached max attempts
                            if self.attempt_count >= self.max_attempts:
                                print(f"Bot: {bot_uid} completed {self.max_attempts} attempts. Stopping...")
                                self.running = False
                                break

                    except (
                        asyncio.TimeoutError,
                        ConnectionResetError,
                        ConnectionAbortedError,
                        asyncio.IncompleteReadError,
                        BrokenPipeError,
                        OSError,
                        Exception,
                    ) as e:
                        pass
            except (
                asyncio.TimeoutError,
                ConnectionRefusedError,
                ConnectionResetError,
                ConnectionAbortedError,
                asyncio.IncompleteReadError,
                BrokenPipeError,
                OSError,
                Exception,
            ) as e:
                pass
        
        # Cleanup after finishing attempts
        await self.sF()
        print(f"Bot {bot_uid} finished with {self.attempt_count} attempts")

    def stop(self):
        """Stop the bot"""
        self.running = False
        asyncio.run(self.sF())

    def GeT_Key_Iv(self, serialized_data):
        my_message = xKEys.MyMessage()
        my_message.ParseFromString(serialized_data)
        timestamp, key, iv = my_message.field21, my_message.field22, my_message.field23
        timestamp_obj = Timestamp()
        timestamp_obj.FromNanoseconds(timestamp)
        timestamp_seconds = timestamp_obj.seconds
        timestamp_nanos = timestamp_obj.nanos
        combined_timestamp = timestamp_seconds * 1_000_000_000 + timestamp_nanos
        return combined_timestamp, key, iv

    def GeT_LoGin_PorTs(self, JwT_ToKen, PayLoad):
        self.UrL = "https://clientbp.ggwhitehawk.com/GetLoginData"
        self.HeadErs = {
            "Expect": "100-continue",
            "Authorization": f"Bearer {JwT_ToKen}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB51",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)",
            "Host": "clientbp.ggwhitehawk.com",
            "Connection": "close",
            "Accept-Encoding": "gzip, deflate, br",
        }
        try:
            self.Res = requests.post(self.UrL, headers=self.HeadErs, data=PayLoad, verify=False)
            self.BesTo_data = json.loads(DeCode_PackEt(self.Res.content.hex()))
            address, address2 = self.BesTo_data["32"]["data"], self.BesTo_data["14"]["data"]
            ip, ip2 = address[: len(address) - 6], address2[: len(address) - 6]
            port, port2 = address[len(address) - 5 :], address2[len(address2) - 5 :]
            return ip, port, ip2, port2
        except requests.RequestException as e:
            print(f" - Bad Requests !")
        print(" - Failed To GeT PorTs !")
        return None, None

    def ToKen_GeneRaTe(self, U, P):
        try:
            if U and P:
                self.PLaFTrom = 4
                self.A, self.O = G_AccEss(U, P)
                self.Version, self.V = "2019118695", "1.118.1"
                self.PyL = {
                    3: str(datetime.now())[:-7],
                    4: "free fire",
                    5: 1,
                    7: self.V,
                    8: "Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)",
                    9: "Handheld",
                    10: "Verizon Wireless",
                    11: "WIFI",
                    12: 1280,
                    13: 960,
                    14: "240",
                    15: "x86-64 SSE3 SSE4.1 SSE4.2 AVX AVX2 | 2400 | 4",
                    16: 5951,
                    17: "Adreno (TM) 640",
                    18: "OpenGL ES 3.0",
                    19: "Google|0fc0e446-ca27-4faa-824a-d40d77767de9",
                    20: "20.171.73.202",
                    21: "fr",
                    22: self.O,
                    23: self.PLaFTrom,
                    24: "Handheld",
                    25: "google G011A",
                    29: self.A,
                    30: 1,
                    41: "Verizon Wireless",
                    42: "WIFI",
                    57: "1ac4b80ecf0478a44203bf8fac6120f5",
                    60: 32966,
                    61: 29779,
                    62: 2479,
                    63: 914,
                    64: 31176,
                    65: 32966,
                    66: 31176,
                    67: 32966,
                    70: 4,
                    73: 2,
                    74: "/data/app/com.dts.freefireth-g8eDE0T268FtFmnFZ2UpmA==/lib/arm",
                    76: 1,
                    77: "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-g8eDE0T268FtFmnFZ2UpmA==/base.apk",
                    78: 6,
                    79: 1,
                    81: "32",
                    83: self.Version,
                    86: "OpenGLES2",
                    87: 255,
                    88: self.PLaFTrom,
                    89: "J\u0003FD\u0004\r_UH\u0003\u000b\u0016_\u0003D^J>\u000fWT\u0000\\=\nQ_;\u0000\r;Z\u0005a",
                    90: "Phoenix",
                    91: "AZ",
                    92: 10214,
                    93: "3rd_party",
                    94: "KqsHT7gtKWkK0gY/HwmdwXIhSiz4fQldX3YjZeK86XBTthKAf1bW4Vsz6Di0S8vqr0Jc4HX3TMQ8KaUU3GeVvYzWF9I=",
                    95: 111207,
                    97: 1,
                    98: 1,
                    99: f"{self.PLaFTrom}",
                    100: f"{self.PLaFTrom}",
                }
            try:
                self.PyL = CrEaTe_ProTo(self.PyL).hex()
                print(self.PyL)
                self.PaYload = bytes.fromhex(EnC_AEs(self.PyL))
            except:
                ResTarTinG()
            self.ResPonse = MajorLoGin(self.PaYload)
            if self.ResPonse:
                self.BesTo_data = json.loads(DeCode_PackEt(self.ResPonse))
                print(self.BesTo_data)
                self.bot_uid = self.BesTo_data["1"]["data"]
                self.JwT_ToKen = self.BesTo_data["8"]["data"]
                self.combined_timestamp, self.key, self.iv = self.GeT_Key_Iv(bytes.fromhex(self.ResPonse))
                ip, port, ip2, port2 = self.GeT_LoGin_PorTs(self.JwT_ToKen, self.PaYload)
                return (
                    self.JwT_ToKen,
                    self.key,
                    self.iv,
                    self.combined_timestamp,
                    ip,
                    port,
                    ip2,
                    port2,
                    self.bot_uid,
                )
        except Exception as e:
            print("From Token Generate ", e)
            ResTarTinG()

    def Get_FiNal_ToKen_0115(self, U, P):
        token, key, iv, Timestamp, ip, port, ip2, port2, bot_uid = self.ToKen_GeneRaTe(U, P)
        self.JwT_ToKen = token
        try:
            self.AfTer_DeC_JwT = jwt.decode(token, options={"verify_signature": False})
            self.AccounT_Uid = self.AfTer_DeC_JwT.get("account_id")
            self.Nm = self.AfTer_DeC_JwT.get("nickname")
            self.H, self.M, self.S = GeT_Time(self.AfTer_DeC_JwT.get("exp"))
            self.Vr = self.AfTer_DeC_JwT.get("release_version")
            self.EncoDed_AccounT = hex(self.AccounT_Uid)[2:]
            self.HeX_VaLue = DecodE_HeX(Timestamp)
            self.TimE_HEx = self.HeX_VaLue
            self.JwT_ToKen_ = token.encode().hex()
        except Exception as e:
            print(f" - Error In ToKen : {e}")
            return
        try:
            self.Header = hex(len(EnC_PacKeT(self.JwT_ToKen_, key, iv)) // 2)[2:]
            length = len(self.EncoDed_AccounT)
            self.__ = "00000000"
            if length == 9:
                self.__ = "0000000"
            elif length == 8:
                self.__ = "00000000"
            elif length == 10:
                self.__ = "000000"
            elif length == 7:
                self.__ = "000000000"
            else:
                print("Unexpected length encountered")
            self.Header = f"0115{self.__}{self.EncoDed_AccounT}{self.TimE_HEx}00000{self.Header}"
            self.FiNal_ToKen_0115 = self.Header + EnC_PacKeT(self.JwT_ToKen_, key, iv)
        except Exception as e:
            print(f" - Erorr In Final Token : {e}")
        self.AutH_ToKen = self.FiNal_ToKen_0115
        asyncio.run(self.STarT(self.JwT_ToKen, self.AutH_ToKen, ip, port, ip2, port2, key, iv, bot_uid))
        return self.AutH_ToKen, key, iv


def load_accounts(file_path="vv.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def start_bots_for_target(target_id, account_limit=None, max_attempts=10):
    """Start bots for a specific target"""
    accounts = load_accounts()
    
    if account_limit:
        # Limit the number of accounts to use
        accounts = dict(list(accounts.items())[:account_limit])
    
    def run_bot(uid, pwd):
        bot = FF_CLient(uid, pwd, target_id, max_attempts)
        with bot_lock:
            if uid not in bot_instances:
                bot_instances[uid] = []
            bot_instances[uid].append(bot)
    
    threads = []
    for uid, pwd in accounts.items():
        t = threading.Thread(target=run_bot, args=(uid, pwd), daemon=True)
        t.start()
        threads.append(t)
    
    return len(accounts)


# Flask API Endpoints
@app.route('/api/attack', methods=['GET'])
def api_attack():
    """API endpoint to start attack on a target (10 attempts per bot)"""
    if not API_STATE['enabled']:
        return jsonify({
            'status': 'error',
            'message': 'API is currently disabled'
        }), 503
    
    target_id = request.args.get('target')
    
    if not target_id:
        return jsonify({
            'status': 'error',
            'message': 'Target ID is required'
        }), 400
    
    try:
        # Validate target ID
        target_id_int = int(target_id)
        
        # Start bots with 10 attempts each
        count_used = start_bots_for_target(target_id_int, None, 10)
        
        # Update global target
        global CURRENT_TARGET
        CURRENT_TARGET = target_id_int
        
        return jsonify({
            'status': 'success',
            'message': f'Attack started on target {target_id} (10 attempts per bot)',
            'target': target_id,
            'bots_used': count_used,
            'max_attempts': 10,
            'Dev': 'Watashii',
            'timestamp': time.time()
        })
    
    except ValueError:
        return jsonify({
            'status': 'error',
            'message': 'Invalid target ID format'
        }), 400
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/status', methods=['GET'])
def api_status():
    """API endpoint to check bot status"""
    with bot_lock:
        active_count = len(active_bots)
        total_attacks = sum(len(bots) for bots in active_bots.values())
        
        return jsonify({
            'status': 'running',
            'api_enabled': API_STATE['enabled'],
            'active_bots': active_count,
            'total_attacks': total_attacks,
            'current_target': CURRENT_TARGET,
            'active_sessions': active_bots,
            'timestamp': time.time()
        })


@app.route('/api/check', methods=['GET'])
def api_check():
    """Quick endpoint to check if API is on or off"""
    return jsonify({
        'api_enabled': API_STATE['enabled'],
        'timestamp': time.time()
    })


@app.route('/api/toggle', methods=['GET', 'POST'])
def api_toggle():
    """API endpoint to toggle API on/off"""
    action = request.args.get('action', default='toggle').lower()
    
    if action == 'on':
        API_STATE['enabled'] = True
        status = 'enabled'
    elif action == 'off':
        API_STATE['enabled'] = False
        status = 'disabled'
    else:  # toggle
        API_STATE['enabled'] = not API_STATE['enabled']
        status = 'enabled' if API_STATE['enabled'] else 'disabled'
    
    # Save config to file
    save_api_config()
    
    return jsonify({
        'status': 'success',
        'message': f'API is now {status}',
        'api_enabled': API_STATE['enabled'],
        'timestamp': time.time()
    })


@app.route('/api/stop', methods=['GET'])
def api_stop():
    """API endpoint to stop all bots immediately"""
    with bot_lock:
        stopped_count = 0
        # Stop all bot instances
        for account, bots in list(bot_instances.items()):
            for bot in bots:
                try:
                    bot.stop()
                    stopped_count += 1
                except:
                    pass
        
        # Clear all tracking
        bot_instances.clear()
        active_bots.clear()
        
        global CURRENT_TARGET
        CURRENT_TARGET = None
        
        return jsonify({
            'status': 'success',
            'message': f'All bots stopped ({stopped_count} bots terminated)',
            'stopped_count': stopped_count
        })


@app.route('/api/add_accounts', methods=['POST'])
def api_add_accounts():
    """API endpoint to add new accounts"""
    try:
        new_accounts = request.json
        
        if not isinstance(new_accounts, dict):
            return jsonify({
                'status': 'error',
                'message': 'Accounts must be provided as JSON object'
            }), 400
        
        # Load existing accounts
        existing_accounts = load_accounts()
        
        # Add new accounts
        existing_accounts.update(new_accounts)
        
        # Save back to file
        with open("vv.json", "w", encoding="utf-8") as f:
            json.dump(existing_accounts, f, indent=2)
        
        return jsonify({
            'status': 'success',
            'message': f'Added {len(new_accounts)} new accounts',
            'total_accounts': len(existing_accounts)
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/targets/queue', methods=['GET'])
def api_queue_targets():
    """API endpoint to queue multiple targets"""
    targets = request.args.getlist('targets')
    
    if not targets:
        return jsonify({
            'status': 'error',
            'message': 'No targets provided'
        }), 400
    
    global TARGET_QUEUE
    TARGET_QUEUE.extend([int(t) for t in targets if t.isdigit()])
    
    return jsonify({
        'status': 'success',
        'message': f'Added {len(targets)} targets to queue',
        'queue_size': len(TARGET_QUEUE),
        'queue': TARGET_QUEUE
    })


@app.route('/api/targets/queue/next', methods=['GET'])
def api_next_target():
    """API endpoint to attack next target in queue"""
    if not API_STATE['enabled']:
        return jsonify({
            'status': 'error',
            'message': 'API is currently disabled'
        }), 503
    
    global TARGET_QUEUE, CURRENT_TARGET
    
    if not TARGET_QUEUE:
        return jsonify({
            'status': 'error',
            'message': 'No targets in queue'
        }), 400
    
    next_target = TARGET_QUEUE.pop(0)
    CURRENT_TARGET = next_target
    
    # Start attack on next target
    count_used = start_bots_for_target(next_target)
    
    return jsonify({
        'status': 'success',
        'message': f'Started attack on next target: {next_target}',
        'target': next_target,
        'bots_used': count_used,
        'remaining_in_queue': len(TARGET_QUEUE)
    })


def StarT_SerVer():
    """Start the server with API"""
    print(render("Global API", colors=["white", "yellow"], align="center"))
    TexT = f"[API Info] > Server is running\n[API Status] > [bold green]Ready[/bold green]\n[API Endpoint] > http://0.0.0.0:5000/api/"
    panel = Panel(
        Align.center(TexT),
        title="[bold yellow]FF - GLobaL API Server[/bold yellow]",
        border_style="bright_yellow",
        padding=(1, 2),
        expand=False,
    )
    console.print(panel)
    
    # Start Flask server
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)


if __name__ == "__main__":
    StarT_SerVer()