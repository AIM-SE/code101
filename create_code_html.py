import os

def create_block(path, name):
    res = ''
    with open(os.path.join(path, name+".py")) as f:
        res += '<code data-type="' + name +'">' + os.linesep
        res += f.read()
        res += '</code>' + os.linesep

    return res

def create(head, example, tail):
    path = os.path.join('code', example)
    res = head

    # working on sample code
    res += '<code data-type="sample-code">' + os.linesep
    with open(os.path.join(path, 'sample.py')) as f:
        res += f.read()
    res += '</code>' + os.linesep

    res += create_block(path, "solution")
    res += create_block(path, "sct")
    res += create_block(path, "hint")

    return res + tail


with open('head.html') as f: head = f.read()
with open('tail.html') as f: tail = f.read()

for example in os.listdir('code/'):
    res = create(head, example, tail)
    with open(os.path.join('doc', example + ".html"), "w") as f:
        f.write(res)
