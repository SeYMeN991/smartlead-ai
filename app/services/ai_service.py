import requests 
import config

class AIServiceError(Exception):
    pass

class AIService():
    def _business_context(self):
        return config.BUSINESS_CONTEXT

    def _ai_istek(self,messages):
        try:
            headers = {
                    "Authorization": f"Bearer {config.GROQ_API_KEY}",
                    "Content-Type": "application/json"
            }
            payload = {
                "model": "openai/gpt-oss-20b",
                "messages": messages
            }
            response = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers=headers,
                    json=payload
            )

            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        
        except Exception as e:
            raise AIServiceError(str(e))

    def yanit_uret(self, mesaj, gecmis):
        if not config.GROQ_API_KEY:
            return "Demo mod"

        messages = [{"role": "system", "content": self._business_context() }]

        messages.extend(gecmis)

        messages.append({"role":"user","content": mesaj})

        return self._ai_istek(messages)

ai_service = AIService()
