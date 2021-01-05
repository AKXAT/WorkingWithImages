#program to mask two images 

from PIL import Image
chess = Image.open('G:\\black.jpg')
alpha = Image.open('G:\\letters.png')
#print("the chess size is {}".format(chess.size))
#print("the alpha size is {}".format(alpha.size))
resize_alpha = alpha.resize((chess.size))
chess.putalpha(100)
resize_alpha.putalpha(100)
chess.paste(im=resize_alpha,box=(0,0),mask=resize_alpha)
chess.show()