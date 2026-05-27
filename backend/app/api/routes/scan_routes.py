from fastapi \
    import APIRouter, WebSocket, WebSocketDisconnect

from sqlalchemy.orm \
    import Session

from app.db.database \
    import SessionLocal

from app.db.models.credentials \
    import Credential

from app.core.crypto \
    import decrypt

from app.websocket.connection_manager \
    import ConnectionManager

from app.websocket.scan_manager \
    import ScanManager

router = APIRouter()

manager = ConnectionManager()

LATEST_FINDINGS = []


@router.websocket("/ws/scan")
async def websocket_scan(
    websocket: WebSocket
):

    global LATEST_FINDINGS

    await manager.connect(
        websocket
    )

    db: Session = SessionLocal()

    try:

        data = \
            await websocket.receive_json()

        hosts = data["hosts"]

        credential_id = \
            data["credential_id"]

        #
        # Load credential
        #
        credential = db.query(
            Credential
        ).filter(
            Credential.id ==
            credential_id
        ).first()

        if not credential:

            await websocket.send_json({

                "type": "error",

                "message":
                    "Credential not found"
            })

            return

        #
        # Decrypt password
        #
        password = decrypt(
            credential.encrypted_password
        )

        username = \
            credential.username

        #
        # Start scan
        #
        scan_manager = \
            ScanManager(websocket)
        
        credential_id = data["credential_id"]

        findings = \
            await scan_manager.run_scan(

                hosts,

                credential_id
            )

        LATEST_FINDINGS = findings

    except WebSocketDisconnect:

        manager.disconnect(
            websocket
        )

        print(
            "Client disconnected"
        )

    except Exception as e:

        await websocket.send_json({

            "type": "error",

            "message": str(e)
        })

    finally:

        db.close()

        try:

            await websocket.close()

        except:
            pass