import jwt
import time
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

JWT_SECRET = "SECRET_KEY"
JWT_ALGORITHM = "HS256"

security = HTTPBearer()

#JWT
def create_token(user_id: str) -> str:
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        payload = jwt.decode(
            credentials.credentials,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM]
        )
        return payload["sub"]
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

#Rate limiting
RATE_LIMIT = 5
WINDOW = 60  
requests_log = {}

def rate_limiter(request: Request):
    ip = request.client.host
    now = time.time()

    timestamps = requests_log.get(ip, [])
    timestamps = [t for t in timestamps if now - t < WINDOW]

    if len(timestamps) >= RATE_LIMIT:
        retry_after = int(WINDOW - (now - timestamps[0]))
        raise HTTPException(
            status_code=429,
            detail="Too many requests",
            headers={
                "Retry-After": str(retry_after),
                "X-Limit-Remaining": "0"
            }
        )

    timestamps.append(now)
    requests_log[ip] = timestamps

    request.state.remaining = RATE_LIMIT - len(timestamps)
