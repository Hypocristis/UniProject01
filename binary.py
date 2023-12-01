def dec_to_bin(decimal_num, num_bits):
    binary_num = ""
    for _ in range(num_bits):
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num //= 2
    return binary_num

def bin_to_dec(binary_num):
    decimal_num = 0
    for digit in binary_num:
        decimal_num = decimal_num * 2 + int(digit)
    return decimal_num

print(bin_to_dec(111))