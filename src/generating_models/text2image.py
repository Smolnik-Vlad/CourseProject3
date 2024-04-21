import httpx

api_key = "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"
API_URL = (
    "https://api-inference.huggingface.co/"
    "models/stabilityai/stable-diffusion-2-1"
)
headers = {"Authorization": f"Bearer {api_key}"}


async def get_image_from_text(prompt: str):
    payload = {"inputs": prompt}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            API_URL, headers=headers, json=payload, timeout=None
        )
        # image = Image.open(io.BytesIO(response.content))
    return response.content
