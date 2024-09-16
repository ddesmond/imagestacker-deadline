#!/usr/bin/env python3
"""ImageStacker.py:
Export exr layers to  PSD file format
ImageStacker can be downloaded from: https://emildohne.com/
"""
__author__ = "Katunar Aleks"
__copyright__ = "Copyright 2024, Planet Earth"
__credits__ = ["Emil Dohne", "Katunar Aleks"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "des"
__email__ = "aleks.katunar@gmail.com"
__status__ = "ReleaseCandidate"

import os
import logging
import sys
import time

from Deadline.Plugins import *


def GetDeadlinePlugin():
    """This is the function that Deadline calls to get an instance of the
    main DeadlinePlugin class.
    """
    return ImageStacker()


def CleanupDeadlinePlugin(deadlinePlugin):
    """This is the function that Deadline calls when the plugin is no
    longer in use so that it can get cleaned up.
    """
    deadlinePlugin.Cleanup()
    # move deactivate
    # no need to deactivate
    # --deactivate {optional:LicenseKey}

class ImageStacker(DeadlinePlugin):
    """This is the main DeadlinePlugin class for MyPlugin."""

    Process = None  # Variable to hold the Managed Process object.

    def __init__(self):
        """Hook up the callbacks in the constructor."""
        self.InitializeProcessCallback += self.InitializeProcess
        self.StartJobCallback += self.StartJob
        self.RenderTasksCallback += self.RenderTasks
        self.EndJobCallback += self.EndJob

    def Cleanup(self):
        """Clean up the plugin."""
        del self.InitializeProcessCallback
        del self.StartJobCallback
        del self.RenderTasksCallback
        del self.EndJobCallback

        # Clean up the managed process object.
        if self.Process:
            self.Process.Cleanup()
            del self.Process

    def InitializeProcess(self):
        """Called by Deadline to initialize the process."""
        # Set the plugin specific settings.
        self.SingleFramesOnly = True
        self.PluginType = PluginType.Advanced

    def StartJob(self):
        """Called by Deadline when the job starts."""
        time.sleep(1)
        return

    def RenderTasks(self):
        # $ ImageStackerCLI --in /Path/To/Folder --out /Path/To/OutFile
        # -c --config /path
        #-bd 32  - override bithdepth
        #-psd -psb
        #--verbosity Debug
        #--activate CLI-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX
        pass

    def EndJob(self):
        """Called by Deadline when the job ends."""
        logging.INFO("Job has finished. Check the Stacked Files.")
