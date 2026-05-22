from datetime \
    import datetime

from sqlalchemy.orm \
    import Session

from app.db.models.asset \
    import Asset

from app.db.models.scan \
    import Scan

from app.db.models.finding \
    import FindingRecord

from app.utils.os_parser \
    import parse_os_name


class PersistenceService:

    def save_scan(
        self,
        db: Session,
        host: str,
        findings,
        collected_data
    ):

        #
        # Real hostname
        #
        real_hostname = \
            collected_data.get(
                "hostname",
                host
            ).strip()

        #
        # Real OS
        #
        real_os = parse_os_name(
            collected_data.get(
                "os_version",
                ""
            )
        )

        #
        # Find existing asset
        #
        asset = db.query(
            Asset
        ).filter(
            Asset.hostname ==
                real_hostname
        ).first()

        #
        # Create asset
        #
        if not asset:

            asset = Asset(
                hostname=real_hostname,

                ip_address=host,

                os=real_os,

                status="Online"
            )

            db.add(asset)

            db.commit()

            db.refresh(asset)

        #
        # Update asset info
        #
        else:

            asset.ip_address = host

            asset.os = real_os

            asset.status = "Online"

            db.commit()

        #
        # DELETE OLD SCANS
        #
        old_scans = db.query(
            Scan
        ).filter(
            Scan.asset_id == asset.id
        ).all()

        old_scan_ids = [
            scan.id
            for scan in old_scans
        ]

        #
        # DELETE OLD FINDINGS
        #
        if old_scan_ids:

            db.query(
                FindingRecord
            ).filter(
                FindingRecord.scan_id.in_(
                    old_scan_ids
                )
            ).delete(
                synchronize_session=False
            )

            db.query(
                Scan
            ).filter(
                Scan.asset_id == asset.id
            ).delete(
                synchronize_session=False
            )

            db.commit()

        #
        # Create new scan
        #
        scan = Scan(
            asset_id=asset.id,

            status="Completed",

            completed_at=datetime.utcnow()
        )

        db.add(scan)

        db.commit()

        db.refresh(scan)

        #
        # Save findings
        #
        for finding in findings:

            finding_record = \
                FindingRecord(

                    scan_id=scan.id,

                    finding_id=
                        finding.finding_id,

                    title=
                        finding.title,

                    severity=
                        finding.severity,

                    evidence=
                        finding.evidence,

                    remediation=
                        finding.remediation,

                    status=
                        finding.status
                )

            db.add(
                finding_record
            )

        db.commit()

        return scan.id