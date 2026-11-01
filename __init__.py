from nautobot.apps.jobs import IntegerVar, Job, register_jobs


class UseMemory(Job):
    gigabytes = IntegerVar(default=16)

    class Meta:
        name = "Use memory"
        description = "Fills memory 1 GB at a time to test the out-of-memory limit"

    def run(self, gigabytes):
        chunks = []
        for i in range(gigabytes):
            chunks.append(b"\x01" * 1024**3)
            self.logger.info("Filled %s GB", i + 1)


register_jobs(UseMemory)
