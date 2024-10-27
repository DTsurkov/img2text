import requests


def send_image_for_ocr(image_path: str, server_url: str) -> dict:
    with open(image_path, "rb") as image_file:
        response = requests.post(
            server_url,
            files={"file": image_file}
        )

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    image_path = "example.png"
    server_url = "http://127.0.0.1:8000/ocr"

    try:
        result = send_image_for_ocr(image_path, server_url)
        print("Result:", result.get("text", ""))
    except Exception as e:
        print("Error:", e)
