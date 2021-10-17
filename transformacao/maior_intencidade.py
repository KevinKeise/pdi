# obtem o maior pixel em uma imagem
def get_max_intensity(img):
    max = 0
    atual = 0
    
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            atual = int(img[x,y])
            if atual > max:
                max = atual
    
    return max