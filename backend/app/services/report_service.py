from reportlab.platypus \
    import (
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle
    )

from reportlab.lib \
    import colors

from reportlab.lib.styles \
    import getSampleStyleSheet

from sqlalchemy.orm \
    import Session

from app.db.models.asset \
    import Asset

from app.db.models.scan \
    import Scan

from app.db.models.finding \
    import FindingRecord


class ReportService:

    def generate_asset_report(
        self,
        db: Session,
        asset_id: int
    ):

        asset = db.query(
            Asset
        ).filter(
            Asset.id == asset_id
        ).first()

        scans = db.query(
            Scan
        ).filter(
            Scan.asset_id == asset.id
        ).all()

        findings = []

        for scan in scans:

            finding_records = db.query(
                FindingRecord
            ).filter(
                FindingRecord.scan_id == scan.id
            ).all()

            findings.extend(
                finding_records
            )

        pdf_path = \
            f"reports/asset_{asset.id}.pdf"

        doc = SimpleDocTemplate(
            pdf_path
        )

        styles = \
            getSampleStyleSheet()

        elements = []

        #
        # Title
        #
        elements.append(

            Paragraph(
                "Security Assessment Report",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        #
        # Asset Info
        #
        elements.append(
            Paragraph(
                f"<b>Hostname:</b> {asset.hostname}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"<b>IP:</b> {asset.ip_address}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"<b>OS:</b> {asset.os}",
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        #
        # Findings Table
        #
        table_data = [[
            "Finding",
            "Severity",
            "Status"
        ]]

        for finding in findings:

            table_data.append([

                finding.title,

                finding.severity,

                finding.status
            ])

        table = Table(
            table_data,
            colWidths=[
                300,
                100,
                100
            ]
        )

        table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.darkblue
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.grey
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
            ])
        )

        elements.append(
            table
        )

        doc.build(elements)

        return pdf_path