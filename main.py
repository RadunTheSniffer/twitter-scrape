from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from scraper import scrape_data  # Import the scrape_data function

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/output', response_class=HTMLResponse)
def submit(request: Request, topic: str = Form(...)):
    link = f"https://twstalker.com/search/{topic.replace(' ', '%20')}"
    print(f"Scraping link: {link}")  # Debugging statement
    scraped_data = scrape_data(link)
    print(f"Scraped data: {scraped_data}")  # Debugging statement
    return templates.TemplateResponse("output.html", {"request": request, "topic": topic, "scraped_data": scraped_data})

if __name__ == "__main__":
    uvicorn.run("main:app", port=3000, log_level="info")

