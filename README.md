# hello world with fast api
1. poetry new foldername --name subfoldername

2. cd foldername

3. open VS code (code .)

4. open file 'pyproject.toml'

    '''
    [tool.poetry]
    name = "fast"
    version = "0.1.0"
    description = ""
    authors = ["suhaibshaikh03 <160228973+suhaibshaikh03@users.noreply.github.com>"]
    readme = "README.md"

    [tool.poetry.dependencies]
    python = "^3.12"


    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"

    '''

5. install new packages in poetry project
    'poetry add fastapi "uvicorn[standard]"

    '''
    [tool.poetry.dependencies]
    python = "^3.12"
    fastapi = "^0.111.0"
    uvicorn = {extras = ["standard"], version = "^0.30.1"}
    '''

6. create 'main.py' location 'fast\main.py'

7. run server
'poetry run uvicorn fast.main:app --reload' 

8. http://127.0.0.1:8000/

9. http://127.0.0.1:8000/docs #swagger home server

10. poetry run pytest -v (for pytest)