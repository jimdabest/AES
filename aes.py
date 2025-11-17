# --- BƯỚC 1: ĐỊNH NGHĨA CÁC HẰNG SỐ (S-box và Rcon) ---
# -----------------------------------------------------------------

# S-box
s_box = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

# Inverse S-box (Bảng thay thế nghịch đảo dung cho giải mã)
inv_s_box = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]

# Rcon (Hằng số vòng)
# Rcon[0] không dùng, Rcon[1] dùng cho Vòng 1, v.v.
Rcon = [
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36
]


# --- BƯỚC 2: CÁC HÀM HỖ TRỢ (Toán học GF(2^8) và Chuyển đổi) ---
# -----------------------------------------------------------------

def bytes_to_matrix(data):
    """Chuyển đổi 16 byte thành ma trận State 4x4 (theo cột)."""
    state = []
    for r in range(4):
        state.append([data[r + 4 * c] for c in range(4)])
    return state

def matrix_to_bytes(state):
    """Chuyển đổi ma trận State 4x4 về 16 byte (theo cột)."""
    data = bytearray(16)
    for r in range(4):
        for c in range(4):
            data[r + 4 * c] = state[r][c]
    return bytes(data)

def gmul_by_02(a):
    """Phép nhân với 02 trong trường GF(2^8).
       Chính là (dịch trái 1) và (XOR 0x1b nếu bị tràn).
    """
    if a < 0x80:
        # Nếu bit cao nhất là 0, chỉ cần dịch trái
        res = (a << 1)
    else:
        # Nếu bit cao nhất là 1, dịch trái và XOR 0x1b
        res = (a << 1) ^ 0x1b
    return res & 0xFF  # Đảm bảo kết quả luôn là 1 byte

def gmul_by_03(a):
    """Phép nhân với 03.
       03 * a = (02 * a) XOR (01 * a)
    """
    return gmul_by_02(a) ^ a

def gmul_by_09(a):
    """Phép nhân với 09 trong trường GF(2^8)."""
    return gmul_by_02(gmul_by_02(gmul_by_02(a))) ^ a

def gmul_by_0b(a):
    """Phép nhân với 0b trong trường GF(2^8)."""
    return gmul_by_02(gmul_by_02(gmul_by_02(a))) ^ gmul_by_02(a) ^ a

def gmul_by_0d(a):
    """Phép nhân với 0d trong trường GF(2^8)."""
    return gmul_by_02(gmul_by_02(gmul_by_02(a))) ^ gmul_by_02(gmul_by_02(a)) ^ a

def gmul_by_0e(a):
    """Phép nhân với 0e trong trường GF(2^8)."""
    return gmul_by_02(gmul_by_02(gmul_by_02(a))) ^ gmul_by_02(gmul_by_02(a)) ^ gmul_by_02(a)


# --- BƯỚC 3: CÁC HÀM CỦA 4 BƯỚC MÃ HÓA (1 VÒNG) ---
# -----------------------------------------------------------------

def sub_bytes(state):
    """Bước 1: SubBytes (Thay thế Byte).
       Tra S-box cho từng byte trong State.
    """
    for r in range(4):
        for c in range(4):
            state[r][c] = s_box[state[r][c]]
    return state

def shift_rows(state):
    """Bước 2: ShiftRows (Dịch Hàng)."""
    # Hàng 0: không dịch
    
    # Hàng 1: dịch trái 1
    state[1] = state[1][1:] + state[1][:1]
    
    # Hàng 2: dịch trái 2
    state[2] = state[2][2:] + state[2][:2]
    
    # Hàng 3: dịch trái 3
    state[3] = state[3][3:] + state[3][:3]
    
    return state

def mix_columns(state):
    """Bước 3: MixColumns (Trộn Cột).
       Nhân từng cột với Ma trận Cố định.
    """
    for c in range(4):
        # Lấy giá trị cột cũ
        s0 = state[0][c]
        s1 = state[1][c]
        s2 = state[2][c]
        s3 = state[3][c]
        
        state[0][c] = gmul_by_02(s0) ^ gmul_by_03(s1) ^ s2            ^ s3
        state[1][c] = s0            ^ gmul_by_02(s1) ^ gmul_by_03(s2) ^ s3
        state[2][c] = s0            ^ s1            ^ gmul_by_02(s2) ^ gmul_by_03(s3)
        state[3][c] = gmul_by_03(s0) ^ s1            ^ s2            ^ gmul_by_02(s3)
        
    return state

