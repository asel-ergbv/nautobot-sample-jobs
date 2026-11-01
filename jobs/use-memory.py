from nautobot.apps import jobs


class UseMemory(jobs.Job):

    class Meta:

        name = "Use memory"
        description = "The job fills memory 1 GB at a time"

        read_only = False

    gigabytes = jobs.IntegerVar(
        description="How many GB to fill",
        default=16,
        min_value=1,
        max_value=64,
    )

    def run(self, *, gigabytes):

        chunks = []
        for i in range(gigabytes):
            chunks.append(b"\x01" * 1024**3)
            self.logger.info("Filled %s GB.", i + 1)


jobs.register_jobs(UseMemory)
