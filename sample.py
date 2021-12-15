
from getAppCubes import getAppCubes

def dump(text, var):
    print('  '.join([text, str(type(var)), str(var)]))
    
if __name__ == '__main__':
    print('Enter the app name')
    query = input()
    AppCubes = getAppCubes.getAppCubes().search(query=query, count=30, loginonly=False)
    
    if len(AppCubes) > 0:
        dump('id', AppCubes[0].id)
        dump('url', AppCubes[0].url)
        dump('loginonly', AppCubes[0].loginonly)
        dump('type', AppCubes[0].type)
        dump('updated_at', AppCubes[0].updated_at)
        dump('jp.name', AppCubes[0].jp.name)
        dump('jp.explanation', AppCubes[0].jp.explanation)
        dump('jp.tags', AppCubes[0].jp.tags[0].name)
    else:
        print('Not found')

    AllAppCubes = getAppCubes.getAppCubes().apps(count=30, loginonly=False)