def add_round_key(state, round_key_matrix):
    """Bước 4: AddRoundKey (Cộng Khóa Vòng).
       XOR State với Khóa Vòng hiện tại.
    """
    for r in range(4):
        for c in range(4):
            state[r][c] = state[r][c] ^ round_key_matrix[r][c]
    return state


# --- BƯỚC 4: MỞ RỘNG KHÓA (KEY EXPANSION) ---
# -----------------------------------------------------------------

def expand_key(master_key):
    """Từ Key 16 byte, tạo ra 11 Khóa Vòng (tổng 176 byte)."""
    
    # Khởi tạo 176 byte (44 words)
    key_schedule = bytearray(176)
    key_schedule[0:16] = master_key  # Key 0
    
    # 1 word = 4 byte
    bytes_generated = 16  # Đã có 16 byte
    rcon_index = 1      # Bắt đầu với Rcon[1]

    while bytes_generated < 176:
        
        # Lấy 4 byte trước đó (word cuối)
        temp_word = list(key_schedule[bytes_generated - 4 : bytes_generated])
        
        # Đây là cột đầu tiên của Khóa Vòng mới (ví dụ: w[4], w[8],...)
        # Cần áp dụng RotWord, SubWord, và XOR Rcon
        if bytes_generated % 16 == 0:
            
            # 1. RotWord (Xoay trái 1 byte)
            # [b0, b1, b2, b3] -> [b1, b2, b3, b0]
            temp_word = temp_word[1:] + temp_word[:1]
            
            # 2. SubWord (Tra S-box)
            for i in range(4):
                temp_word[i] = s_box[temp_word[i]]
                
            # 3. XOR Rcon
            temp_word[0] = temp_word[0] ^ Rcon[rcon_index]
            rcon_index += 1

        # Lấy 4 byte của 16 byte trước đó (word tương ứng ở Khóa Vòng trước)
        prev_word = key_schedule[bytes_generated - 16 : bytes_generated - 12]
        
        # XOR `temp_word` với `prev_word` để tạo word mới
        for i in range(4):
            key_schedule[bytes_generated + i] = prev_word[i] ^ temp_word[i]
            
        bytes_generated += 4
        
    # Trả về toàn bộ 11 khóa vòng (dưới dạng list 11 ma trận 4x4)
    round_keys = []
    for i in range(11):
        key_bytes = key_schedule[i * 16 : (i + 1) * 16]
        round_keys.append(bytes_to_matrix(key_bytes))
        
    return round_keys


# --- BƯỚC 5: HÀM MÃ HÓA CHÍNH (AES-128-ECB) ---
# -----------------------------------------------------------------

def aes_encrypt(plaintext, key):
    """Thực hiện mã hóa AES-128-ECB cho MỘT block 16 byte."""
    
    if len(plaintext) != 16:
        raise ValueError("Plaintext phải dài đúng 16 byte cho ECB 1 block")
    if len(key) != 16:
        raise ValueError("Key phải dài đúng 16 byte cho AES-128")

    # 1. Mở rộng khóa thành 11 Khóa Vòng
    round_keys = expand_key(key)
    
    # 2. Chuyển plaintext thành State
    state = bytes_to_matrix(plaintext)
    
    # 3. Vòng 0: Chỉ AddRoundKey
    state = add_round_key(state, round_keys[0])
    
    # 4. Vòng 1 đến 9: 4 bước
    for i in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[i])
        
    # 5. Vòng 10 (Vòng cuối): 3 bước (BỎ QUA MixColumns)
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[10])
    
    # 6. Chuyển State về lại 16 byte
    ciphertext = matrix_to_bytes(state)
    return ciphertext


# --- BƯỚC 6: CÁC HÀM NGHỊCH ĐẢO CHO GIẢI MÃ ---
# -----------------------------------------------------------------

def inv_sub_bytes(state):
    """Bước nghịch đảo của SubBytes.
       Tra inverse S-box cho từng byte trong State.
    """
    for r in range(4):
        for c in range(4):
            state[r][c] = inv_s_box[state[r][c]]
    return state

def inv_shift_rows(state):
    """Bước nghịch đảo của ShiftRows.
       Dịch phải thay vì dịch trái.
    """
    # Hàng 0: không dịch
    
    # Hàng 1: dịch phải 1 (tương đương dịch trái 3)
    state[1] = state[1][3:] + state[1][:3]
    
    # Hàng 2: dịch phải 2 (tương đương dịch trái 2) 
    state[2] = state[2][2:] + state[2][:2]
    
    # Hàng 3: dịch phải 3 (tương đương dịch trái 1)
    state[3] = state[3][1:] + state[3][:1]
    
    return state

