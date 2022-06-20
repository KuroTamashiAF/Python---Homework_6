import view_data
import encode_block
import decode_data
import Rewrite

def compression():
    data = view_data.enter_from_user()
    encode_block.encode(data)
    view_data.view(encode_block.encode(data)+' Сжатые данные')
    Rewrite.write_in_file(encode_block.encode(data))
    print('-'*30)
    recovery_data = encode_block.encode(data)
    decode_data.decode(recovery_data)
    view_data.view(decode_data.decode(recovery_data)+' восстановленные данные')
