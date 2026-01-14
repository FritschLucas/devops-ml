from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import FastAPI, APIRouter
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from api.src.services.mail_service import MailService
from api.src.models.mail import Mail
from api.src.models.classification_result import ClassificationResult  


tags_metadata = [
    {
        "name": "Health",
        "description": "Health check endpoints",
    },
    {
        "name": "mail Classification",
        "description": "Endpoints for spam mail classification",
    },
]

app = FastAPI(
    title="Spam mail API",
    description="API for spam mail classification",
    version="0.1.0",
    openapi_tags=tags_metadata,  # si tu as des tags
    docs_url="/docs",     # Swagger UI interactive
    redoc_url="/redoc",   # Redoc statique
    openapi_url="/openapi.json",  # chemin OpenAPI standard
)

# Metrics
REQUEST_COUNT = Counter(
    "app_requests_total", 
    "Total number of requests", 
    ["method", "endpoint"])
REQUEST_LATENCY = Histogram(
    "request_latency_seconds",
    "Request latency", 
    ["method", "endpoint"])

# CORS Middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Metrics Middleware
@app.middleware("http")
async def metrics_middleware(request, call_next):
    import time
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
    start = time.time()
    response = await call_next(request)
    resp_time = time.time() - start
    REQUEST_LATENCY.labels(method=request.method, endpoint=request.url.path).observe(resp_time)
    return response

router = APIRouter(
    prefix="/api",
)

@router.get("/metrics", tags=["Metrics"])
async def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

@router.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "ok"}

@router.post("/classify", tags=["Classification"], response_model=ClassificationResult)
async def classify_mail(mail: Mail):
    return MailService(mail).classify()

app.include_router(router)