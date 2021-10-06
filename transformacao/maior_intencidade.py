def get_max_intensity(img):
    max = 0
    atual = 0
    
    for x in range(460):
        for y in range(690):
            atual = int(img[x,y])
            if atual > max:
                max = atual
    
    return max