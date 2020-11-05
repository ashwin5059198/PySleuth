from ..core.components import ProcessMonitor
from .base import BaseController
from ..config_handler import ConfigHandler


class ProcessController(BaseController):
    def __init__(self):
        super(ProcessController, self).__init__()

        self.worker = ProcessMonitor()
        self.worker.initLogger("proc")

        cfg = ConfigHandler().getComponentSettings("Process_Monitor")
        self.worker.setPause(cfg.log_every)

        self.connectSlots()
    
    def startWorker(self):
        self.worker.start()

    def connectSlots(self):
        self.worker.SIG_process.connect(self, "onNewProcess")
    
    def onNewProcess(self, procName: str):
        self.worker.log(procName)