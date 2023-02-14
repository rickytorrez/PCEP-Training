# generators -> functions that behave like iterators
# similar to range

# yield, similar to return but it pauses until we ask for the next item
def genRange (stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step

# uses to the next() built in to call the next iterator