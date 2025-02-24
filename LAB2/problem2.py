import hashlib
import time
import requests

def calculate_checksum(file_path, hash_function):
    #使用特定的hashfuction來創建
    hasher = hashlib.new(hash_function)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def compare_hash_speeds(file_path):
    #不童的hash fuc
    hash_functions = ['md5', 'sha1', 'sha224', 'sha256', 'sha512', 'sha3_224', 'sha3_256', 'sha3_512']

    print(f"Calculating checksums for {file_path}")
    #算時間
    for hash_function in hash_functions:
        start_time = time.time()
        checksum = calculate_checksum(file_path, hash_function)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{hash_function.upper()}: {checksum}")
        print(f"Time taken: {elapsed_time:.6f} seconds\n")

if __name__ == "__main__":
    video_url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
    video_file_path = "BigBuckBunny.mp4"

    response = requests.get(video_url)
    #讀影片
    with open(video_file_path, 'wb') as video_file:
        video_file.write(response.content)

    compare_hash_speeds(video_file_path)
