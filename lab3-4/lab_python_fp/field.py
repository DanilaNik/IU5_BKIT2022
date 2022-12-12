def field(items, *args):
    if len(args) == 1:
        arr = []
        for item in items:
            for key in item:
                if key == args[0] and item[key] is not None:
                    arr.append(item[key])
        return arr                    
    else:
        for item in items:
            dictionary = dict()
            for key in item:
                for argument in args:
                   if key == argument and item[argument] is not None:
                       dictionary[key] = item[key]
        return(dictionary)

def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    # должен выдавать 'Ковер', 'Диван для отдыха'.
    res = (field(goods, 'title'))
    for el in res:
        print(el , end = '; ')
    print()    
    # должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}.
    print(field(goods, 'title', 'price'))

if __name__ == '__main__':
    main()