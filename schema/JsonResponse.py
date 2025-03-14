from fastapi.responses import JSONResponse
import json

class JsonResponse(JSONResponse):
    def render(self, content: any) -> bytes:
        return json.dumps(content, ensure_ascii=False).encode("utf-8")
