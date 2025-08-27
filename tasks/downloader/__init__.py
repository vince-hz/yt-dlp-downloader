#region generated meta
import typing
class Inputs(typing.TypedDict):
    targetURL: str
    saveTo: (str | None) | None
    cookies: str | None
class Outputs(typing.TypedDict):
    savedPath: str
#endregion

from oocana import Context
import download_imp
import tempfile

def main(params: Inputs, context: Context) -> Outputs:
    def progressHook(value):
        context.report_progress(value)

    cookie_file_content = params['cookies']
    cookiePath = ""
    if cookie_file_content:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(cookie_file_content)
            cookiePath = f.name
    saveTo = context.session_dir
    if params['saveTo']:
        saveTo = params['saveTo']

    path = download_imp.download_video_advanced(params['targetURL'], saveTo, cookiePath, 'best', False, progressHook)
    return {'savedPath': path}
