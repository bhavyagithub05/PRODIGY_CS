from PIL import Image

#load the image
image = Image.open("input_image.webp")

# display the image (optional)
image.show()
def swap_pixels(image):
    pixels = image.load()
    width,height =image.size

    for y in range(height):
       for x in range(0,width,2):
         if x+1 < width:
            #swap pixel with the next one
            pixels[x,y], pixels[x+1,y] = pixels[x+1,y],pixels[x,y]

    return image
def xor_pixels(image,key):
    pixels = image.load()
    width,height=image.size

    for y in range(height):
        for x in range(width):
           r,g,b = pixels[x,y]
           #apply xor operaton with the key
           pixels[x,y]=(r ^ key,g ^ key,b ^ key)

    return image

#encypt the image
def encrypt_image(image,key):
   image = swap_pixels(image)
   image = xor_pixels(image,key)
   return image

#decrypt  the image
def decrypt_image(image,key):
   image = xor_pixels(image,key)
   image = swap_pixels(image)
   return image

if __name__ == "__main__":
   image = Image.open("input_image.webp")

   key = 123 #example key for xor operation

   encrypted_image = encrypt_image(image.copy(),key)
   encrypted_image.save("encrypted_image.png")
   encrypted_image.show()#display the encypted image


   decrypted_image = decrypt_image(encrypted_image.copy(),key)
   decrypted_image.save("decrypted_image.png")
   decrypted_image.show() #display the decrypted image



