from fastapi import WebSocket
import asyncio

from app.services.linux_audit \
    import LinuxAudit

from app.services.dynamic_audit_engine \
    import DynamicAuditEngine


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

        await self.send_progress(
            10,
            f"[{host}] Connecting SSH..."
        )

        audit = LinuxAudit(
            host,
            username,
            password
        )

        await self.send_progress(
            25,
            f"[{host}] Collecting system data..."
        )

        collected_data = \
            audit.collect()

        self.collected_data = collected_data

        await self.send_progress(
            60,
            f"[{host}] Running audit engine..."
        )

        try:

            engine = DynamicAuditEngine()

            findings = engine.run(
                collected_data
            )

        except Exception as e:

            print(
                "ENGINE ERROR:",
                str(e)
            )

            raise e

        print(
            f"{host} findings:",
            len(findings)
        )

        for finding in findings:

            await self.send_finding(
                finding
            )

            await asyncio.sleep(0.2)

        if len(findings) == 0:

            await self.websocket.send_json({
                "type": "info",
                "message":
                    f"[{host}] No findings detected"
            })

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