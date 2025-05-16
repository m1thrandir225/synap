from app.models.summarization import OpenAIServiceResponse
from openai import OpenAI, OpenAIError
import json
from app.config import settings 
import re

class OpenAIService:
    def __init__(self, api_key: str = settings.OPENAI_API_KEY):
        if not api_key:
            raise ValueError("OpenAI API key is not configured.")
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4.1-2025-04-14"

    def get_summary_and_topics_from_base64_content(
        self,
        filename: str,
        base64_content: str,
        file_mime_type: str = "application/pdf"
    ) -> OpenAIServiceResponse:
        prompt_text = (
            "You will receive a base64-encoded file. "
            "Please summarize its content in one paragraph. Less than 255 characters."
            "Then, extract 3–5 key topics it discusses.\n\n"
            "Respond in this JSON format only:\n"
            "{\n"
            "  \"summarization\": \"...\",\n"
            "  \"topics\": [\"...\", \"...\"]\n"
            "}"
        )
        try:
            response = self.client.chat.completions.create( 
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt_text
                            },
                            {
                                "type": "text",
                                "text": f"The following is the content of '{filename}' encoded in base64: data:{file_mime_type};base64,{base64_content}"
                            }
                
                        ],
                    }
                ],
                response_format={"type": "json_object"}
            )

            content_str = response.choices[0].message.content
            if not content_str:
                raise ValueError("OpenAI returned an empty content string.")

            parsed_json = json.loads(content_str)
            parsed_json["query"] = prompt_text  # Or another useful value
            return OpenAIServiceResponse(**parsed_json)

        except OpenAIError as e:
            raise Exception(f"OpenAI API error: {e}") 
        except json.JSONDecodeError as e:
            raise ValueError(f"Could not parse AI response as JSON: {e}. Response: {content_str}")
        except Exception as e:
            raise ValueError(f"Error processing OpenAI response: {e}")
        
    def get_learning_materials_for_topics(self, topics: list[str]) -> list[dict]:
        # search_prompt = {
        #     "role": "user",
        #     "content": (
        #         f"Based on these topics: {topics}. "
        #         "Can you give me relevant YouTube videos and articles to continue my learning journey on these topics? "
        #         "Respond only with a JSON object in this structure:\n"
        #         "{\n"
        #         "  \"title\": \"string\",\n"
        #         "  \"description\": \"string\",\n"
        #         "  \"url\": \"string\",\n"
        #         "  \"material_type\": \"string\" // 'article' or 'video'\n"
        #         "}\n"
        #         "Respond in JSON format only."
        #     )
        # }
        search_prompt = {
            "role": "user",
            "content": (
                f"Based on these topics: {topics}. "
                "Can you give me a list of relevant YouTube videos and articles to continue my learning journey on these topics? "
                "Include a 'relevance_score' between 0 and 1 indicating how relevant each resource is to the topics. "
                "Respond only with a JSON object in this structure:\n"
                "{\n"
                "  \"resources\": [\n"
                "    {\n"
                "      \"title\": \"string\",\n"
                "      \"description\": \"string\",\n"
                "      \"url\": \"string\",\n"
                "      \"material_type\": \"string\" // 'article' or 'video'\n"
                "      \"relevance_score\": float // value between 0 and 1\n"
                "    }\n"
                "  ]\n"
                "}\n"
                "Respond in JSON format only."
            )
        }


        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-search-preview",
                messages=[search_prompt]
            )
            
            content_str = response.choices[0].message.content.strip()

            # Remove Markdown code block if it exists
            if content_str.startswith("```json") or content_str.startswith("```"):
                content_str = re.sub(r"^```(?:json)?\s*", "", content_str)
                content_str = re.sub(r"\s*```$", "", content_str)

            # Now parse the cleaned JSON
            parsed_json = json.loads(content_str)
            materials = parsed_json.get("resources", [])

            if isinstance(materials, dict):
                return [materials]
            return materials

        except OpenAIError as e:
            raise Exception(f"OpenAI API error: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Could not parse AI response as JSON: {e}. Response: {content_str}")
        except Exception as e:
            raise ValueError(f"Error processing OpenAI search response: {e}")
