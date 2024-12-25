from PIL import Image

def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    binary_message += '1111111111111110'

    pixels = list(img.getdata())
    encoded_pixels = []
    binary_index = 0

    for pixel in pixels:
        if binary_index < len(binary_message):
            r, g, b = pixel

            # Modify the least significant bit of the red channel
            new_r = (r & ~1) | int(binary_message[binary_index])
            binary_index += 1

            if binary_index < len(binary_message):
                # Modify the least significant bit of the green channel
                new_g = (g & ~1) | int(binary_message[binary_index])
                binary_index += 1
            else:
                new_g = g

            if binary_index < len(binary_message):
                # Modify the least significant bit of the blue channel
                new_b = (b & ~1) | int(binary_message[binary_index])
                binary_index += 1
            else:
                new_b = b

            encoded_pixels.append((new_r, new_g, new_b))
        else:
            encoded_pixels.append(pixel)

    encoded_img = Image.new(img.mode, img.size)
    encoded_img.putdata(encoded_pixels)
    encoded_img.save(output_path)

    print(f"Message encoded and saved to {output_path}")

def decode_message(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')

    pixels = list(img.getdata())
    binary_message = ''

    for pixel in pixels:
        r, g, b = pixel

        # Extract the least significant bits
        binary_message += str(r & 1)
        binary_message += str(g & 1)
        binary_message += str(b & 1)

    # Split binary message into chunks of 8 bits
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    
    decoded_message = ''
    for char in chars:
        if char == '11111110':
            break
        decoded_message += chr(int(char, 2))

    return decoded_message

# Example usage:
# Encode a message
encode_message('input_image.jpeg', 'Kaliber{st3g4n0gr4phy_1s_fun}', 'encoded_image.png')

# Decode the message
print(decode_message('encoded_image.png'))
