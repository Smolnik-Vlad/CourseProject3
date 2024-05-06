import async_google_trans_new
import httpx

api_key = "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"
API_URL = (
    "https://api-inference.huggingface.co/"
    "models/Salesforce/blip-image-captioning-large"
)
headers = {"Authorization": f"Bearer {api_key}"}


async def get_text_from_image(file_bytes):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            API_URL, headers=headers, data=file_bytes, timeout=None
        )
        text = response.json()[0]["generated_text"]
        g = async_google_trans_new.AsyncTranslator()
        ru_text = await g.translate(text, "ru")
    return ru_text
