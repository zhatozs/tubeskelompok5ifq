from browser import document, console, alert

input = document['input']
button = document['btn']
output = document['output']
select = document['select']

def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan angka')
            temp = ''
            input.value = temp
            return temp
        else:
            return temp

def formula(x, y):
    match x:
        case 'Baju':
            return y * 30000
        case 'Celana':
            return y * 25000
        case 'Dasi':
            return y * 10000
        case 'Topi':
            return y * 15000
        case 'Jaket':
            return y * 50000
        case _:        
            return 0


def main(ev):
    num = getNum(input.value)
    result = formula(select.value, num)
    output.textContent = str(result)

def keyEnter(ev):
    console.log(f"{ev.code}")
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

button.bind('click', main)
input.bind("keypress", keyEnter)
