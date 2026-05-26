from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.db.session \
    import get_db
from app.services.report_service import ReportService

router = APIRouter()

@router.get(
    "/reports/asset/{asset_id}"
)
def export_asset_report(
    asset_id: int,
    db: Session = Depends(get_db)
):

    pdf_path = \
        ReportService().generate_asset_report(
            db,
            asset_id
        )

    return FileResponse(
        pdf_path,
        media_type=
            "application/pdf",
        filename=
            f"asset_{asset_id}_report.pdf"
    )
