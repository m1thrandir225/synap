import json
from typing import Annotated, Optional
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from app.storage_provider import LocalStorageProvider, get_local_storage_provider
from app.services.openai_service import OpenAIService
from app.models.summarisation_response import OpenAIServiceResponse
from app.database.db import get_db
from app.repositories.summarization_repository import SummarizationRepository
from openai import OpenAI
from sqlalchemy.orm import Session

router = APIRouter(prefix="/example_router", tags=["example_router"])


def get_openai_service() -> OpenAIService:
    return OpenAIService(OpenAI())

def get_openai_client(api_key: Optional[str] = None):
    """Creates and returns an OpenAI client."""
    return OpenAI()

@router.get("/")
def example():
    return {"text": "hello from example router"}

@router.get("/summarize1")
def summarize(client: OpenAI = Depends(get_openai_client)):    
    response = client.responses.create(
    model="gpt-4.1",
    input="Give me a short summary of postgres features."
    )
    return response

    
@router.get("/fileB64")
def fileB64(storage_provider: LocalStorageProvider = Depends(get_local_storage_provider)):
    filename="essay_engineers.pdf"
    base64_str = storage_provider.get_file_base64(filename)
    return base64_str

@router.get("/summarize")
def summarize(client: OpenAI = Depends(get_openai_client), storage_provider: LocalStorageProvider = Depends(get_local_storage_provider)):    
    filename="essay_engineers.pdf"
    encoded_content = storage_provider.get_file_base64(filename)

    response = client.responses.create(
    model="gpt-4.1-2025-04-14",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "filename": "essay_engineers.pdf",
                    "file_data": f"data:application/pdf;base64,{encoded_content}",
                },
                {
                    "type": "input_text",
                    "text": (
                        "You will receive a base64-encoded PDF file. "
                        "Please summarize its content in one paragraph. "
                        "Then, extract 3–5 key topics it discusses.\n\n"
                        "Respond in this JSON format only:\n"
                        "{\n"
                        "  \"summarization\": \"...\",\n"
                        "  \"topics\": [\"...\", \"...\"]\n"
                        "}"
                    ),
                },
            ],
        },
    ]
    )

    # try:
    #     content = response.choices[0].message.content
    #     parsed = json.loads(content)
    # except Exception as e:
    #     raise ValueError(f"Could not parse AI response as JSON: {e}")
    
    return response


def get_summarization_repo(db: Session = Depends(get_db)):
    return SummarizationRepository(db)

@router.get("/create_sum")
def create_sum(summarization_repo: Annotated[SummarizationRepository, Depends(get_summarization_repo)],):
    json_string = """
    {
    "summarization": "The essay discusses the current and future value of engineers in the global job market. It highlights the high demand and limited supply of engineers, explaining that becoming an engineer requires deep knowledge, interest, discipline, and routine, which reduces the number of qualified candidates. The essay argues that engineers add significant and often exponential value to organizations, making them highly sought after by employers. As demand increases faster than supply, the value of engineers is expected to continue rising.",
    "topics": [
        "Supply and demand of engineers",
        "Barriers to becoming an engineer",
        "Economic value of engineers in organizations",
        "Future trends in engineering careers"
    ]
    }
    """

    parsed_json = json.loads(json_string)

    try:
        summarization_data = {
            "summarization_text": parsed_json["summarization"],
            "topics": parsed_json["topics"],
        }
        new_summarization = summarization_repo.create(summarization_data)
        return new_summarization
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create summarization: {e}",
        )

