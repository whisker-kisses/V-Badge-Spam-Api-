# F F V Badge Spam API--

A powerful Flask-based API for managing Free Fire bots with automated attack capabilities and queue management.

## 🎯 Credits

**All credits go to Watashii**
- Developer: Watashii
- Telegram: @Watashii
- Team Channel: @WATASHII_IS_HERE

---

## 📋 Features

- ✅ **Multi-Bot Management** - Control multiple bot accounts simultaneously
- ✅ **Configurable Attacks** - Set custom attempt limits per bot (default: 10 attempts)
- ✅ **Target Queue System** - Queue multiple targets for sequential attacks
- ✅ **API Toggle** - Enable/disable API endpoints on-the-fly
- ✅ **Real-time Status** - Monitor active bots and attack progress
- ✅ **Account Management** - Add new accounts dynamically via API
- ✅ **Persistent Configuration** - API state saved between restarts

---

## 🚀 Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Setup

1. **Clone or download the project**
   ```bash
   cd spamapi
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure accounts**
   
   Edit `vv.json` to add your Free Fire accounts:
   ```json
   {
     "account_uid_1": "password1",
     "account_uid_2": "password2",
     "account_uid_3": "password3"
   }
   ```

4. **Start the server**
   ```bash
   python main.py
   ```

   The API will start on `http://0.0.0.0:5000`

---

## 🔧 Configuration Files

### `vv.json` - Account Configuration
Contains Free Fire account credentials (UID:Password pairs)

### `api_config.json` - API Settings
Automatically created to persist API enable/disable state

---

## 📡 API Endpoints

### Base URL
```
http://your-server-ip:5000/api/
```

---

### 1. **Start Attack**
**Endpoint:** `/api/attack`  
**Method:** `GET`  
**Description:** Launch an attack on a specific target with all available bots

**Parameters:**
- `target` (required) - Target ID to attack

**Example:**
```bash
http://localhost:5000/api/attack?target=123456789
```

**Response:**
```json
{
  "status": "success",
  "message": "Attack started on target 123456789 (10 attempts per bot)",
  "target": "123456789",
  "bots_used": 15,
  "max_attempts": 10,
  "Dev": "Watashii",
  "timestamp": 1738310400.0
}
```

---

### 2. **Check Status**
**Endpoint:** `/api/status`  
**Method:** `GET`  
**Description:** Get current status of all bots and active attacks

**Example:**
```bash
http://localhost:5000/api/status
```

**Response:**
```json
{
  "status": "running",
  "api_enabled": true,
  "active_bots": 15,
  "total_attacks": 150,
  "current_target": 123456789,
  "active_sessions": {},
  "timestamp": 1738310400.0
}
```

---

### 3. **Quick API Check**
**Endpoint:** `/api/check`  
**Method:** `GET`  
**Description:** Quickly check if API is enabled or disabled

**Example:**
```bash
http://localhost:5000/api/check
```

**Response:**
```json
{
  "api_enabled": true,
  "timestamp": 1738310400.0
}
```

---

### 4. **Toggle API**
**Endpoint:** `/api/toggle`  
**Method:** `GET` or `POST`  
**Description:** Enable, disable, or toggle the API state

**Parameters:**
- `action` (optional) - Values: `on`, `off`, `toggle` (default: toggle)

**Examples:**
```bash
# Toggle API state
http://localhost:5000/api/toggle

# Enable API
http://localhost:5000/api/toggle?action=on

# Disable API
http://localhost:5000/api/toggle?action=off
```

**Response:**
```json
{
  "status": "success",
  "message": "API is now enabled",
  "api_enabled": true,
  "timestamp": 1738310400.0
}
```

---

### 5. **Stop All Bots**
**Endpoint:** `/api/stop`  
**Method:** `GET`  
**Description:** Immediately stop all running bots

**Example:**
```bash
http://localhost:5000/api/stop
```

**Response:**
```json
{
  "status": "success",
  "message": "All bots stopped (15 bots terminated)",
  "stopped_count": 15
}
```

---

### 6. **Add Accounts**
**Endpoint:** `/api/add_accounts`  
**Method:** `POST`  
**Description:** Add new bot accounts dynamically

**Content-Type:** `application/json`

**Example:**
```bash
curl -X POST http://localhost:5000/api/add_accounts \
  -H "Content-Type: application/json" \
  -d '{
    "987654321": "password123",
    "123456789": "password456"
  }'
```

**Response:**
```json
{
  "status": "success",
  "message": "Added 2 new accounts",
  "total_accounts": 17
}
```

---

### 7. **Queue Targets**
**Endpoint:** `/api/targets/queue`  
**Method:** `GET`  
**Description:** Add multiple targets to the attack queue

