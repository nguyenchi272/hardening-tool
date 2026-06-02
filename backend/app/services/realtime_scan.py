from fastapi import WebSocket
import asyncio

from app.services.dynamic_audit_engine \
    import DynamicAuditEngine

from app.services.os_detector import OSDetector

from app.services.ssh_collector \
    import SSHCollector

from app.services.audit_factory \
    import AuditFactory


class RealtimeScanService:

    def __init__(
        self,
        websocket: WebSocket
    ):
        self.websocket = websocket
        self.collected_data = {}

    async def send_progress(
        self,
        progress,
        message
    ):

        await self.websocket.send_json({
            "type": "progress",
            "progress": progress,
            "message": message
        })

    async def send_finding(
        self,
        finding
    ):

        await self.websocket.send_json({
            "type": "finding",
            "finding":
                finding.model_dump()
        })

    async def run_multi_scan(
        self,
        hosts,
        username,
        password
    ):

        tasks = []

        for host in hosts:

            tasks.append(

                self.run_single_scan(
                    host,
                    username,
                    password
                )
            )

        results = await asyncio.gather(
            *tasks
        )

        return results

    async def run_single_scan(
        self,
        host,
        username,
        password
    ):

        collector = None

        try:

            await self.send_progress(
                15,
                f"[{host}] Connecting SSH..."
            )

            collector = SSHCollector(

                host,

                username,

                password
            )

            collector.connect()

            await self.send_progress(
                20,
                f"[{host}] Detecting OS..."
            )

            os_name = \
                OSDetector.detect(
                    collector
                )

            await self.send_progress(
                25,
                f"[{host}] Detected OS: {os_name}"
            )

            audit = \
                AuditFactory.create(

                    os_name,

                    collector
                )

            await self.send_progress(
                30,
                f"[{host}] Collecting system data..."
            )

            collected_data = \
                audit.collect()

            await self.send_progress(
                60,
                f"[{host}] Running audit engine..."
            )

            engine = DynamicAuditEngine()

            findings = engine.run(

                os_name,

                collected_data
            )

            for finding in findings:

                await self.send_finding(
                    finding
                )

                await asyncio.sleep(0.2)

            await self.send_progress(
                100,
                f"[{host}] Scan completed"
            )

            return {

                "host": host,

                "findings": findings,

                "collected_data":
                    collected_data
            }

        except Exception as e:

            await self.websocket.send_json({

                "type": "error",

                "message":
                    f"[{host}] {str(e)}"
            })

            return {

                "host": host,

                "error": str(e)
            }

        finally:

            if collector:

                collector.close()