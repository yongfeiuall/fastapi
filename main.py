# 导入 FastAPI
from fastapi import FastAPI
from routers import users
import uvicorn
import config

# 实例化 FastAPI
app = FastAPI(
    title="UserApp",
    description='fastapi demo',
    version=config.VERSION,
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

app.include_router(users.router)

if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host=config.HOST,
        port=config.PORT
    )

