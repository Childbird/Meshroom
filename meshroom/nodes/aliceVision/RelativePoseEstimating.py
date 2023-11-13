__version__ = "1.0"

from meshroom.core import desc

class RelativePoseEstimating(desc.AVCommandLineNode):
    commandLine = 'aliceVision_relativePoseEstimating {allParams}'
    size = desc.DynamicNodeSize('input')
    
    parallelization = desc.Parallelization(blockSize=25)
    commandLineRange = '--rangeStart {rangeStart} --rangeSize {rangeBlockSize}'
    

    category = 'Sparse Reconstruction'
    documentation = '''
Estimate relative pose between each pair of views that share tracks.
'''

    inputs = [
        desc.File(
            name="input",
            label="SfMData",
            description="SfMData file.",
            value="",
            uid=[0],
        ),
        desc.File(
            name="tracksFilename",
            label="Tracks File",
            description="Tracks file.",
            value="",
            uid=[0],
        ),
        desc.BoolParam(
            name="enforcePureRotation",
            label="Enforce pure rotation",
            description="Enforce pure rotation as a model",
            value=False,
            uid=[0],
        ),
        desc.ChoiceParam(
            name="verboseLevel",
            label="Verbose Level",
            description="Verbosity level (fatal, error, warning, info, debug, trace).",
            value="info",
            values=["fatal", "error", "warning", "info", "debug", "trace"],
            exclusive=True,
            uid=[],
        )
    ]

    outputs = [
        desc.File(
            name="output",
            label="Pairs Info",
            description="Path to the output Pairs info files directory.",
            value=desc.Node.internalFolder,
            uid=[],
        )
    ]
