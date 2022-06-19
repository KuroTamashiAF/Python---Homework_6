def encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''

    for char in data:
        if char != prev_char:                                  # тут понятно что если символы не совпадают тогда заходим в ветвление и идем ниже
            if prev_char:                                      # хоть убивайте ну не пойму я такую запись!!!если переменаая ЧТО??? тогда выполняй это !!
                encoding += str(count) + prev_char             # какое тут условие?? 
            count = 1
            prev_char = char
        else:
            count+=1
    else:
        encoding+=str(count)+prev_char
        return encoding
