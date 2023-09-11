import random
import string

def generate_id(length: int = 4):
    return ''.join(random.choices(string.ascii_letters, k=length))

def success_flash_msg(id: str, full_url:str):
    return f"""
    <h2>
        Success!
    </h2>
    <p>
        ID: <strong>{id}</strong>. Link:
    </p>
    <div class="input-group mb-3">
        <input id="full_url" type="text" class="form-control" readonly
        value="{full_url}">
        <button class="btn btn-outline-dark" type="button" id="full_url_copy" data-clipboard-target="#full_url">Copy</button>
    </div>

    <script>
        new ClipboardJS("#full_url_copy");
    </script>
    """
