def charRange (stop, start, step=1):
    stopModifier = 1
    startCode = ord(start)
    stopCode = ord(stop)
    
    if startCode > stopCode:
        step *= -1
        stopModifier *= -1
    
    for value in range( startCode, stopCode + stopModifier, step):
        yield chr(value)