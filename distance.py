##传入2s移动的步数count,已移动的距离distance,身高
def Distance(float count,int distance, float tall, float F = 1):
    F = count / 2

    if(tall < 1.6 and tall > 1.5 ):
        if( F <= 1.35):
            S = 0.38
        if( F > 1.35 and F < 2.45):
            S = 0.45 * F - 0.23
        else:
            S = 0.87

    if(tall < 1.7 and tall > 1.6 ):
        if( F <= 1.35):
            S = 0.43
        if( F > 1.35 and F < 2.45):
            S = 0.45 * F - 0.17
        else:
            S = 0.93

    if(tall < 1.8 and tall > 1.7 ):
        if( F <= 1.35):
            S = 0.51
        if( F > 1.35 and F < 2.45):
            S = 0.45 * F - 0.1
        else:
            S = 1.0

    if(tall < 2 and tall > 1.8 ):
        if( F <= 1.35):
            S = 0.61
        if( F > 1.35 and F<2.45):
            S = 0.45 * F - 0.01
        else:
            S = 1.09

    distance = distance + S * count

    return distance
    
    
