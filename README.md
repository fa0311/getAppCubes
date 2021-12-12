# getAppCubes

[getAppCubes](https://apps.moons14.com/)のPythonライブラリです<br>

## Usage

```python
from getAppCubes import getAppCubes
AppCubes = getAppCubes.getAppCubes().search('マイクラ')

# app id
print(AppCubes[0].id)
# app url
print(AppCubes[0].url)
# app is login only
print(AppCubes[0].loginonly)
# app type
print(AppCubes[0].type)
# app updated at
print(AppCubes[0].updated_at)
# ja_JP app name
print(AppCubes[0].jp.name)
# ja_JP app explanation
print(AppCubes[0].jp.explanation)
# ja_JP app tags
print(AppCubes[0].jp.tags)
```