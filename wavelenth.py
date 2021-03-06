import numpy as np

def getResultAndWavelenth(matches):
    '''get wavelength from distance of templates'''
    location = [[matches[0][0]],[matches[1][0]]]

    for i in range(1,len(matches[1])):
        if matches[0][i] - matches[0][i-1] > 20:
                break
        if matches[1][i] - matches[1][i-1] > 10:
                location[0].append(matches[0][i])
                location[1].append(matches[1][i])

    wavelenth = 0
    for i in range(1,len(location[1])):
        lenth = np.sqrt((location[1][i]-location[1][i-1])**2 + (location[0][i]-location[0][i-1])**2)

        wavelenth += lenth

        
    if len(location[1])>1:
        wavelenth /= (len(location[1]) - 1)

    return location,wavelenth

