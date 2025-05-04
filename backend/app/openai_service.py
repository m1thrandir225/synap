import base64
from typing import Dict
from openai import OpenAI


class OpenAIService:
    def __init__(self, client: OpenAI):
        self.client = client

    def summarize_pdf(self, filename: str, file_content: bytes) -> Dict:
        encoded_content = base64.b64encode(file_content).decode("utf-8")
        prompt = (
            "You will receive a PDF file. Summarize it briefly. "
            "Then, list 3–5 key topics it discusses."
        )

        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt,
                        },
                        {
                            "type": "file",
                            "file_data": {
                                "file_name": filename,
                                "file_type": "application/pdf",
                                "data": encoded_content,
                            },
                        },
                    ],
                }
            ]
        )

        content = response.choices[0].message.content
        if not content:
            raise ValueError("No content returned from OpenAI.")

        summary_part, _, topics_part = content.partition("Topics:")
        summary = summary_part.replace("Summary:", "").strip()
        topics = [t.strip() for t in topics_part.strip().split(",") if t]

        return {
            "summarization": summary,
            "topics": topics,
        }
