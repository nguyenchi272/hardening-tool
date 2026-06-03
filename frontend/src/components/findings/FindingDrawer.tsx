import {
  X,
  ShieldCheck
} from "lucide-react"

import {
  useState
} from "react"

import { Finding }
  from "../../types/finding"

import FixModal
  from "./FixModal"

interface Props {

  finding: Finding

  onClose: () => void
}

export default function FindingDrawer({
  finding,
  onClose
}: Props) {

  const [showFix, setShowFix] =
    useState(false)
  return (

    <>

      <div
        className="
          fixed
          inset-0
          z-50
          flex
          justify-end
          bg-black/50
          backdrop-blur-sm
        "
      >

        <div
          className="
            h-full
            w-[700px]
            overflow-y-auto
            border-l
            border-slate-800
            bg-[#081121]
            p-8
          "
        >

          <div
            className="
              mb-8
              flex
              items-start
              justify-between
            "
          >

            <div>

              <p
                className="
                  text-sm
                  text-slate-500
                "
              >
                {finding.finding_id}
              </p>

              <h2
                className="
                  mt-2
                  text-3xl
                  font-bold
                "
              >
                {finding.title}
              </h2>

            </div>

            <button
              onClick={onClose}
              className="
                rounded-lg
                p-2
                transition-all
                hover:bg-slate-800
              "
            >
              <X size={20} />
            </button>

          </div>

          <div className="space-y-6">

            <Section
              title="Description"
              content={finding.description}
            />

            <Section
              title="Impact"
              content={finding.impact}
            />

            <Section
              title="Evidence"
              content={finding.evidence}
            />

            <Section
              title="Remediation"
              content={finding.remediation}
            />

            <div
              className="
                rounded-xl
                border
                border-slate-800
                bg-slate-900/40
                p-5
              "
            >

              <h3
                className="
                  mb-4
                  text-lg
                  font-semibold
                "
              >
                Metadata
              </h3>

              <div className="space-y-3">

                <MetaRow
                  label="Severity"
                  value={finding.severity}
                />

                <MetaRow
                  label="Risk Score"
                  value={
                    String(
                      finding.risk_score
                    )
                  }
                />

                <MetaRow
                  label="Category"
                  value={finding.category}
                />

                <MetaRow
                  label="Status"
                  value={finding.status}
                />

                <MetaRow
                  label="Hostname"
                  value={finding.server}
                />

                <MetaRow
                  label="IP Address"
                  value={finding.host}
                />

              </div>

            </div>

            <TagSection
              title="Compliance"
              items={finding.compliance}
            />

            <TagSection
              title="Tags"
              items={finding.tags}
            />

            <TagSection
              title="References"
              items={finding.references}
            />

          {finding.auto_fix_supported && (
            <button
              onClick={() =>
                setShowFix(true)
              }
              className="
                flex
                w-full
                items-center
                justify-center
                gap-2
                rounded-xl
                bg-green-600
                py-4
                font-semibold
                transition-all
                hover:bg-green-500
              "
            >

              <ShieldCheck size={18} />

              Auto Fix Finding

            </button>
          )}
          </div>

        </div>

      </div>

      <FixModal
        open={showFix}
        assetId={finding.asset_id}
        findingId={
          finding.finding_id
        }
        onClose={() =>
          setShowFix(false)
        }
      />

    </>

  )
}

function Section({
  title,
  content
}: {
  title: string
  content: string
}) {

  return (

    <div
      className="
        rounded-xl
        border
        border-slate-800
        bg-slate-900/40
        p-5
      "
    >

      <h3
        className="
          mb-3
          text-lg
          font-semibold
        "
      >
        {title}
      </h3>

      <p
        className="
          whitespace-pre-wrap
          text-slate-300
        "
      >
        {content}
      </p>

    </div>
  )
}

function MetaRow({
  label,
  value
}: {
  label: string
  value: string
}) {

  return (

    <div
      className="
        flex
        items-center
        justify-between
      "
    >

      <span
        className="
          text-slate-500
        "
      >
        {label}
      </span>

      <span
        className="
          font-medium
        "
      >
        {value}
      </span>

    </div>
  )
}

function TagSection({
  title,
  items
}: {
  title: string
  items: string[]
}) {

  return (

    <div
      className="
        rounded-xl
        border
        border-slate-800
        bg-slate-900/40
        p-5
      "
    >

      <h3
        className="
          mb-4
          text-lg
          font-semibold
        "
      >
        {title}
      </h3>

      <div
        className="
          flex
          flex-wrap
          gap-2
        "
      >

        {items.map((item) => (

          <span
            key={item}
            className="
              rounded-full
              bg-slate-800
              px-3
              py-1
              text-sm
            "
          >
            {item}
          </span>
        ))}

      </div>

    </div>
  )
}