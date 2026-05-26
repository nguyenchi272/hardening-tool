from sqlalchemy.orm \
    import Session

from app.services.realtime_scan \
    import RealtimeScanService

from app.services.persistence_service \
    import PersistenceService

from app.db.database \
    import SessionLocal

from app.websocket.events \
    import (
        SCAN_COMPLETED,
        SCAN_ERROR
    )


class ScanManager:

    def __init__(
        self,
        websocket
    ):

        self.websocket = websocket

    async def run_scan(
        self,
        hosts,
        username,
        password
    ):

        scanner = \
            RealtimeScanService(
                self.websocket
            )

        results = \
            await scanner.run_multi_scan(
                hosts,
                username,
                password
            )

        db: Session = SessionLocal()

        all_findings = []

        try:

            for result in results:

                #
                # Skip failed hosts
                #
                if isinstance(
                    result,
                    Exception
                ):
                    continue

                host = \
                    result["host"]

                findings = \
                    result["findings"]

                collected_data = \
                    result[
                        "collected_data"
                    ]

                PersistenceService().save_scan(

                    db,

                    host,

                    findings,

                    collected_data
                )

                all_findings.extend(
                    findings
                )

            await self.websocket.send_json({

                "type":
                    SCAN_COMPLETED,

                "findings_count":
                    len(all_findings)
            })

            return all_findings

        except Exception as e:

            await self.websocket.send_json({

                "type":
                    SCAN_ERROR,

                "message":
                    str(e)
            })

        finally:

            db.close()