def inv_mix_columns(state):
    """Bước nghịch đảo của MixColumns.
       Nhân từng cột với Ma trận Nghịch đảo.
    """
    for c in range(4):
        # Lấy giá trị cột cũ
        s0 = state[0][c]
        s1 = state[1][c]
        s2 = state[2][c]
        s3 = state[3][c]
        
        state[0][c] = gmul_by_0e(s0) ^ gmul_by_0b(s1) ^ gmul_by_0d(s2) ^ gmul_by_09(s3)
        state[1][c] = gmul_by_09(s0) ^ gmul_by_0e(s1) ^ gmul_by_0b(s2) ^ gmul_by_0d(s3)
        state[2][c] = gmul_by_0d(s0) ^ gmul_by_09(s1) ^ gmul_by_0e(s2) ^ gmul_by_0b(s3)
        state[3][c] = gmul_by_0b(s0) ^ gmul_by_0d(s1) ^ gmul_by_09(s2) ^ gmul_by_0e(s3)
        
    return state


# --- BƯỚC 7: HÀM GIẢI MÃ CHÍNH (AES-128-ECB) ---
# -----------------------------------------------------------------

def aes_decrypt(ciphertext, key):
    """Thực hiện giải mã AES-128-ECB cho MỘT block 16 byte."""
    
    if len(ciphertext) != 16:
        raise ValueError("Ciphertext phải dài đúng 16 byte cho ECB 1 block")
    if len(key) != 16:
        raise ValueError("Key phải dài đúng 16 byte cho AES-128")

    # 1. Mở rộng khóa thành 11 Khóa Vòng (giống như mã hóa)
    round_keys = expand_key(key)
    
    # 2. Chuyển ciphertext thành State
    state = bytes_to_matrix(ciphertext)
    
    # 3. Vòng 10: AddRoundKey với khóa vòng cuối
    state = add_round_key(state, round_keys[10])
    
    # 4. Vòng 9 đến 1: 4 bước nghịch đảo (thứ tự ngược lại)
    for i in range(9, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, round_keys[i])
        state = inv_mix_columns(state)
        
    # 5. Vòng 0 (Vòng cuối): 3 bước (BỎ QUA InvMixColumns)
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, round_keys[0])
    
    # 6. Chuyển State về lại 16 byte
    plaintext = matrix_to_bytes(state)
    return plaintext


# --- CHẠY VÍ DỤ (Dùng dữ liệu của chúng ta) ---
# -----------------------------------------------------------------

if __name__ == "__main__":
    # --- Dữ liệu đầu vào ---
    key_str = "PHAMNGUYEN062006"
    plaintext_str = "TGIAOTHONGVANTAI"
    
    key_bytes = key_str.encode('utf-8')
    plaintext_bytes = plaintext_str.encode('utf-8')

    print("--- QUÁ TRÌNH MÃ HÓA (Python thuần túy) ---")
    print(f"Plaintext (văn bản): {plaintext_str}")
    print(f"Plaintext (hex):    {plaintext_bytes.hex()}")
    print(f"Key (văn bản):      {key_str}")
    print(f"Key (hex):          {key_bytes.hex()}")
    
    # --- Thực hiện mã hóa ---
    try:
        ciphertext_bytes = aes_encrypt(plaintext_bytes, key_bytes)
        
        # In kết quả
        print("\n--- KẾT QUẢ (CIPHERTEXT) ---")
        hex_result = ciphertext_bytes.hex()
        print(f"Ciphertext (dạng hex): {hex_result}")

        # Định dạng thành ma trận 4x4 (đọc theo cột)
        print("\nCiphertext (dạng ma trận 4x4 - đọc theo cột):")
        matrix = bytes_to_matrix(ciphertext_bytes)
        for r in range(4):
            print(f"{matrix[r][0]:02x} {matrix[r][1]:02x} {matrix[r][2]:02x} {matrix[r][3]:02x}")    

        # --- Thực hiện giải mã để kiểm tra ---
        decrypted_bytes = aes_decrypt(ciphertext_bytes, key_bytes)
        decrypted_str = decrypted_bytes.decode('utf-8')
        print("\n--- QUÁ TRÌNH GIẢI MÃ ---")
        print(f"Decrypted Plaintext (văn bản): {decrypted_str}")    
    except ValueError as ve:
        print(f"Lỗi: {ve}")