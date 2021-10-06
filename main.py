# Import FastAPI
from fastapi import FastAPI
from routers import users
from fastapi.staticfiles import StaticFiles
import uvicorn
import config

# new FastAPI
app = FastAPI(
    title="UserApp",
    description='fastapi user service',
    version=config.PROJECT_VERSION,
    contact={
        "name": "yongfeiuall",
        "url": "http://izheyi.com",
        "email": "yongfeiuall@163.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users.router)


if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host=config.HOST,
        port=config.PORT
    )