**Parameters:**
- `targets[]` (required) - Multiple target IDs to queue

**Example:**
```bash
http://localhost:5000/api/targets/queue?targets=111111&targets=222222&targets=333333
```

**Response:**
```json
{
  "status": "success",
  "message": "Added 3 targets to queue",
  "queue_size": 3,
  "queue": [111111, 222222, 333333]
}
```

---

### 8. **Attack Next in Queue**
**Endpoint:** `/api/targets/queue/next`  
**Method:** `GET`  
**Description:** Start attack on the next target in queue

**Example:**
```bash
http://localhost:5000/api/targets/queue/next
```

**Response:**
```json
{
  "status": "success",
  "message": "Started attack on next target: 111111",
  "target": 111111,
  "bots_used": 15,
  "remaining_in_queue": 2
}
```

---

## 💡 Usage Examples

### Example 1: Basic Attack
```bash
# Start attack on target
curl "http://localhost:5000/api/attack?target=123456789"

# Check status
curl "http://localhost:5000/api/status"

# Stop all bots when done
curl "http://localhost:5000/api/stop"
```

### Example 2: Queue Multiple Targets
```bash
# Add targets to queue
curl "http://localhost:5000/api/targets/queue?targets=111111&targets=222222&targets=333333"

# Attack first target
curl "http://localhost:5000/api/targets/queue/next"

# Wait for completion, then attack next
curl "http://localhost:5000/api/targets/queue/next"
```

### Example 3: Manage API State
```bash
# Disable API temporarily
curl "http://localhost:5000/api/toggle?action=off"

# Check if API is enabled
curl "http://localhost:5000/api/check"

# Re-enable API
curl "http://localhost:5000/api/toggle?action=on"
```

### Example 4: Python Script Integration
```python
import requests
import time

API_BASE = "http://localhost:5000/api"

# Start attack
response = requests.get(f"{API_BASE}/attack?target=123456789")
print(response.json())

# Monitor status every 5 seconds
for _ in range(10):
    status = requests.get(f"{API_BASE}/status").json()
    print(f"Active bots: {status['active_bots']}, Total attacks: {status['total_attacks']}")
    time.sleep(5)

# Stop when done
requests.get(f"{API_BASE}/stop")
```

---

## 🛡️ Security Notes

⚠️ **Important Security Considerations:**

1. **Never expose this API to the public internet without authentication**
2. **Use firewall rules to restrict access to trusted IPs only**
3. **Consider adding authentication middleware for production use**
4. **Keep your `vv.json` file private and secure**
5. **Use HTTPS/SSL in production environments**

---

## 🔍 Troubleshooting

### API Returns 503 Error
- Check if API is enabled: `http://localhost:5000/api/check`
- Enable API: `http://localhost:5000/api/toggle?action=on`

### Bots Not Starting
- Verify accounts in `vv.json` are valid
- Check console output for error messages
- Ensure network connectivity to Free Fire servers

### Server Not Accessible
- Verify firewall allows connections on port 5000
- Check if server is running: `netstat -an | findstr 5000`
- Try accessing from localhost first: `http://127.0.0.1:5000/api/status`

---

## 📊 Bot Behavior

- **Default Attempts:** 10 attacks per bot per target
- **Message Sent:** Custom Watashii promotional message
- **Actions Per Attempt:**
  1. Join target group/chat
  2. Send promotional message
  3. Send invite (if applicable)
  4. Leave chat
- **Automatic Cleanup:** Bots stop after reaching max attempts

---

## 🌐 Remote Access

To access the API from other devices on your network:

1. Find your local IP: `ipconfig` (Windows) or `ifconfig` (Linux)
2. Use that IP instead of localhost: `http://192.168.1.100:5000/api/status`
3. Ensure firewall allows incoming connections on port 5000

---

## 📝 File Structure

```
V-bagde-spam-api/
├── main.py              # Main API server and bot logic
├── xC4.py              # Encryption/encoding utilities
├── xKEys.py            # Protocol buffer definitions
├── requirements.txt    # Python dependencies
├── vv.json             # Account credentials
├── api_config.json     # API configuration (auto-generated)
├── README.md           # This file
└── __pycache__/        # Python cache files
```

---

## 🤝 Support

For questions, support, or updates:
- **Discord** https://guns.lol/watashii
- **Developer Contact:** @Watashii

---

## ⚖️ Disclaimer

This tool is provided for educational purposes only. Use responsibly and in accordance with Free Fire's Terms of Service. The developer (Watashii) is not responsible for any misuse or consequences resulting from the use of this software.

---

## 📜 License

Developed by **Watashii**  
All rights reserved.

---

**🎮 Happy Gaming! 🎮**

Subscribe to Watashii on YouTube for more awesome tools and updates!
