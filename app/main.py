from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.recommender import MovieRecommender
from app.graph_builder import AStarGraph
from app.utils import draw_interactive_graph

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

rec = MovieRecommender("data/imdb_top_1000.csv")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/recommend", response_class=HTMLResponse)
def recommend(request: Request, movie: str):
    results = rec.recommend(movie)

    graph = AStarGraph(results)
    start = results[0]['title']
    goal = results[-1]['title']
    path = [m['title'] for m in results]

    draw_interactive_graph(graph.graph, start, goal, path)

    return templates.TemplateResponse("results.html", {
        "request": request,
        "movies": results
    })
