from fastapi import APIRouter

from app.api.routes.health_routes \
    import router as health_router

from app.api.routes.scan_routes \
    import router as scan_router

from app.api.routes.dashboard_routes \
    import router as dashboard_router

from app.api.routes.asset_routes \
    import router as asset_router

from app.api.routes.report_routes \
    import router as report_router

from app.api.routes.remediation_routes \
    import router as remediation_router

from app.api.routes.credential_routes \
    import router as credential_router


router = APIRouter(
    prefix="/api/v1"
)

router.include_router(
    health_router
)

router.include_router(
    scan_router
)

router.include_router(
    dashboard_router
)

router.include_router(
    asset_router
)

router.include_router(
    report_router
)

router.include_router(
    remediation_router
)

router.include_router(
    credential_router
)