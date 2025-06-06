#region generated meta
import typing
class Inputs(typing.TypedDict):
    targetURL: str
    saveTo: str | str
class Outputs(typing.TypedDict):
    savedPath: str
#endregion

from oocana import Context
import download_imp

def main(params: Inputs, context: Context) -> Outputs:
    def progressHook(value):
        context.report_progress(value)

    path = download_imp.download_video_advanced(params['targetURL'], params['saveTo'], 'best', False, progressHook)
    return {'savedPath': path}
