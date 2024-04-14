import io


def save_buffer(buffer: io.BytesIO, file_path: str) -> str:
    with open(file_path, "wb") as f:
        f.write(buffer.getbuffer())

    return file_path
