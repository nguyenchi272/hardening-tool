// Findings.ts
export interface Finding {

  id: string

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

  status: string
}