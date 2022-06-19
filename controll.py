import view_data
import encode_block


def performance():
    data = view_data.enter_from_user()
    encode_block.encode(data)
    view_data.view(encode_block.encode(data))

    