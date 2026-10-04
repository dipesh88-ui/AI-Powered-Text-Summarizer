import os
import re

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

app = FastAPI(title="Text Summarizer App", description="Text Summarization using T5", version="1.0")

MODEL_DIR = "./saved_summary_model"
FALLBACK_MODEL = "t5-small"

if os.path.isdir(MODEL_DIR) and os.path.exists(os.path.join(MODEL_DIR, "config.json")):
    model_path = MODEL_DIR
else:
    model_path = FALLBACK_MODEL

model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = T5Tokenizer.from_pretrained(model_path)

if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model.to(device)
model.eval()

templates = Jinja2Templates(directory=".")


class DialogueInput(BaseModel):
    dialogue: str


def clean_data(text):
    text = re.sub(r"\r\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = text.strip().lower()
    return text


def summarize_dialogue(dialogue: str) -> str:
    cleaned = clean_data(dialogue)
    if not cleaned:
        return "Please enter some text to summarize."

    prefixed_input = "summarize: " + cleaned
    inputs = tokenizer(
        prefixed_input,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt",
    ).to(device)

    with torch.no_grad():
        generated_ids = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=150,
            num_beams=4,
            early_stopping=True,
        )

    summary = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return summary.strip() or "No summary generated."


@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    summary = summarize_dialogue(dialogue_input.dialogue)
    return {"summary": summary}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")