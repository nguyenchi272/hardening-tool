from fastapi \
    import APIRouter, WebSocket, WebSocketDisconnect

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

    try:

        data = \
            await websocket.receive_json()

        hosts = data["hosts"]

        username = data["username"]

        password = data["password"]

        scan_manager = \
            ScanManager(websocket)

        findings = \
            await scan_manager.run_scan(

                hosts,

                username,

                password
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

        try:

            await websocket.close()

        except:
            pass