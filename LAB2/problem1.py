import hashlib
import requests
import time

def fetch_password_list(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        print("Failed to fetch password list")
        return []

def crack_sha1_hash(target_hash, password_list):
    #算時間
    start_time = time.time()
    #每個資料都用sha1來加密
    for attempt, password in enumerate(password_list, start=1):
        hashed_password = hashlib.sha1((password).encode()).hexdigest()#1-c先找出redbull再把password改成'redbull'+password
        #如果答案表加密後跟要找的依樣，那就印出答案時間和找幾次
        if hashed_password == target_hash:
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"Hash: {target_hash}")
            print(f"Password: {password}")
            print(f"Took {attempt} attempts to crack input hash. Time Taken: {time_taken:.6f} seconds")
            return
   #找不到就說失敗         
    print("Failed to crack the hash.")

def main():
    #輸入要找的hash
    hash_to_crack = "9d6b628c1f81b4795c0266c0f12123c1e09a7ad3"
    #密碼表
    password_list_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
    password_list = fetch_password_list(password_list_url)
    if password_list:
        crack_sha1_hash(hash_to_crack, password_list)

if __name__ == "__main__":
    main()
