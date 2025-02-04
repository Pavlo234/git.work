def namber(a,b):
    return a + b

def get_los_angeles_points(results):
    los_angeles_result = 0
    for name, score in results:
        if name.startswith('Los Angeles '):
            a = name.split()
            if len(a) == 3 and a[2][0].isupper() and a[2].isalpha() and a[2][1:].islower():
                split_score = score.split(':')

                los_angeles_result += int(split_score[0])
    return los_angeles_result     
