import pyzipper
import codecs

PASSWORD_FILE = "password.txt"  # 密码保存文件名
MAX_PASSWORD_LENGTH = 10  # 最大密码长度
CHARACTERS = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+=-[]{}\\|,.<>"  # 所有可能的字符
zip_file_path = "your_zip_file_path" #需要解压的文件全路径

def try_password(zip_file, password):
    try:
        with pyzipper.AESZipFile(zip_file) as zf:
            zf.extractall(pwd=password.encode())
        return True
    except Exception as e:
        return False
    
def unzip_zipfile_with_password(zip_file_path, password):
    success = try_password(zip_file_path, password)
    return success

def operate_index(index):
    carry = 1
    result = []
    for i in range(len(index) - 1, -1, -1):
        num = index[i] + carry
        if num > len(CHARACTERS) - 1:
            num = num % len(CHARACTERS)
            carry = 1
        else:
            carry = 0
        result.insert(0, num)
    if carry == 1:
        result.insert(0, 0)
    return result


def string_builder_to_index_list(sb):
    index_list = []
    for ch in sb:
        index = CHARACTERS.find(ch)
        if index >= 0:
            index_list.append(index)
    return index_list


def index_list_to_string_builder(index_list):
    sb = ""
    for index in index_list:
        if 0 <= index < len(CHARACTERS):
            ch = CHARACTERS[index]
            sb += ch
    return sb


def read_previous_index():
    try:
        with open(PASSWORD_FILE, "r") as file:
            lines = file.readlines()
            if len(lines) > 0:
                previous_password = lines[-1].strip()
                return previous_password
    except IOError:
        print("无法读取最新索引。")
    return ""


def generate_passwords(previous_index, index_list):
    string_builder = index_list_to_string_builder(index_list)
    # if string_builder == previous_index:
    #     print("密码重复，跳过")
    #     return False
    with open(PASSWORD_FILE, "w") as file:

        if try_password(zip_file_path, string_builder):
            print(f"Success! Password is {string_builder}")
            file.write(string_builder + "\n")
            return True
        else:
            print("Password error:", string_builder)
            file.write(string_builder + "\n")
            return False


if __name__ == "__main__":
    index = [0]
    previous_index = read_previous_index()
    index = string_builder_to_index_list(previous_index)
    while len(index) < MAX_PASSWORD_LENGTH:
        if generate_passwords(previous_index, index):
            break
        else:
            index = operate_index(index)

