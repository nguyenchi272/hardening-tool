// Findings.ts
export interface Finding {

  id: string

  asset_id: number

  finding_id: string

  title: string

  severity: string

  risk_score: number

  category: string

  description: string

  impact: string

  evidence: string

  remediation: string

  references: string[]

  compliance: string[]

  tags: string[]

  server: string

  host: string

  ip_address: string

  status: string

  auto_fix_supported: boolean

  requires_restart: boolean

  requires_reboot: boolean

  manual_review: boolean
}