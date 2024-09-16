###############################################################
## Imports
###############################################################
import os

from Deadline.Events import *
from Deadline.Scripting import *

# OopCompanion:suppressRename

###############################################################
## Give Deadline an instance of this class so it can use it.
###############################################################
def GetDeadlineEventListener():
    return BotkoListener()

def CleanupDeadlineEventListener( eventListener ):
    eventListener.Cleanup()

###############################################################
## The NukeTmpFilesCleanUpListener event listener class.
###############################################################
class EventStackerListener ( DeadlineEventListener ):
    def __init__( self ):
        self.OnJobFinishedCallback += self.OnJobFinished
        self.OnJobStartedCallback += self.OnJobStarted

    def Cleanup( self ):
        del self.OnJobFinishedCallback
        del self.OnJobStartedCallback

    def OnJobStarted( self, job ):
        msg = "EventStacker is running."
        self.LogInfo("{}".format(msg))
        return

    def OnJobFinished( self, job ):
        eventType = self.GetConfigEntryWithDefault( "JobDoneMessage", "On Job Started" )

        if ( eventType == "On Job Finished" or eventType == "On Job Started and On Job Finished" ):
            self.LogInfo( "[EVENTSTACKER] - Job finished, listening ..." )
            self.RunAfterJobDone( job )
        return


    def RunAfterJobDone( self, job ):
        data_payload = str(job)
        self.LogInfo(data_payload)
        return